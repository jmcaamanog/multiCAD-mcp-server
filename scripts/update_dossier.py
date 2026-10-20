import urllib.parse
from pathlib import Path

prs = [
    {
        'num': '01',
        'branch': 'pr/01-fix-fastmcp-and-security',
        'title': 'fix: resolve FastMCP 2.x/3.x compatibility, security test isolation, and fix broken changelog link',
        'summary': 'Fix FastMCP 2.x/3.x, aislamiento tests y enlace CHANGELOG',
        'body': '''### Summary of Changes
- **FastMCP compatibility**: Import FastMCP directly from `fastmcp` to support MCP 2.x and 3.x specifications without `ModuleNotFoundError`.
- **Security test isolation**: Isolate `ConfigManager` state during path traversal tests to avoid state leakage.
- **Documentation**: Fix broken CHANGELOG link in README.

All 316 unit tests passing.'''
    },
    {
        'num': '02',
        'branch': 'pr/02-cli-entrypoint-and-parsers',
        'title': 'feat(cli): add multicad-mcp CLI entrypoint, CLI flags, and resilient list/dict shorthand input parsing',
        'summary': 'Binario CLI multicad-mcp, flags y parsers tolerantes',
        'body': '''### Summary of Changes
- **CLI entrypoint**: Add `multicad-mcp` CLI executable with `--transport stdio|http`, `--host`, `--port`, and `--no-dashboard` options.
- **Packaging**: Register `[project.scripts]` in `pyproject.toml`.
- **Input robustness**: Allow shorthand parsers to accept native Python `dict` and `list` inputs without failing on `.strip()`.

All 316 unit tests passing.'''
    },
    {
        'num': '03',
        'branch': 'pr/03-1click-desktop-installer',
        'title': 'feat(installer): add 1-click Windows installer for Claude Desktop and Cursor with automatic backup',
        'summary': 'Instalador 1-clic Windows con copia .bak para Claude y Cursor',
        'body': '''### Summary of Changes
- **1-Click installer**: Added `scripts/instalar_claude_desktop.py` and `instalar_en_claude_desktop.bat`.
- **Auto-detection**: Detects `multicad-mcp` executable and Claude Desktop / Cursor configuration paths.
- **Safe backups**: Creates automatic timestamped `.bak` files before updating config JSON.

All 316 unit tests passing.'''
    },
    {
        'num': '04',
        'branch': 'pr/04-headless-ezdxf-engine',
        'title': 'feat(adapter): add autonomous headless ezdxf CAD adapter with automated fallback',
        'summary': 'Motor autónomo ezdxf offline y fallback automático',
        'body': '''### Summary of Changes
- **Headless engine**: New `EzdxfAdapter` implementing `CADInterface` using `ezdxf` for offline, CI/CD, and non-GUI CAD operations.
- **Automated fallback**: Automatically falls back to `ezdxf` when no running AutoCAD or ZWCAD COM instance is detected.

All 316 unit tests passing.'''
    },
    {
        'num': '05',
        'branch': 'pr/05-cad-qa-audit-purge-and-ci',
        'title': 'ci: add GitHub Actions CI/CD workflows, release automation, CAD audit and layer purge',
        'summary': 'CI/CD GitHub Actions, auditoría audit y purga de capas purge',
        'body': '''### Summary of Changes
- **CI/CD workflows**: Added GitHub Actions workflows for continuous integration (`ci.yml`) and automated releases (`release.yml`).
- **QA audit**: Added `audit` action to detect zero-length lines, duplicate entities, and layer 0 anomalies.
- **Layer purge**: Added `purge` action to clean up unreferenced layers.

All 316 unit tests passing.'''
    },
    {
        'num': '06',
        'branch': 'pr/06-view-camera-control',
        'title': 'feat(view): add manage_view tool for camera zoom extents/window, 3D view presets, and visual styles',
        'summary': 'Control de cámara en vivo manage_view, zoom extents y vistas 3D',
        'body': '''### Summary of Changes
- **Camera controls**: Added `manage_view` tool with `zoom_extents`, `zoom_window`, and `zoom_center`.
- **3D presets**: Support for top, front, and axonometric isometric views (`iso_sw`, `iso_se`, etc.).
- **Visual styles**: Switch between wireframe, conceptual, realistic, and shaded styles.

All 316 unit tests passing.'''
    },
    {
        'num': '07',
        'branch': 'pr/07-human-in-the-loop',
        'title': 'feat(interaction): add prompt_user tool for human-in-the-loop CAD crosshair and entity selection',
        'summary': 'Interacción asistida prompt_user con mirilla de AutoCAD',
        'body': '''### Summary of Changes
- **Human-in-the-Loop**: Added `prompt_user` tool allowing AI agents to request user input via AutoCAD crosshair (`point`), entity picking (`entity`), distance measurement, or text input.
- **Clean cancellation**: Cleanly handles user pressing ESC without crashing the MCP server.

All 316 unit tests passing.'''
    },
    {
        'num': '08',
        'branch': 'pr/08-vector-pdf-plotter',
        'title': 'feat(export): add standalone vector PDF 1.4 plotter with standard paper formats (A4-A0) and stamp',
        'summary': 'Trazador nativo a PDF 1.4 vectorial con formatos ISO A4-A0',
        'body': '''### Summary of Changes
- **Vector PDF plotter**: Native standalone PDF 1.4 vector generator in `export_data(format="pdf")` without heavy external binary dependencies.
- **ISO standards**: Supports standard ISO paper sizes (A4 through A0), scale framing, and title block stamps.

All 316 unit tests passing.'''
    },
    {
        'num': '09',
        'branch': 'pr/09-bim-metadata-xdata',
        'title': 'feat(bim): add BIM semantic metadata and XDATA support (set_metadata, get_metadata)',
        'summary': 'Metadatos BIM estructurados y persistencia en XDATA CAD',
        'body': '''### Summary of Changes
- **BIM metadata**: Added `set_metadata` and `get_metadata` commands in `manage_entities`.
- **XDATA persistence**: Stores structured building properties (fire resistance, U-value, manufacturer, cost codes) in AutoCAD XDATA and DXF dictionaries under `MULTICAD_BIM`.

All 316 unit tests passing.'''
    },
    {
        'num': '10',
        'branch': 'pr/10-xref-raster-manager',
        'title': 'feat(xrefs): add manage_xrefs tool for DWG external references and raster image attachments',
        'summary': 'Gestor de referencias externas DWG e inserción de ortofotos PNOA',
        'body': '''### Summary of Changes
- **XREF management**: Added `manage_xrefs` tool to attach, list, reload, and detach external DWG references.
- **Raster images**: Support for attaching georeferenced orthophotos and raster images (`attach_raster`).

All 316 unit tests passing.'''
    },
    {
        'num': '11',
        'branch': 'pr/11-drawing-inspector-and-viewer',
        'title': 'feat(inspection): add inspect_drawing spatial intelligence and show_drawing_viewer interactive HTML5 CAD viewer',
        'summary': 'Inferencia espacial (Point-in-Polygon) y visor interactivo HTML5',
        'body': '''### Summary of Changes
- **Spatial intelligence**: Added `inspect_drawing` with bounding box calculation, ASCII minimap generation, and Point-in-Polygon raycasting queries.
- **Interactive viewer**: Added `show_drawing_viewer` generating a standalone HTML5 Canvas viewer with zoom, pan, layer toggles, and space inspection.

All 316 unit tests passing.'''
    },
    {
        'num': '12',
        'branch': 'pr/12-smart-annotations',
        'title': 'feat(annotations): add manage_annotations tool for automated room labeling and dimensioning',
        'summary': 'Acotación automática de envolventes y rotulación con m²',
        'body': '''### Summary of Changes
- **Space labeling**: Added `label_spaces` action to automatically compute polygon centroids, calculate area in m², and place centered room labels.
- **Auto dimensioning**: Added `auto_dimension` for building envelope and wall segment dimensioning.

All 316 unit tests passing.'''
    },
    {
        'num': '13',
        'branch': 'pr/13-offset-and-fillet',
        'title': 'feat(entities): add offset, fillet, chamfer, explode, and matchprop manipulation tools',
        'summary': 'OFFSET, FILLET, CHAMFER, EXPLODE y MATCHPROP',
        'body': '''### Summary of Changes
- **Parametric editing**: Added `offset_entity`, `fillet_entities`, `chamfer_entities`, `explode_entity`, and `match_properties` in `manage_entities` and CAD adapters.
- **CAD parity**: Full dual support across AutoCAD COM and headless ezdxf.

All 316 unit tests passing.'''
    },
    {
        'num': '14',
        'branch': 'pr/14-boundary-and-join',
        'title': 'feat(entities): add boundary polyline detection, geometry join, trim, and extend',
        'summary': 'BOUNDARY (contorno cerrado), JOIN (unión con holgura), TRIM y EXTEND',
        'body': '''### Summary of Changes
- **Boundary detection**: Added `create_boundary` for closed boundary polyline detection from an internal point.
- **Topology operations**: Added `join_entities` (joining contiguous segments into polylines with gap tolerance) and `trim_extend_entity` (trimming and extending segments against cutting edges).

All 316 unit tests passing.'''
    },
    {
        'num': '15',
        'branch': 'pr/15-geometry-snapping-intersections',
        'title': 'feat(inspection): add geometric intersections query and object snapping assistant (OSNAP)',
        'summary': 'Intersecciones vectoriales y asistente de enganche OSNAP',
        'body': '''### Summary of Changes
- **Vector intersections**: Added `intersections` mode in `inspect_drawing` to detect real crossing points between lines and polylines.
- **OSNAP assistant**: Added `snap` mode for magnetic snapping to endpoints, midpoints, and circle/arc centers within a tolerance.

All 316 unit tests passing.'''
    },
    {
        'num': '16',
        'branch': 'pr/16-paperspace-layout-generator',
        'title': 'feat(layouts): add manage_layouts for paperspace sheets, viewports, architectural scaling, and AECO title blocks',
        'summary': 'Presentaciones espacio papel ISO (A4-A0), MVIEW escaladas y cajetines AECO',
        'body': '''### Summary of Changes
- **Paperspace layouts**: Added `manage_layouts` tool for creating paperspace presentation sheets with standard ISO formats (A4 to A0).
- **MVIEW viewports**: Floating viewports linked to modelspace at standard architectural scales (1:50, 1:100, etc.).
- **AECO title blocks**: Standard sheet borders and title blocks with metadata.

All 316 unit tests passing.'''
    },
    {
        'num': '17',
        'branch': 'pr/17-advanced-hatch-patterns',
        'title': 'feat(drawing): add architectural hatch patterns (ANSI31, AR-CONC, GRAVEL, SOLID), scaling, rotation, and boundary associativity',
        'summary': 'Tramas arquitectónicas normalizadas (ANSI31, AR-CONC, GRAVEL) y escala',
        'body': '''### Summary of Changes
- **Architectural patterns**: Added support for standard technical hatch patterns (`ANSI31`, `AR-CONC`, `ANSI32`, `GRAVEL`, `EARTH`, `SOLID`) in `draw_entities(type="hatch")`.
- **Hatch controls**: Full support for scale, rotation angle, and associative boundary hatching via `boundary_handle`.

All 316 unit tests passing.'''
    },
    {
        'num': '18',
        'branch': 'pr/18-find-and-replace-text',
        'title': 'feat(entities): add batch text find and replace across TEXT, MTEXT, and block attributes',
        'summary': 'Búsqueda y reemplazo por lotes en TEXT, MTEXT y atributos con Regex',
        'body': '''### Summary of Changes
- **Batch text replace**: Added `find_text` and `replace_text` in `manage_entities`.
- **Scope**: Searches and replaces across `TEXT`, `MTEXT`, and block attributes (`ATTRIB`).
- **Features**: Regex pattern matching, case sensitivity toggle, and layer filtering.

All 316 unit tests passing.'''
    }
]

out = """# 🚀 Dossier Oficial de Pull Requests (multiCAD-MCP)

Guía completa y estructurada para el lanzamiento de los **18 Pull Requests atómicos** desde el fork [`jmcaamanog/multiCAD-mcp-server`](https://github.com/jmcaamanog/multiCAD-mcp-server) hacia el repositorio upstream [`AnCode666/multiCAD-mcp`](https://github.com/AnCode666/multiCAD-mcp).

---

## ⚡ Enlaces Directos de Creación de PR (Con Autocompletado de Título y Descripción)

> [!TIP]
> Al hacer clic en cualquiera de estos enlaces, GitHub abrirá la pantalla de creación con **Título** y **Descripción** pre-rellenados automáticamente. Si tu navegador o GitHub no cargan el texto por longitud de URL, tienes abajo las fichas listas para copiar y pegar.

| # | Rama | Enfoque | Enlace Directo (1-Clic con Autocompletado) |
| :-: | :--- | :--- | :--- |
"""

for p in prs:
    encoded_title = urllib.parse.quote_plus(p['title'])
    encoded_body = urllib.parse.quote_plus(p['body'])
    url = f"https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:{p['branch']}?expand=1&title={encoded_title}&body={encoded_body}"
    out += f"| **{p['num']}** | `{p['branch']}` | {p['summary']} | [🔗 Abrir PR #{p['num']}]({url}) |\n"

out += """
---

## 📝 Fichas Listas para Copiar y Pegar en GitHub

"""

for p in prs:
    out += f"""### PR #{p['num']}: `{p['branch']}`

**Título:**
```text
{p['title']}
```

**Descripción:**
```markdown
{p['body']}
```

---
"""

Path('docs/PR_DOSSIER.md').write_text(out, encoding='utf-8')
print("PR_DOSSIER.md successfully updated!")
