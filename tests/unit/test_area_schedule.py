"""
Unit tests for Area and Area Table Schedule operations (AECO & ConTech).
"""

from unittest.mock import MagicMock, patch
import pytest

from mcp_tools.shorthand import parse_entity_op_shorthand
from mcp_tools.tools.entities import _area, _area_table
from adapters.ezdxf_adapter import EzdxfAdapter


class TestAreaShorthandParsing:
    """Test shorthand parsing for area and area_table commands."""

    def test_parse_area_default(self):
        res = parse_entity_op_shorthand("area")
        assert res["action"] == "area"
        assert res["handles"] == "all"

    def test_parse_area_handles(self):
        res = parse_entity_op_shorthand("area|A1,B2")
        assert res["action"] == "area"
        assert res["handles"] == "A1,B2"

    def test_parse_area_layer(self):
        res = parse_entity_op_shorthand("area|layer|A-ESTANCIAS")
        assert res["action"] == "area"
        assert res["layer"] == "A-ESTANCIAS"

    def test_parse_area_table(self):
        res = parse_entity_op_shorthand("area_table|100,200|A-ESTANCIAS|Cuadro de Zonas")
        assert res["action"] == "area_table"
        assert res["insertion_point"] == "100,200"
        assert res["layer"] == "A-ESTANCIAS"
        assert res["title"] == "Cuadro de Zonas"


class TestAreaHandlerExecution:
    """Test _area and _area_table execution with EzdxfAdapter."""

    def test_area_calculation_with_ezdxf(self):
        adapter = EzdxfAdapter()
        adapter.create_layer("A-ROOMS")
        h1 = adapter.draw_rectangle((0, 0), (10, 5), layer="A-ROOMS")
        h2 = adapter.draw_rectangle((0, 0), (4, 4), layer="A-ROOMS")

        with patch("mcp_tools.tools.entities.get_current_adapter", return_value=adapter):
            res = _area({"layer": "A-ROOMS"})
            assert res["success"] is True
            assert res["count"] == 2
            # 10*5 = 50, 4*4 = 16 => Total 66
            assert res["total_area"] == pytest.approx(66.0, 0.01)
            # Perimeters: 2*(10+5)=30, 2*(4+4)=16 => Total 46
            assert res["total_perimeter"] == pytest.approx(46.0, 0.01)

    def test_area_table_generation_with_ezdxf(self):
        adapter = EzdxfAdapter()
        adapter.create_layer("A-ESTANCIAS")
        adapter.draw_rectangle((0, 0), (10, 10), layer="A-ESTANCIAS")
        adapter.draw_rectangle((20, 0), (25, 10), layer="A-ESTANCIAS")

        with patch("mcp_tools.tools.entities.get_current_adapter", return_value=adapter):
            res = _area_table({
                "layer": "A-ESTANCIAS",
                "insertion_point": "100,100",
                "title": "CUADRO GENERAL DE SUPERFICIES",
            })
            assert res["success"] is True
            assert res["spaces_count"] == 2
            # 10*10 = 100, 5*10 = 50 => Total 150
            assert res["total_area"] == pytest.approx(150.0, 0.01)
            assert res["table_handle"] is not None

    def test_area_table_no_entities_returns_graceful_error(self):
        adapter = EzdxfAdapter()
        with patch("mcp_tools.tools.entities.get_current_adapter", return_value=adapter):
            res = _area_table({"layer": "NON_EXISTENT_LAYER"})
            assert res["success"] is False
            assert "No measurable entities found" in res["error"]
