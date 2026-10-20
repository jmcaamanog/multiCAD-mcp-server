"""
Unit tests for ConTech Bridge: multiCAD-MCP ➔ CE3X-MCP-SERVER.
"""

import json
import os
from unittest.mock import patch
import pytest

from adapters.ezdxf_adapter import EzdxfAdapter
from mcp_tools.tools.ce3x_bridge import _calculate_orientation, extract_thermal_envelope


class TestCe3xOrientationCalculation:
    """Test vector normal orientation math for facade wall segments."""

    def test_north_facing_wall(self):
        # Horizontal wall from right to left (exterior normal points +Y / North)
        # p1=(10, 0), p2=(0, 0) -> dx = -10, dy = 0 -> nx = 0, ny = 10 -> pointing +Y (North)
        orient = _calculate_orientation((10, 0), (0, 0))
        assert orient == "Norte"

    def test_south_facing_wall(self):
        # Horizontal wall from left to right (exterior normal points -Y / South)
        # p1=(0, 0), p2=(10, 0) -> dx = 10, dy = 0 -> nx = 0, ny = -10 -> pointing -Y (South)
        orient = _calculate_orientation((0, 0), (10, 0))
        assert orient == "Sur"

    def test_east_facing_wall(self):
        # Vertical wall from bottom to top (exterior normal points +X / East)
        # p1=(0, 0), p2=(0, 10) -> dx = 0, dy = 10 -> nx = 10, ny = 0 -> pointing +X (East)
        orient = _calculate_orientation((0, 0), (0, 10))
        assert orient == "Este"

    def test_west_facing_wall(self):
        # Vertical wall from top to bottom (exterior normal points -X / West)
        # p1=(0, 10), p2=(0, 0) -> dx = 0, dy = -10 -> nx = -10, ny = 0 -> pointing -X (West)
        orient = _calculate_orientation((0, 10), (0, 0))
        assert orient == "Oeste"


class TestCe3xEnvelopeExtraction:
    """Test full thermal envelope scanning and JSON export."""

    def test_extract_envelope_from_cad_model(self, tmp_path):
        adapter = EzdxfAdapter()
        adapter.create_layer("A-WALL")
        # Draw a building envelope: 10m x 8m
        # South facade: (0,0) -> (10,0) (10m)
        adapter.draw_line((0, 0), (10, 0), layer="A-WALL")
        # East facade: (10,0) -> (10,8) (8m)
        adapter.draw_line((10, 0), (10, 8), layer="A-WALL")
        # North facade: (10,8) -> (0,8) (10m)
        adapter.draw_line((10, 8), (0, 8), layer="A-WALL")
        # West facade: (0,8) -> (0,0) (8m)
        adapter.draw_line((0, 8), (0, 0), layer="A-WALL")

        # Floor footprint (80 m²)
        adapter.create_layer("A-ESTANCIAS")
        adapter.draw_rectangle((0, 0), (10, 8), layer="A-ESTANCIAS")

        payload = extract_thermal_envelope(
            adapter,
            wall_height=3.0,
            climate_zone="C1",
            building_type="vivienda_individual",
        )

        assert payload["target"] == "CE3X-MCP-SERVER"
        assert payload["climate_zone"] == "C1"
        assert payload["usable_floor_area_m2"] == pytest.approx(80.0, 0.1)

        envelopes = payload["thermal_envelopes"]
        orientations = [env["orientacion"] for env in envelopes]
        assert "Sur" in orientations
        assert "Norte" in orientations
        assert "Este" in orientations
        assert "Oeste" in orientations

        # South facade area: 10m * 3m = 30 m²
        south_env = next(e for e in envelopes if e["orientacion"] == "Sur")
        assert south_env["superficie_bruta_m2"] == pytest.approx(30.0, 0.1)
