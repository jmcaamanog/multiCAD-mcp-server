"""
Unit tests for AECO Features: Architectural Macros (wall, door, window),
FIEBDC-3 (.bc3) Export, CAD QA Audit, and Layer Purge.
"""

from unittest.mock import patch
import os
import json
import pytest

from adapters.ezdxf_adapter import EzdxfAdapter
from mcp_tools.tools.drawing import _draw_wall, _draw_door, _draw_window
from mcp_tools.tools.export import _export_bc3
from mcp_tools.tools.layers import _purge
from mcp_tools.tools.entities import _audit
from mcp_tools.shorthand import parse_entity_shorthand, parse_layer_op_shorthand, parse_entity_op_shorthand


class TestAecoArchitecturalMacros:
    """Test wall, door, and window macros."""

    def test_parse_wall_shorthand(self):
        spec = parse_entity_shorthand("wall|0,0|10,0|0.30|red|A-MURO")
        assert spec["type"] == "wall"
        assert spec["thickness"] == 0.30
        assert spec["color"] == "red"
        assert spec["layer"] == "A-MURO"

    def test_draw_wall_execution(self):
        adapter = EzdxfAdapter()
        with patch("mcp_tools.tools.drawing.get_current_adapter", return_value=adapter):
            handle = _draw_wall({
                "start": "0,0",
                "end": "10,0",
                "thickness": 0.20,
                "layer": "A-WALLS",
                "color": "red",
            })
            assert handle is not None
            props = adapter.get_entity_properties(handle)
            assert props["object_name"] == "LWPOLYLINE"
            area_info = adapter.get_entity_area(handle)
            # Wall of 10m length x 0.20m thickness = 2.0 m²
            assert area_info["area"] == pytest.approx(2.0, 0.05)

    def test_draw_door_execution(self):
        adapter = EzdxfAdapter()
        with patch("mcp_tools.tools.drawing.get_current_adapter", return_value=adapter):
            handle = _draw_door({
                "hinge": "5,5",
                "width": 0.82,
                "angle": 0.0,
                "layer": "A-DOORS",
                "color": "green",
            })
            assert handle is not None

    def test_draw_window_execution(self):
        adapter = EzdxfAdapter()
        with patch("mcp_tools.tools.drawing.get_current_adapter", return_value=adapter):
            handle = _draw_window({
                "start": "2,0",
                "end": "4,0",
                "thickness": 0.10,
                "layer": "A-WINDOWS",
                "color": "cyan",
            })
            assert handle is not None


class TestFiebdc3Bc3Export:
    """Test exporting CAD measurements to FIEBDC-3 (.bc3) budget format."""

    def test_export_bc3_generates_file(self, tmp_path):
        adapter = EzdxfAdapter()
        adapter.create_layer("A-ESTANCIAS")
        adapter.draw_rectangle((0, 0), (6, 5), layer="A-ESTANCIAS")  # 30 m²

        with patch("mcp_tools.tools.export.get_current_adapter", return_value=adapter):
            with patch("core.config.get_config") as mock_cfg:
                mock_cfg.return_value.output.directory = str(tmp_path)
                res_raw = _export_bc3(adapter, "test_presupuesto.bc3")
                res = json.loads(res_raw)
                assert res["success"] is True
                assert res["count"] == 1
                assert res["total_area"] == pytest.approx(30.0, 0.1)
                assert os.path.exists(res["path"])

                with open(res["path"], "r", encoding="latin-1") as f:
                    content = f.read()
                    assert "~V|FIEBDC-3/2020|" in content
                    assert "~C|OBRA##|" in content
                    assert "~M|CAP01##\\" in content


class TestCadQaAndPurge:
    """Test CAD QA audit and layer purging."""

    def test_purge_unused_layers(self):
        adapter = EzdxfAdapter()
        adapter.create_layer("EMPTY_UNUSED_LAYER")
        adapter.create_layer("USED_LAYER")
        adapter.draw_line((0, 0), (1, 1), layer="USED_LAYER")

        with patch("mcp_tools.tools.layers.get_current_adapter", return_value=adapter):
            res = _purge({})
            assert res["success"] is True
            assert "EMPTY_UNUSED_LAYER" in res["purged_layers"]
            assert "USED_LAYER" not in res["purged_layers"]
            assert "0" not in res["purged_layers"]

    def test_audit_drawing_qa(self):
        adapter = EzdxfAdapter()
        adapter.draw_line((0, 0), (10, 10), layer="0")  # drawing on layer 0

        with patch("mcp_tools.tools.entities.get_current_adapter", return_value=adapter):
            res = _audit({})
            assert res["success"] is True
            assert res["issues_count"] >= 1
            assert res["issues"][0]["type"] == "layer_0_entities"


class TestEzdxfVisualPreview:
    """Test vector preview generation in EzdxfAdapter."""

    def test_export_view_svg(self, tmp_path):
        adapter = EzdxfAdapter()
        adapter.draw_rectangle((0, 0), (20, 15))
        svg_file = os.path.join(tmp_path, "preview_test.svg")
        res = adapter.export_view(filepath=svg_file)
        assert res["format"] == "svg"
        assert res["length"] > 0
        assert os.path.exists(svg_file)
        with open(svg_file, "r", encoding="utf-8") as f:
            svg_content = f.read()
            assert "<svg" in svg_content
