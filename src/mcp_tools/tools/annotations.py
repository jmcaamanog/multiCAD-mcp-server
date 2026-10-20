"""
Smart Architectural Annotations & Dimensioning tools.

Features:
- manage_annotations: Automated dimensioning (bounding box, polyline segments),
  space labeling (centroids with calculated m² and room names), and callouts/leaders.
"""

import json
import math
import logging
from typing import Dict, Any, List, Optional, Union

from mcp_tools.decorators import cad_tool, get_current_adapter
from mcp_tools.helpers import parse_coordinate
from mcp_tools.tools.inspection import _get_drawing_entities_data

logger = logging.getLogger(__name__)


def register_annotation_tools(mcp):
    """Register architectural annotation tools with FastMCP."""

    @cad_tool(mcp, "manage_annotations")
    def manage_annotations(
        action: str = "label_spaces",
        handles: Optional[Union[List[str], str]] = None,
        style: str = "overall",
        offset: float = 1.0,
        text_height: float = 0.35,
        prefix: str = "",
        suffix: str = " m²",
        layer: Optional[str] = None,
        color: Optional[str] = None,
    ) -> str:
        """Create automated architectural annotations, centroid room labels, and linear dimension chains.

        Behavior:
        - Mutation: Mutates drawing by generating and placing new annotation text, dimensions, and leaders.
        - Persistence: Inserted annotations persist in DWG/DXF database upon save.
        - Side Effects: Auto-creates destination annotation layers (e.g. A-ANNO-TEXT, A-ANNO-DIMS) if nonexistent.

        Usage Guidelines:
        - When to Use: Call to automatically label room centroids with computed areas (m²), generate overall or wall-by-wall linear dimension chains, or add leader callouts with arrowheads.
        - Sibling Routing / Alternatives:
          * For manually drafting single primitive dimensions or leaders with custom points, use `draw_entities(entities="dimension|... / leader|...")`.
          * For modifying, moving, restyling, or deleting existing annotation entities, use `manage_entities`.
          * For room scheduling tables, use `manage_entities(operations="area_table|...")`.

        Actions & Parameters:
        - "label_spaces": Places text label with room name and computed area at centroid of closed room spaces.
        - "auto_dimension": Generates exterior linear dimension chain along bounding box or wall segments.
        - "add_leader": Inserts architectural callout leader pointing to specified geometry.

        Parameters:
        - action: Action to perform ("label_spaces", "auto_dimension", "add_leader"). Default: "label_spaces".
        - handles: Optional entity handle or list of handles to annotate. If None, processes all spaces.
        - style: Dimensioning style for "auto_dimension" ("overall" for global extents, "segments" for each wall). Default: "overall".
        - offset: Offset distance in drawing units between geometry and dimension line. Default: 1.0.
        - text_height: Text height for labels and dimensions in drawing units. Default: 0.35.
        - prefix: Text prefix added before calculated area value (e.g. "Sup = "). Default: "".
        - suffix: Text suffix appended after area value. Default: " m²".
        - layer: Target layer name (default: "A-ANNO-TEXT" for space labels, "A-ANNO-DIMS" for dimensions).
        - color: Optional color name or ACI number.

        Returns:
            JSON string containing created annotation handles, count, and status.
        """
        adapter = get_current_adapter()
        action_lower = action.lower().strip()

        # Normalize handles if passed as string or comma-separated list
        target_handles = None
        if handles:
            if isinstance(handles, str):
                target_handles = [h.strip() for h in handles.split(",") if h.strip()]
            else:
                target_handles = [str(h).strip() for h in handles]

        # Extract drawing data
        data = _get_drawing_entities_data(adapter)
        spaces = data["spaces"]
        if target_handles:
            spaces = [s for s in spaces if s["handle"] in target_handles]

        created_entities = []

        # ==========================================
        # ACTION: label_spaces
        # ==========================================
        if action_lower in ("label_spaces", "label", "etiquetar", "rotular"):
            target_layer = layer or "A-ANNO-TEXT"
            text_color = color or "yellow"

            # Ensure layer exists
            if hasattr(adapter, "create_layer"):
                try:
                    adapter.create_layer(target_layer, color=text_color)
                except Exception:
                    pass

            for s in spaces:
                cx, cy = s["centroid"]
                area = s["area"]
                metadata = s.get("metadata", {})
                room_name = (
                    metadata.get("nombre")
                    or metadata.get("name")
                    or metadata.get("tipo")
                    or metadata.get("type")
                    or f"Espacio #{s['handle']}"
                )

                label_text = f"{room_name}\n{prefix}{area:.2f}{suffix}"

                # Draw text using adapter
                if hasattr(adapter, "draw_text"):
                    h = adapter.draw_text(
                        position=(cx, cy, 0.0),
                        text=label_text,
                        height=text_height,
                        layer=target_layer,
                        color=text_color,
                    )
                    created_entities.append({
                        "handle": h,
                        "type": "TEXT",
                        "text": label_text,
                        "position": (cx, cy),
                        "room_handle": s["handle"],
                        "area_m2": area,
                    })

            return json.dumps({
                "success": True,
                "action": "label_spaces",
                "layer": target_layer,
                "count": len(created_entities),
                "labels": created_entities,
                "message": f"Successfully labeled {len(created_entities)} spaces with centroid areas.",
            }, indent=2, ensure_ascii=False)

        # ==========================================
        # ACTION: auto_dimension
        # ==========================================
        elif action_lower in ("auto_dimension", "dimension", "acotar", "cotas"):
            target_layer = layer or "A-ANNO-DIMS"
            dim_color = color or "cyan"

            if hasattr(adapter, "create_layer"):
                try:
                    adapter.create_layer(target_layer, color=dim_color)
                except Exception:
                    pass

            style_lower = style.lower().strip()

            if style_lower in ("overall", "bbox", "exterior", "general"):
                # Dimension the overall bounding box (Horizontal bottom + Vertical left)
                bbox = data["bbox"]
                min_x, max_x = bbox["min_x"], bbox["max_x"]
                min_y, max_y = bbox["min_y"], bbox["max_y"]

                # Bottom horizontal dimension
                h_bot = adapter.add_dimension(
                    start=(min_x, min_y, 0.0),
                    end=(max_x, min_y, 0.0),
                    offset=offset,
                    layer=target_layer,
                    color=dim_color,
                )
                created_entities.append({
                    "handle": h_bot,
                    "type": "DIMENSION",
                    "subtype": "horizontal_overall",
                    "length": bbox["width"],
                    "start": (min_x, min_y),
                    "end": (max_x, min_y),
                })

                # Left vertical dimension
                h_left = adapter.add_dimension(
                    start=(min_x, min_y, 0.0),
                    end=(min_x, max_y, 0.0),
                    offset=offset,
                    layer=target_layer,
                    color=dim_color,
                )
                created_entities.append({
                    "handle": h_left,
                    "type": "DIMENSION",
                    "subtype": "vertical_overall",
                    "length": bbox["length"],
                    "start": (min_x, min_y),
                    "end": (min_x, max_y),
                })

            elif style_lower in ("segments", "walls", "perimetral", "tramos"):
                # Dimension each segment of selected closed polylines/rooms
                for s in spaces:
                    poly = s["polygon"]
                    n = len(poly)
                    for i in range(n):
                        p1 = poly[i]
                        p2 = poly[(i + 1) % n]
                        seg_len = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
                        if seg_len < 0.1:
                            continue

                        h_dim = adapter.add_dimension(
                            start=(p1[0], p1[1], 0.0),
                            end=(p2[0], p2[1], 0.0),
                            offset=offset,
                            layer=target_layer,
                            color=dim_color,
                        )
                        created_entities.append({
                            "handle": h_dim,
                            "type": "DIMENSION",
                            "subtype": "segment",
                            "room_handle": s["handle"],
                            "length": round(seg_len, 2),
                            "start": p1,
                            "end": p2,
                        })

            return json.dumps({
                "success": True,
                "action": "auto_dimension",
                "style": style_lower,
                "layer": target_layer,
                "count": len(created_entities),
                "dimensions": created_entities,
                "message": f"Created {len(created_entities)} dimension annotations.",
            }, indent=2, ensure_ascii=False)

        else:
            return json.dumps({
                "success": False,
                "error": f"Unknown action '{action}'. Supported actions: 'label_spaces', 'auto_dimension'.",
            })
