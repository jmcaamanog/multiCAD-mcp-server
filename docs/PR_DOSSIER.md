# 🚀 Dossier Oficial de Pull Requests (multiCAD-MCP)

Guía completa y estructurada para el lanzamiento de los **18 Pull Requests atómicos** desde el fork [`jmcaamanog/multiCAD-mcp-server`](https://github.com/jmcaamanog/multiCAD-mcp-server) hacia el repositorio upstream [`AnCode666/multiCAD-mcp`](https://github.com/AnCode666/multiCAD-mcp).

---

## ⚡ Enlaces Directos de Creación de PR (Con Autocompletado de Título y Descripción)

> [!TIP]
> Al hacer clic en cualquiera de estos enlaces, GitHub abrirá la pantalla de creación con **Título** y **Descripción** pre-rellenados automáticamente. Si tu navegador o GitHub no cargan el texto por longitud de URL, tienes abajo las fichas listas para copiar y pegar.

| # | Rama | Enfoque | Enlace Directo (1-Clic con Autocompletado) |
| :-: | :--- | :--- | :--- |
| **01** | `pr/01-fix-fastmcp-and-security` | Fix FastMCP 2.x/3.x, aislamiento tests y enlace CHANGELOG | [🔗 Abrir PR #01](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/01-fix-fastmcp-and-security?expand=1&title=fix%3A+resolve+FastMCP+2.x%2F3.x+compatibility%2C+security+test+isolation%2C+and+fix+broken+changelog+link&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AFastMCP+compatibility%2A%2A%3A+Import+FastMCP+directly+from+%60fastmcp%60+to+support+MCP+2.x+and+3.x+specifications+without+%60ModuleNotFoundError%60.%0A-+%2A%2ASecurity+test+isolation%2A%2A%3A+Isolate+%60ConfigManager%60+state+during+path+traversal+tests+to+avoid+state+leakage.%0A-+%2A%2ADocumentation%2A%2A%3A+Fix+broken+CHANGELOG+link+in+README.%0A%0AAll+316+unit+tests+passing.) |
| **02** | `pr/02-cli-entrypoint-and-parsers` | Binario CLI multicad-mcp, flags y parsers tolerantes | [🔗 Abrir PR #02](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/02-cli-entrypoint-and-parsers?expand=1&title=feat%28cli%29%3A+add+multicad-mcp+CLI+entrypoint%2C+CLI+flags%2C+and+resilient+list%2Fdict+shorthand+input+parsing&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ACLI+entrypoint%2A%2A%3A+Add+%60multicad-mcp%60+CLI+executable+with+%60--transport+stdio%7Chttp%60%2C+%60--host%60%2C+%60--port%60%2C+and+%60--no-dashboard%60+options.%0A-+%2A%2APackaging%2A%2A%3A+Register+%60%5Bproject.scripts%5D%60+in+%60pyproject.toml%60.%0A-+%2A%2AInput+robustness%2A%2A%3A+Allow+shorthand+parsers+to+accept+native+Python+%60dict%60+and+%60list%60+inputs+without+failing+on+%60.strip%28%29%60.%0A%0AAll+316+unit+tests+passing.) |
| **03** | `pr/03-1click-desktop-installer` | Instalador 1-clic Windows con copia .bak para Claude y Cursor | [🔗 Abrir PR #03](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/03-1click-desktop-installer?expand=1&title=feat%28installer%29%3A+add+1-click+Windows+installer+for+Claude+Desktop+and+Cursor+with+automatic+backup&body=%23%23%23+Summary+of+Changes%0A-+%2A%2A1-Click+installer%2A%2A%3A+Added+%60scripts%2Finstalar_claude_desktop.py%60+and+%60instalar_en_claude_desktop.bat%60.%0A-+%2A%2AAuto-detection%2A%2A%3A+Detects+%60multicad-mcp%60+executable+and+Claude+Desktop+%2F+Cursor+configuration+paths.%0A-+%2A%2ASafe+backups%2A%2A%3A+Creates+automatic+timestamped+%60.bak%60+files+before+updating+config+JSON.%0A%0AAll+316+unit+tests+passing.) |
| **04** | `pr/04-headless-ezdxf-engine` | Motor autónomo ezdxf offline y fallback automático | [🔗 Abrir PR #04](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/04-headless-ezdxf-engine?expand=1&title=feat%28adapter%29%3A+add+autonomous+headless+ezdxf+CAD+adapter+with+automated+fallback&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AHeadless+engine%2A%2A%3A+New+%60EzdxfAdapter%60+implementing+%60CADInterface%60+using+%60ezdxf%60+for+offline%2C+CI%2FCD%2C+and+non-GUI+CAD+operations.%0A-+%2A%2AAutomated+fallback%2A%2A%3A+Automatically+falls+back+to+%60ezdxf%60+when+no+running+AutoCAD+or+ZWCAD+COM+instance+is+detected.%0A%0AAll+316+unit+tests+passing.) |
| **05** | `pr/05-cad-qa-audit-purge-and-ci` | CI/CD GitHub Actions, auditoría audit y purga de capas purge | [🔗 Abrir PR #05](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/05-cad-qa-audit-purge-and-ci?expand=1&title=ci%3A+add+GitHub+Actions+CI%2FCD+workflows%2C+release+automation%2C+CAD+audit+and+layer+purge&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ACI%2FCD+workflows%2A%2A%3A+Added+GitHub+Actions+workflows+for+continuous+integration+%28%60ci.yml%60%29+and+automated+releases+%28%60release.yml%60%29.%0A-+%2A%2AQA+audit%2A%2A%3A+Added+%60audit%60+action+to+detect+zero-length+lines%2C+duplicate+entities%2C+and+layer+0+anomalies.%0A-+%2A%2ALayer+purge%2A%2A%3A+Added+%60purge%60+action+to+clean+up+unreferenced+layers.%0A%0AAll+316+unit+tests+passing.) |
| **06** | `pr/06-view-camera-control` | Control de cámara en vivo manage_view, zoom extents y vistas 3D | [🔗 Abrir PR #06](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/06-view-camera-control?expand=1&title=feat%28view%29%3A+add+manage_view+tool+for+camera+zoom+extents%2Fwindow%2C+3D+view+presets%2C+and+visual+styles&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ACamera+controls%2A%2A%3A+Added+%60manage_view%60+tool+with+%60zoom_extents%60%2C+%60zoom_window%60%2C+and+%60zoom_center%60.%0A-+%2A%2A3D+presets%2A%2A%3A+Support+for+top%2C+front%2C+and+axonometric+isometric+views+%28%60iso_sw%60%2C+%60iso_se%60%2C+etc.%29.%0A-+%2A%2AVisual+styles%2A%2A%3A+Switch+between+wireframe%2C+conceptual%2C+realistic%2C+and+shaded+styles.%0A%0AAll+316+unit+tests+passing.) |
| **07** | `pr/07-human-in-the-loop` | Interacción asistida prompt_user con mirilla de AutoCAD | [🔗 Abrir PR #07](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/07-human-in-the-loop?expand=1&title=feat%28interaction%29%3A+add+prompt_user+tool+for+human-in-the-loop+CAD+crosshair+and+entity+selection&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AHuman-in-the-Loop%2A%2A%3A+Added+%60prompt_user%60+tool+allowing+AI+agents+to+request+user+input+via+AutoCAD+crosshair+%28%60point%60%29%2C+entity+picking+%28%60entity%60%29%2C+distance+measurement%2C+or+text+input.%0A-+%2A%2AClean+cancellation%2A%2A%3A+Cleanly+handles+user+pressing+ESC+without+crashing+the+MCP+server.%0A%0AAll+316+unit+tests+passing.) |
| **08** | `pr/08-vector-pdf-plotter` | Trazador nativo a PDF 1.4 vectorial con formatos ISO A4-A0 | [🔗 Abrir PR #08](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/08-vector-pdf-plotter?expand=1&title=feat%28export%29%3A+add+standalone+vector+PDF+1.4+plotter+with+standard+paper+formats+%28A4-A0%29+and+stamp&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AVector+PDF+plotter%2A%2A%3A+Native+standalone+PDF+1.4+vector+generator+in+%60export_data%28format%3D%22pdf%22%29%60+without+heavy+external+binary+dependencies.%0A-+%2A%2AISO+standards%2A%2A%3A+Supports+standard+ISO+paper+sizes+%28A4+through+A0%29%2C+scale+framing%2C+and+title+block+stamps.%0A%0AAll+316+unit+tests+passing.) |
| **09** | `pr/09-bim-metadata-xdata` | Metadatos BIM estructurados y persistencia en XDATA CAD | [🔗 Abrir PR #09](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/09-bim-metadata-xdata?expand=1&title=feat%28bim%29%3A+add+BIM+semantic+metadata+and+XDATA+support+%28set_metadata%2C+get_metadata%29&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ABIM+metadata%2A%2A%3A+Added+%60set_metadata%60+and+%60get_metadata%60+commands+in+%60manage_entities%60.%0A-+%2A%2AXDATA+persistence%2A%2A%3A+Stores+structured+building+properties+%28fire+resistance%2C+U-value%2C+manufacturer%2C+cost+codes%29+in+AutoCAD+XDATA+and+DXF+dictionaries+under+%60MULTICAD_BIM%60.%0A%0AAll+316+unit+tests+passing.) |
| **10** | `pr/10-xref-raster-manager` | Gestor de referencias externas DWG e inserción de ortofotos PNOA | [🔗 Abrir PR #10](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/10-xref-raster-manager?expand=1&title=feat%28xrefs%29%3A+add+manage_xrefs+tool+for+DWG+external+references+and+raster+image+attachments&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AXREF+management%2A%2A%3A+Added+%60manage_xrefs%60+tool+to+attach%2C+list%2C+reload%2C+and+detach+external+DWG+references.%0A-+%2A%2ARaster+images%2A%2A%3A+Support+for+attaching+georeferenced+orthophotos+and+raster+images+%28%60attach_raster%60%29.%0A%0AAll+316+unit+tests+passing.) |
| **11** | `pr/11-drawing-inspector-and-viewer` | Inferencia espacial (Point-in-Polygon) y visor interactivo HTML5 | [🔗 Abrir PR #11](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/11-drawing-inspector-and-viewer?expand=1&title=feat%28inspection%29%3A+add+inspect_drawing+spatial+intelligence+and+show_drawing_viewer+interactive+HTML5+CAD+viewer&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ASpatial+intelligence%2A%2A%3A+Added+%60inspect_drawing%60+with+bounding+box+calculation%2C+ASCII+minimap+generation%2C+and+Point-in-Polygon+raycasting+queries.%0A-+%2A%2AInteractive+viewer%2A%2A%3A+Added+%60show_drawing_viewer%60+generating+a+standalone+HTML5+Canvas+viewer+with+zoom%2C+pan%2C+layer+toggles%2C+and+space+inspection.%0A%0AAll+316+unit+tests+passing.) |
| **12** | `pr/12-smart-annotations` | Acotación automática de envolventes y rotulación con m² | [🔗 Abrir PR #12](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/12-smart-annotations?expand=1&title=feat%28annotations%29%3A+add+manage_annotations+tool+for+automated+room+labeling+and+dimensioning&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ASpace+labeling%2A%2A%3A+Added+%60label_spaces%60+action+to+automatically+compute+polygon+centroids%2C+calculate+area+in+m%C2%B2%2C+and+place+centered+room+labels.%0A-+%2A%2AAuto+dimensioning%2A%2A%3A+Added+%60auto_dimension%60+for+building+envelope+and+wall+segment+dimensioning.%0A%0AAll+316+unit+tests+passing.) |
| **13** | `pr/13-offset-and-fillet` | OFFSET, FILLET, CHAMFER, EXPLODE y MATCHPROP | [🔗 Abrir PR #13](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/13-offset-and-fillet?expand=1&title=feat%28entities%29%3A+add+offset%2C+fillet%2C+chamfer%2C+explode%2C+and+matchprop+manipulation+tools&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AParametric+editing%2A%2A%3A+Added+%60offset_entity%60%2C+%60fillet_entities%60%2C+%60chamfer_entities%60%2C+%60explode_entity%60%2C+and+%60match_properties%60+in+%60manage_entities%60+and+CAD+adapters.%0A-+%2A%2ACAD+parity%2A%2A%3A+Full+dual+support+across+AutoCAD+COM+and+headless+ezdxf.%0A%0AAll+316+unit+tests+passing.) |
| **14** | `pr/14-boundary-and-join` | BOUNDARY (contorno cerrado), JOIN (unión con holgura), TRIM y EXTEND | [🔗 Abrir PR #14](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/14-boundary-and-join?expand=1&title=feat%28entities%29%3A+add+boundary+polyline+detection%2C+geometry+join%2C+trim%2C+and+extend&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ABoundary+detection%2A%2A%3A+Added+%60create_boundary%60+for+closed+boundary+polyline+detection+from+an+internal+point.%0A-+%2A%2ATopology+operations%2A%2A%3A+Added+%60join_entities%60+%28joining+contiguous+segments+into+polylines+with+gap+tolerance%29+and+%60trim_extend_entity%60+%28trimming+and+extending+segments+against+cutting+edges%29.%0A%0AAll+316+unit+tests+passing.) |
| **15** | `pr/15-geometry-snapping-intersections` | Intersecciones vectoriales y asistente de enganche OSNAP | [🔗 Abrir PR #15](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/15-geometry-snapping-intersections?expand=1&title=feat%28inspection%29%3A+add+geometric+intersections+query+and+object+snapping+assistant+%28OSNAP%29&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AVector+intersections%2A%2A%3A+Added+%60intersections%60+mode+in+%60inspect_drawing%60+to+detect+real+crossing+points+between+lines+and+polylines.%0A-+%2A%2AOSNAP+assistant%2A%2A%3A+Added+%60snap%60+mode+for+magnetic+snapping+to+endpoints%2C+midpoints%2C+and+circle%2Farc+centers+within+a+tolerance.%0A%0AAll+316+unit+tests+passing.) |
| **16** | `pr/16-paperspace-layout-generator` | Presentaciones espacio papel ISO (A4-A0), MVIEW escaladas y cajetines AECO | [🔗 Abrir PR #16](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/16-paperspace-layout-generator?expand=1&title=feat%28layouts%29%3A+add+manage_layouts+for+paperspace+sheets%2C+viewports%2C+architectural+scaling%2C+and+AECO+title+blocks&body=%23%23%23+Summary+of+Changes%0A-+%2A%2APaperspace+layouts%2A%2A%3A+Added+%60manage_layouts%60+tool+for+creating+paperspace+presentation+sheets+with+standard+ISO+formats+%28A4+to+A0%29.%0A-+%2A%2AMVIEW+viewports%2A%2A%3A+Floating+viewports+linked+to+modelspace+at+standard+architectural+scales+%281%3A50%2C+1%3A100%2C+etc.%29.%0A-+%2A%2AAECO+title+blocks%2A%2A%3A+Standard+sheet+borders+and+title+blocks+with+metadata.%0A%0AAll+316+unit+tests+passing.) |
| **17** | `pr/17-advanced-hatch-patterns` | Tramas arquitectónicas normalizadas (ANSI31, AR-CONC, GRAVEL) y escala | [🔗 Abrir PR #17](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/17-advanced-hatch-patterns?expand=1&title=feat%28drawing%29%3A+add+architectural+hatch+patterns+%28ANSI31%2C+AR-CONC%2C+GRAVEL%2C+SOLID%29%2C+scaling%2C+rotation%2C+and+boundary+associativity&body=%23%23%23+Summary+of+Changes%0A-+%2A%2AArchitectural+patterns%2A%2A%3A+Added+support+for+standard+technical+hatch+patterns+%28%60ANSI31%60%2C+%60AR-CONC%60%2C+%60ANSI32%60%2C+%60GRAVEL%60%2C+%60EARTH%60%2C+%60SOLID%60%29+in+%60draw_entities%28type%3D%22hatch%22%29%60.%0A-+%2A%2AHatch+controls%2A%2A%3A+Full+support+for+scale%2C+rotation+angle%2C+and+associative+boundary+hatching+via+%60boundary_handle%60.%0A%0AAll+316+unit+tests+passing.) |
| **18** | `pr/18-find-and-replace-text` | Búsqueda y reemplazo por lotes en TEXT, MTEXT y atributos con Regex | [🔗 Abrir PR #18](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp-server:pr/18-find-and-replace-text?expand=1&title=feat%28entities%29%3A+add+batch+text+find+and+replace+across+TEXT%2C+MTEXT%2C+and+block+attributes&body=%23%23%23+Summary+of+Changes%0A-+%2A%2ABatch+text+replace%2A%2A%3A+Added+%60find_text%60+and+%60replace_text%60+in+%60manage_entities%60.%0A-+%2A%2AScope%2A%2A%3A+Searches+and+replaces+across+%60TEXT%60%2C+%60MTEXT%60%2C+and+block+attributes+%28%60ATTRIB%60%29.%0A-+%2A%2AFeatures%2A%2A%3A+Regex+pattern+matching%2C+case+sensitivity+toggle%2C+and+layer+filtering.%0A%0AAll+316+unit+tests+passing.) |

---

## 📝 Fichas Listas para Copiar y Pegar en GitHub

### PR #01: `pr/01-fix-fastmcp-and-security`

**Título:**
```text
fix: resolve FastMCP 2.x/3.x compatibility, security test isolation, and fix broken changelog link
```

**Descripción:**
```markdown
### Summary of Changes
- **FastMCP compatibility**: Import FastMCP directly from `fastmcp` to support MCP 2.x and 3.x specifications without `ModuleNotFoundError`.
- **Security test isolation**: Isolate `ConfigManager` state during path traversal tests to avoid state leakage.
- **Documentation**: Fix broken CHANGELOG link in README.

All 316 unit tests passing.
```

---
### PR #02: `pr/02-cli-entrypoint-and-parsers`

**Título:**
```text
feat(cli): add multicad-mcp CLI entrypoint, CLI flags, and resilient list/dict shorthand input parsing
```

**Descripción:**
```markdown
### Summary of Changes
- **CLI entrypoint**: Add `multicad-mcp` CLI executable with `--transport stdio|http`, `--host`, `--port`, and `--no-dashboard` options.
- **Packaging**: Register `[project.scripts]` in `pyproject.toml`.
- **Input robustness**: Allow shorthand parsers to accept native Python `dict` and `list` inputs without failing on `.strip()`.

All 316 unit tests passing.
```

---
### PR #03: `pr/03-1click-desktop-installer`

**Título:**
```text
feat(installer): add 1-click Windows installer for Claude Desktop and Cursor with automatic backup
```

**Descripción:**
```markdown
### Summary of Changes
- **1-Click installer**: Added `scripts/instalar_claude_desktop.py` and `instalar_en_claude_desktop.bat`.
- **Auto-detection**: Detects `multicad-mcp` executable and Claude Desktop / Cursor configuration paths.
- **Safe backups**: Creates automatic timestamped `.bak` files before updating config JSON.

All 316 unit tests passing.
```

---
### PR #04: `pr/04-headless-ezdxf-engine`

**Título:**
```text
feat(adapter): add autonomous headless ezdxf CAD adapter with automated fallback
```

**Descripción:**
```markdown
### Summary of Changes
- **Headless engine**: New `EzdxfAdapter` implementing `CADInterface` using `ezdxf` for offline, CI/CD, and non-GUI CAD operations.
- **Automated fallback**: Automatically falls back to `ezdxf` when no running AutoCAD or ZWCAD COM instance is detected.

All 316 unit tests passing.
```

---
### PR #05: `pr/05-cad-qa-audit-purge-and-ci`

**Título:**
```text
ci: add GitHub Actions CI/CD workflows, release automation, CAD audit and layer purge
```

**Descripción:**
```markdown
### Summary of Changes
- **CI/CD workflows**: Added GitHub Actions workflows for continuous integration (`ci.yml`) and automated releases (`release.yml`).
- **QA audit**: Added `audit` action to detect zero-length lines, duplicate entities, and layer 0 anomalies.
- **Layer purge**: Added `purge` action to clean up unreferenced layers.

All 316 unit tests passing.
```

---
### PR #06: `pr/06-view-camera-control`

**Título:**
```text
feat(view): add manage_view tool for camera zoom extents/window, 3D view presets, and visual styles
```

**Descripción:**
```markdown
### Summary of Changes
- **Camera controls**: Added `manage_view` tool with `zoom_extents`, `zoom_window`, and `zoom_center`.
- **3D presets**: Support for top, front, and axonometric isometric views (`iso_sw`, `iso_se`, etc.).
- **Visual styles**: Switch between wireframe, conceptual, realistic, and shaded styles.

All 316 unit tests passing.
```

---
### PR #07: `pr/07-human-in-the-loop`

**Título:**
```text
feat(interaction): add prompt_user tool for human-in-the-loop CAD crosshair and entity selection
```

**Descripción:**
```markdown
### Summary of Changes
- **Human-in-the-Loop**: Added `prompt_user` tool allowing AI agents to request user input via AutoCAD crosshair (`point`), entity picking (`entity`), distance measurement, or text input.
- **Clean cancellation**: Cleanly handles user pressing ESC without crashing the MCP server.

All 316 unit tests passing.
```

---
### PR #08: `pr/08-vector-pdf-plotter`

**Título:**
```text
feat(export): add standalone vector PDF 1.4 plotter with standard paper formats (A4-A0) and stamp
```

**Descripción:**
```markdown
### Summary of Changes
- **Vector PDF plotter**: Native standalone PDF 1.4 vector generator in `export_data(format="pdf")` without heavy external binary dependencies.
- **ISO standards**: Supports standard ISO paper sizes (A4 through A0), scale framing, and title block stamps.

All 316 unit tests passing.
```

---
### PR #09: `pr/09-bim-metadata-xdata`

**Título:**
```text
feat(bim): add BIM semantic metadata and XDATA support (set_metadata, get_metadata)
```

**Descripción:**
```markdown
### Summary of Changes
- **BIM metadata**: Added `set_metadata` and `get_metadata` commands in `manage_entities`.
- **XDATA persistence**: Stores structured building properties (fire resistance, U-value, manufacturer, cost codes) in AutoCAD XDATA and DXF dictionaries under `MULTICAD_BIM`.

All 316 unit tests passing.
```

---
### PR #10: `pr/10-xref-raster-manager`

**Título:**
```text
feat(xrefs): add manage_xrefs tool for DWG external references and raster image attachments
```

**Descripción:**
```markdown
### Summary of Changes
- **XREF management**: Added `manage_xrefs` tool to attach, list, reload, and detach external DWG references.
- **Raster images**: Support for attaching georeferenced orthophotos and raster images (`attach_raster`).

All 316 unit tests passing.
```

---
### PR #11: `pr/11-drawing-inspector-and-viewer`

**Título:**
```text
feat(inspection): add inspect_drawing spatial intelligence and show_drawing_viewer interactive HTML5 CAD viewer
```

**Descripción:**
```markdown
### Summary of Changes
- **Spatial intelligence**: Added `inspect_drawing` with bounding box calculation, ASCII minimap generation, and Point-in-Polygon raycasting queries.
- **Interactive viewer**: Added `show_drawing_viewer` generating a standalone HTML5 Canvas viewer with zoom, pan, layer toggles, and space inspection.

All 316 unit tests passing.
```

---
### PR #12: `pr/12-smart-annotations`

**Título:**
```text
feat(annotations): add manage_annotations tool for automated room labeling and dimensioning
```

**Descripción:**
```markdown
### Summary of Changes
- **Space labeling**: Added `label_spaces` action to automatically compute polygon centroids, calculate area in m², and place centered room labels.
- **Auto dimensioning**: Added `auto_dimension` for building envelope and wall segment dimensioning.

All 316 unit tests passing.
```

---
### PR #13: `pr/13-offset-and-fillet`

**Título:**
```text
feat(entities): add offset, fillet, chamfer, explode, and matchprop manipulation tools
```

**Descripción:**
```markdown
### Summary of Changes
- **Parametric editing**: Added `offset_entity`, `fillet_entities`, `chamfer_entities`, `explode_entity`, and `match_properties` in `manage_entities` and CAD adapters.
- **CAD parity**: Full dual support across AutoCAD COM and headless ezdxf.

All 316 unit tests passing.
```

---
### PR #14: `pr/14-boundary-and-join`

**Título:**
```text
feat(entities): add boundary polyline detection, geometry join, trim, and extend
```

**Descripción:**
```markdown
### Summary of Changes
- **Boundary detection**: Added `create_boundary` for closed boundary polyline detection from an internal point.
- **Topology operations**: Added `join_entities` (joining contiguous segments into polylines with gap tolerance) and `trim_extend_entity` (trimming and extending segments against cutting edges).

All 316 unit tests passing.
```

---
### PR #15: `pr/15-geometry-snapping-intersections`

**Título:**
```text
feat(inspection): add geometric intersections query and object snapping assistant (OSNAP)
```

**Descripción:**
```markdown
### Summary of Changes
- **Vector intersections**: Added `intersections` mode in `inspect_drawing` to detect real crossing points between lines and polylines.
- **OSNAP assistant**: Added `snap` mode for magnetic snapping to endpoints, midpoints, and circle/arc centers within a tolerance.

All 316 unit tests passing.
```

---
### PR #16: `pr/16-paperspace-layout-generator`

**Título:**
```text
feat(layouts): add manage_layouts for paperspace sheets, viewports, architectural scaling, and AECO title blocks
```

**Descripción:**
```markdown
### Summary of Changes
- **Paperspace layouts**: Added `manage_layouts` tool for creating paperspace presentation sheets with standard ISO formats (A4 to A0).
- **MVIEW viewports**: Floating viewports linked to modelspace at standard architectural scales (1:50, 1:100, etc.).
- **AECO title blocks**: Standard sheet borders and title blocks with metadata.

All 316 unit tests passing.
```

---
### PR #17: `pr/17-advanced-hatch-patterns`

**Título:**
```text
feat(drawing): add architectural hatch patterns (ANSI31, AR-CONC, GRAVEL, SOLID), scaling, rotation, and boundary associativity
```

**Descripción:**
```markdown
### Summary of Changes
- **Architectural patterns**: Added support for standard technical hatch patterns (`ANSI31`, `AR-CONC`, `ANSI32`, `GRAVEL`, `EARTH`, `SOLID`) in `draw_entities(type="hatch")`.
- **Hatch controls**: Full support for scale, rotation angle, and associative boundary hatching via `boundary_handle`.

All 316 unit tests passing.
```

---
### PR #18: `pr/18-find-and-replace-text`

**Título:**
```text
feat(entities): add batch text find and replace across TEXT, MTEXT, and block attributes
```

**Descripción:**
```markdown
### Summary of Changes
- **Batch text replace**: Added `find_text` and `replace_text` in `manage_entities`.
- **Scope**: Searches and replaces across `TEXT`, `MTEXT`, and block attributes (`ATTRIB`).
- **Features**: Regex pattern matching, case sensitivity toggle, and layer filtering.

All 316 unit tests passing.
```

---
