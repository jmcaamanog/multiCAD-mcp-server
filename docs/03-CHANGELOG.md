# Changelog

All notable changes to multiCAD-mcp will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **CLI Binary Entrypoint**: Added `[project.scripts]` in `pyproject.toml` exposing `multicad-mcp` command (`multicad-mcp = "server:main"`), enabling direct CLI execution and `uvx multiCAD-mcp` support.
- **CLI Flags**: Added `main()` entrypoint function in `src/server.py` supporting `--transport {stdio,http}`, `--host`, `--port`, and `--no-dashboard` arguments.
- **1-Click Windows Installer**: Added `instalar_en_claude_desktop.bat` and `scripts/instalar_claude_desktop.py` for automated, non-destructive configuration of Claude Desktop and Cursor with automatic `.bak` backups.
- **Resilient Shorthand Input Parsing**: Enhanced `parse_drawing_input`, `parse_entity_ops_input`, `parse_layer_ops_input`, `parse_block_ops_input`, and `parse_file_ops_input` in `src/mcp_tools/shorthand.py` to natively accept Python `list` and `dict` objects in addition to shorthand strings.
- **Architectural Macros (`wall`, `door`, `window`)**: Added high-level architectural shorthand commands in `draw_entities` (`wall|start|end|thickness|layer|color`, `door|start|end|swing_direction|thickness|layer|color`, `window|start|end|thickness|layer|color`) allowing LLMs to draft floorplans with standard wall double lines, door openings with arcs, and window frames with single commands.
- **FIEBDC-3 (`.bc3`) Budget & Cost Export**: Added standard Spanish ConTech exchange format support in `export_data(format="bc3", filename=...)`, parsing CAD boundaries into classified measurement lines compatible with Presto, Arquímedes, and Menfis.
- **Headless Vector Visual Preview (SVG)**: Added `export_view` / `get_screenshot` in `EzdxfAdapter` returning clean SVG vector renders with model bounding box auto-detection, providing instant visual feedback loops for multimodal LLMs.
- **CAD Quality Assurance & Layer Purge**: Added `audit` action in `manage_entities` detecting zero-length lines, duplicate overlaps, and layer 0 infractions; added `purge` action in `manage_layers` automatically removing unused layers.
- **GitHub CI/CD Automation Workflows**: Added multi-OS automated testing (`.github/workflows/ci.yml`), automated GitHub releases (`.github/workflows/release.yml`), issue templates, and Smithery registry manifest (`smithery.yaml`).
- **Live Camera Control & View Management (`manage_view` / `manage_session`)**: Added `zoom_window`, `zoom_center`, `preset` (3D isometric / orthographic view presets: `top`, `bottom`, `front`, `iso_sw`, `iso_se`, etc.), `style` (visual styles: `wireframe`, `conceptual`, `realistic`, `shaded`), and full shorthand support (`ze`, `zw`, `zc`, `preset|top`, `style|realistic`).
- **Human-in-the-Loop Interactive Prompts (`prompt_user`)**: Added interactive prompting with CAD crosshairs (`point` via `Utility.GetPoint`), entity picking on screen (`entity` via `Utility.GetEntity`), distance measuring (`distance` via `Utility.GetDistance`), and text input with graceful user cancellation handling.
- **Standalone Vector PDF Plotting (`export_data(format="pdf")`)**: Added direct vector PDF 1.4 document plotting supporting standard paper sizes (`A4`, `A3`, `A2`, `A1`, `A0`), frame stamps, and line styles without requiring external heavy C libraries.
- **BIM Semantic Metadata & XDATA (`set_metadata`, `get_metadata`)**: Added ability to attach and query structured BIM properties (fire rating, thermal U-values, cost codes, manufacturers) to any CAD entity handle using native AutoCAD XDATA and DXF extended dictionaries.
- **External References & Raster Images (`manage_xrefs`)**: Added unified management for DWG external references (`attach_dwg`, `reload`, `detach`) and raster images/orthophotos (`attach_raster`).
- **ConTech Bridge to `CE3X-MCP-SERVER` (`export_ce3x_envelope`)**: Added automatic building thermal envelope extraction with normal-vector orientation calculation (N, S, E, W, etc.), window-to-wall mapping, and CTE DB-HE structured JSON payload generation ready for direct energy certification in CE3X.
- **Standardized Layer Templates (AECO, AIA, MEP)**: Added `template` action to `manage_layers` (`template|aeco`, `template|aia`, `template|mep`) to automatically provision professional CAD layer structures (colors, lineweights, architectural standards like CTE DB-HE/COAM, US AIA, and MEP systems) in a single command.
- **Headless DXF Engine (`ezdxf`)**: Added `EzdxfAdapter` implementing full `CADInterface` for autonomous creation, editing, and saving of DXF drawings on disk without requiring AutoCAD/ZWCAD or Windows COM. Includes automatic server fallback when no GUI CAD is running.
- **Area & Perimeter Computation (AECO)**: Added `area` action in `manage_entities` (`area|handles` or `area|layer|name`) supporting geometric polygon Shoelace calculation and native CAD properties for accurate architectural quantification.
- **Spatial Intelligence & Point-in-Polygon Inspection (`inspect_drawing`)**: Added spatial intelligence tool supporting global bounding box calculation, room schedules, ASCII minimaps directly in chat, and raycasting Point-in-Polygon queries ("what is at coordinates X,Y?").
- **Interactive Standalone HTML5 CAD Viewer (`show_drawing_viewer`)**: Added 1-click generation and browser launch of interactive vector CAD viewer with smooth pan/zoom, layer toggling, and room clicking inspector displaying calculated m² and BIM properties.
- **Smart Architectural Annotations & Dimensioning (`manage_annotations`)**: Added automated space labeling (`label_spaces`) placing centered text in room centroids with calculated m² and BIM tags, and automated dimensioning (`auto_dimension`) supporting overall building bounding boxes and polyline segment wall dimensions.
- **Automated Area Schedule Tables (`area_table`)**: Added `area_table` action in `manage_entities` (`area_table|x,y|layer|title`) to automatically measure closed boundaries and generate professional CAD summary tables of Usable Surface (Superficie Útil) with itemized breakdown and total summary rows.

### Fixed

- **FastMCP Import & `mcp 2.x` Compatibility**: Fixed `ModuleNotFoundError` in `src/mcp_tools/decorators.py` by importing `FastMCP` directly from `fastmcp` package instead of deprecated/removed `mcp.server.fastmcp`.
- **Security Test Isolation**: Fixed false negative in `tests/unit/test_security.py::TestPathTraversal::test_validate_export_path_blocks_traversal_attempts` by properly mocking `ConfigManager.output.allow_arbitrary_paths = False`.
- **Dictionary Key Duplication**: Removed duplicate `"Spline"` key in `src/web/api.py` entity type mapping.

---

## [0.2.1] - 2026-06-27

### Added

- **Table Entity Support**: Added support for drawing native table entities using the `table` command in `draw_entities` (shorthand alias `tab`).
- **Bypass path traversal restrictions**: Added `allow_arbitrary_paths` configuration parameter in `output` settings. This allows users to save drawings to any absolute path on their host system, bypassing standard path traversal protection if explicitly enabled.
- **Selection mapping for tables**: Registered `table` to map to `AcDbTable` in entity selections.

### Fixed

- **Type Checking Warning**: Fixed a type-checking error in `DrawMLeaderRequest` initialization where `text_height` could resolve to `Any | None` instead of a non-nullable `float`.

---

## [0.2.0] - 2026-03-14

### Security (CRITICAL)

- **Path Traversal Prevention**: Added `_validate_export_path()` to prevent directory traversal attacks in file export operations.
- **Command Injection Mitigation**: Added `_sanitize_command_input()` to sanitize CAD command inputs, preventing malicious command injection.
- **Thread-Safe Singletons**: Implemented double-checked locking pattern in `AdapterRegistry` and `ConfigManager` for thread-safe operation.
- **COM Initialization Safety**: Improved error handling in `connection_mixin.py` for COM initialization across threads.

### Added

- **Block attribute management**: `get_attrs` and `set_attrs` actions in `manage_blocks` — read and write attribute tag values on block references.
- **Modern packaging**: `pyproject.toml` with full project metadata, dev/docs dependency groups, `[tool.ruff]`, `[tool.mypy]`, `[tool.interrogate]`, and `[tool.pytest]` configuration.
- **MkDocs documentation site**: Material theme with auto-generated API reference via mkdocstrings.

### Changed

- **Unified tool architecture**: 55 specific CAD commands replaced by 7 unified dispatch tools using compact shorthand format (~85% token reduction).
  - `manage_session` (11 actions), `draw_entities` (10 types), `manage_blocks` (6 actions), `manage_layers` (9 actions), `manage_files` (5 actions), `manage_entities` (10 actions), `export_data` (4 combinations).
- **Auto-named exports**: Excel export defaults to `[drawing_name]_data.xlsx` instead of `drawing_data.xlsx`.
- **Excel improvements**: autofilter enabled on all sheets (Entities, Layers, Blocks); `limit=0` ensures full export.
- **Dashboard refactor**: removed background refresher thread; export and refresh run directly on MCP thread; centralized configuration in `config.json` (port 8888).
- **Test suite**: expanded from 62 to 171 tests.

### Performance

- **O(n*m) → O(1) Optimization**: Optimized entity lookup in `set_entities_color_bylayer()` using `HandleToObject()` API.
  - Replaced inefficient nested loop iteration with direct handle-to-object lookups.
  - Expected 60%+ improvement on drawings with 10,000+ entities.

### Bug Fixes

- **Missing Return Statement**: Fixed `_paste()` function missing return value in `entities.py`.
- **Hardcoded Version**: Updated `web/api.py` to import version from `__version__.py` instead of hardcoding.
- **JSON Error Handling**: Added JSON error handling in `_set_color_bylayer()` with proper error messages.
- **Coordinate Validation**: Improved coordinate parsing with better error messages in paste operations.

---

## [0.1.3] - 2026-02-12

### Changed - Mixin Architecture Refactor

Major refactoring of the adapter layer for better maintainability.

#### Architecture

- **Mixin-based adapter**: `autocad_adapter.py` reduced from 3,198 to 99 lines.
- **11 specialized mixins**: Each mixin handles a specific responsibility (Utility, Connection, Drawing, Layer, File, View, Selection, Entity, Manipulation, Block, Export).
- **AdapterRegistry**: Encapsulated global state in singleton class.
- **Removed NLP**: Natural language processor removed (use direct tool calls).

#### Bug Fixes

- Fixed `@staticmethod` error in `validate_lineweight`.

#### Improvements

- **Refactored `DrawingMixin`**: Reduces boilerplate code in drawing methods using `_finalize_entity` helper.
- **Simplified `draw_mleader`**: Extracted complex fallback logic to improve readability.
- **Documentation**: Simplified `README.md` and updated documentation structure.

---

## [0.1.2] - 2025-12-09

### Added

- **Block creation**: `create_block` tool (from handles or selection).
- Core methods: `create_block_from_entities()`, `create_block_from_selection()`.
- 7 new tests (42 total).

### Changed

- Direct instantiation: `AutoCADAdapter(cad_type)` replaces factory.
- Context managers: `com_session()`, `SelectionSetManager`.
- Performance: `PickfirstSelectionSet` for fast entity access.

---

## [0.1.1] - 2025-11-22

### Added - Batch Operations

**13 batch operation tools** (legacy tools replaced by current unified architecture in 0.2.0):
- Drawing: `draw_lines`, `draw_circles`, `draw_arcs`, `draw_rectangles`, `draw_polylines`, `draw_texts`, `add_dimensions`.
- Layers: `rename_layers`, `delete_layers`, `turn_layers_on`, `turn_layers_off`.
- Entities: `change_entities_colors`, `change_entities_layers`.

---

## [0.1.0] - 2025-11-12

### Initial Release

- **Multi-CAD support**: AutoCAD, ZWCAD, GstarCAD, BricsCAD.
- **FastMCP 2.0** server with MCP tools.
- **Universal adapter** via COM API.
- **Excel export** with locale support.
- **Type safety**: 100% type hints.
- **Testing**: Comprehensive test suite.
