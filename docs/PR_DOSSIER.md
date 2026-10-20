# 🚀 Dossier Oficial de Pull Requests (multiCAD-MCP)

Guía completa y estructurada para el lanzamiento de los **18 Pull Requests atómicos** desde el fork [`jmcaamanog/multiCAD-mcp`](https://github.com/jmcaamanog/multiCAD-mcp) hacia el repositorio upstream [`AnCode666/multiCAD-mcp`](https://github.com/AnCode666/multiCAD-mcp).

---

## ⚡ Enlaces Directos de Creación de PR (1-Clic)

| # | Rama | Título de la PR | Enlace Directo para Abrir la PR |
| :-: | :--- | :--- | :--- |
| **01** | `pr/01-fix-fastmcp-and-security` | `fix: resolve FastMCP 2.x/3.x compatibility, security test isolation, and fix broken changelog link` | [🔗 Abrir PR #01](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/01-fix-fastmcp-and-security?expand=1) |
| **02** | `pr/02-cli-entrypoint-and-parsers` | `feat(cli): add multicad-mcp CLI entrypoint, CLI flags, and resilient list/dict shorthand input parsing` | [🔗 Abrir PR #02](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/02-cli-entrypoint-and-parsers?expand=1) |
| **03** | `pr/03-1click-desktop-installer` | `feat(installer): add 1-click Windows installer for Claude Desktop and Cursor with automatic backup` | [🔗 Abrir PR #03](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/03-1click-desktop-installer?expand=1) |
| **04** | `pr/04-headless-ezdxf-engine` | `feat(adapter): add autonomous headless ezdxf CAD adapter with automated fallback` | [🔗 Abrir PR #04](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/04-headless-ezdxf-engine?expand=1) |
| **05** | `pr/05-cad-qa-audit-purge-and-ci` | `ci: add GitHub Actions CI/CD workflows, release automation, CAD audit and layer purge` | [🔗 Abrir PR #05](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/05-cad-qa-audit-purge-and-ci?expand=1) |
| **06** | `pr/06-view-camera-control` | `feat(view): add manage_view tool for camera zoom extents/window, 3D view presets, and visual styles` | [🔗 Abrir PR #06](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/06-view-camera-control?expand=1) |
| **07** | `pr/07-human-in-the-loop` | `feat(interaction): add prompt_user tool for human-in-the-loop CAD crosshair and entity selection` | [🔗 Abrir PR #07](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/07-human-in-the-loop?expand=1) |
| **08** | `pr/08-vector-pdf-plotter` | `feat(export): add standalone vector PDF 1.4 plotter with standard paper formats (A4-A0) and stamp` | [🔗 Abrir PR #08](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/08-vector-pdf-plotter?expand=1) |
| **09** | `pr/09-bim-metadata-xdata` | `feat(bim): add BIM semantic metadata and XDATA support (set_metadata, get_metadata)` | [🔗 Abrir PR #09](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/09-bim-metadata-xdata?expand=1) |
| **10** | `pr/10-xref-raster-manager` | `feat(xrefs): add manage_xrefs tool for DWG external references and raster image attachments` | [🔗 Abrir PR #10](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/10-xref-raster-manager?expand=1) |
| **11** | `pr/11-drawing-inspector-and-viewer` | `feat(inspection): add inspect_drawing spatial intelligence and show_drawing_viewer interactive HTML5 CAD viewer` | [🔗 Abrir PR #11](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/11-drawing-inspector-and-viewer?expand=1) |
| **12** | `pr/12-smart-annotations` | `feat(annotations): add manage_annotations tool for automated room labeling and dimensioning` | [🔗 Abrir PR #12](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/12-smart-annotations?expand=1) |
| **13** | `pr/13-offset-and-fillet` | `feat(entities): add offset, fillet, chamfer, explode, and matchprop manipulation tools` | [🔗 Abrir PR #13](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/13-offset-and-fillet?expand=1) |
| **14** | `pr/14-boundary-and-join` | `feat(entities): add boundary polyline detection, geometry join, trim, and extend` | [🔗 Abrir PR #14](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/14-boundary-and-join?expand=1) |
| **15** | `pr/15-geometry-snapping-intersections` | `feat(inspection): add geometric intersections query and object snapping assistant (OSNAP)` | [🔗 Abrir PR #15](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/15-geometry-snapping-intersections?expand=1) |
| **16** | `pr/16-paperspace-layout-generator` | `feat(layouts): add manage_layouts for paperspace sheets, viewports, architectural scaling, and AECO title blocks` | [🔗 Abrir PR #16](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/16-paperspace-layout-generator?expand=1) |
| **17** | `pr/17-advanced-hatch-patterns` | `feat(drawing): add architectural hatch patterns (ANSI31, AR-CONC, GRAVEL, SOLID), scaling, rotation, and boundary associativity` | [🔗 Abrir PR #17](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/17-advanced-hatch-patterns?expand=1) |
| **18** | `pr/18-find-and-replace-text` | `feat(entities): add batch text find and replace across TEXT, MTEXT, and block attributes` | [🔗 Abrir PR #18](https://github.com/AnCode666/multiCAD-mcp/compare/main...jmcaamanog:multiCAD-mcp:pr/18-find-and-replace-text?expand=1) |

---

## 📝 Contenido Detallado de las Pull Requests

### PR #01: `fix: resolve FastMCP 2.x/3.x compatibility, security test isolation, and fix broken changelog link`
- **Motivación**: En las versiones recientes de `mcp` (v2.x y superiores), `mcp.server.fastmcp` fue renombrado o deprecado, causando un `ModuleNotFoundError` en entornos limpios. Asimismo, el test de seguridad de traversal path tenía un fallo de aislamiento y el link del CHANGELOG en README apuntaba a un archivo 07 inexistente.
- **Cambios**:
  - `src/mcp_tools/decorators.py`: Importar FastMCP directamente desde el paquete `fastmcp`.
  - `tests/unit/test_security.py`: Aislar configuración de `allow_arbitrary_paths` durante el test.
  - `README.md`: Corregir enlace a `docs/03-CHANGELOG.md`.

---

### PR #02: `feat(cli): add multicad-mcp CLI entrypoint, CLI flags, and resilient list/dict shorthand input parsing`
- **Motivación**: Facilitar el empaquetado y la ejecución directa del servidor desde cualquier terminal o lanzador (`uvx multiCAD-mcp`).
- **Cambios**:
  - `src/server.py`: Definir función `main()` con soporte para flags de transporte (`--transport stdio|http`), host, puerto y desactivación de dashboard.
  - `pyproject.toml`: Registrar `[project.scripts]` para generar el binario `multicad-mcp`.
  - `src/mcp_tools/shorthand.py`: Robustecer parsers para aceptar diccionarios o listas nativas generadas por clientes LLM.

---

### PR #03: `feat(installer): add 1-click Windows installer for Claude Desktop and Cursor with automatic backup`
- **Motivación**: Reducir a cero la fricción de instalación para usuarios que no desean editar manualmente archivos JSON.
- **Cambios**:
  - `scripts/instalar_claude_desktop.py`: Localiza `claude_desktop_config.json` y configuraciones de Cursor, genera backups `.bak` automáticos e inyecta `multicad-mcp`.
  - `instalar_en_claude_desktop.bat`: Script ejecutable por doble clic en Windows.

---

### PR #04: `feat(adapter): add autonomous headless ezdxf CAD adapter with automated fallback`
- **Motivación**: Permitir el uso del servidor MCP en servidores Linux, pipelines CI/CD o equipos Windows sin licencias de CAD abiertas.
- **Cambios**:
  - `src/adapters/ezdxf_adapter.py`: Implementación autónoma de `CADInterface` usando `ezdxf`.
  - `src/adapters/adapter_manager.py`: Auto-fallback transparente a `ezdxf` cuando no se detecta AutoCAD o ZWCAD en ejecución.

---

### PR #05: `ci: add GitHub Actions CI/CD workflows, release automation, CAD audit and layer purge`
- **Motivación**: Automatizar pruebas unitarias en GitHub y dotar al MCP de comandos de control de calidad para dibujos CAD.
- **Cambios**:
  - `.github/workflows/ci.yml` y `release.yml`: Pipelines de validación continua y publicación de releases.
  - `manage_entities`: Acción `audit` para detectar líneas de longitud cero, duplicados y entidades en capa 0.
  - `manage_layers`: Acción `purge` para eliminar capas vacías no referenciadas.

---

### PR #06: `feat(view): add manage_view tool for camera zoom extents/window, 3D view presets, and visual styles`
- **Motivación**: Permitir al LLM controlar la cámara y encuadrar el dibujo para ver el resultado de sus operaciones.
- **Cambios**:
  - Nueva herramienta `manage_view`: `zoom_extents`, `zoom_window`, `zoom_center`.
  - Presets 3D axonométricos (`top`, `front`, `iso_sw`, etc.) y estilos visuales (`wireframe`, `conceptual`, `realistic`).

---

### PR #07: `feat(interaction): add prompt_user tool for human-in-the-loop CAD crosshair and entity selection`
- **Motivación**: Habilitar interacción bidireccional entre la IA y el usuario mediante la mirilla y selección gráfica de AutoCAD.
- **Cambios**:
  - Nueva herramienta `prompt_user`: `point`, `entity`, `distance`, `text` usando `AutoCAD.Utility`.
  - Manejo de cancelación limpia mediante tecla `ESC`.

---

### PR #08: `feat(export): add standalone vector PDF 1.4 plotter with standard paper formats (A4-A0) and stamp`
- **Motivación**: Trazar planos a PDF vectorial puro sin requerir impresoras virtuales o librerías binarias externas.
- **Cambios**:
  - Motor de trazado PDF 1.4 nativo en `export_data(format="pdf")`.
  - Soporte para formatos ISO (`A4` a `A0`) y cartela de rotulación.

---

### PR #09: `feat(bim): add BIM semantic metadata and XDATA support (set_metadata, get_metadata)`
- **Motivación**: Permitir enriquecer entidades CAD con propiedades BIM estructuradas persistentes.
- **Cambios**:
  - Comandos `set_metadata` y `get_metadata` en `manage_entities`.
  - Persistencia en XDATA de AutoCAD y diccionarios DXF bajo la aplicación registrada `MULTICAD_BIM`.

---

### PR #10: `feat(xrefs): add manage_xrefs tool for DWG external references and raster image attachments`
- **Motivación**: Gestionar referencias externas DWG y cartografía ráster/ortofotos en proyectos colaborativos.
- **Cambios**:
  - Nueva herramienta `manage_xrefs`: `attach_dwg`, `list`, `reload`, `detach`, `attach_raster`.

---

### PR #11: `feat(inspection): add inspect_drawing spatial intelligence and show_drawing_viewer interactive HTML5 CAD viewer`
- **Motivación**: Dotar al LLM de visión espacial del plano (bounding box, minimapa ASCII, Point-in-Polygon) y visor interactivo Canvas.
- **Cambios**:
  - Herramienta `inspect_drawing`: Modos `summary` y `point` (raycasting).
  - Herramienta `show_drawing_viewer`: Generación y apertura en 1 clic de visor interactivo HTML5 en el navegador.

---

### PR #12: `feat(annotations): add manage_annotations tool for automated room labeling and dimensioning`
- **Motivación**: Automatizar tareas repetitivas de rotulación de superficies y acotación de planos.
- **Cambios**:
  - Herramienta `manage_annotations`: `label_spaces` (rótulo centrado con m²) y `auto_dimension` (cotas exteriores y de tramos).

---

### PR #13: `feat(entities): add offset, fillet, chamfer, explode, and matchprop manipulation tools`
- **Motivación**: Dotar a los agentes de IA de los comandos de edición paramétrica fundamentales de AutoCAD.
- **Cambios**:
  - Soporte de `offset`, `fillet`, `chamfer`, `explode` y `matchprop` en `manage_entities` y shorthand.
  - Soporte dual completo en AutoCAD COM y ezdxf.

---

### PR #14: `feat(entities): add boundary polyline detection, geometry join, trim, and extend`
- **Motivación**: Permitir la generación topológica de contornos cerrados y limpieza de líneas de intersección.
- **Cambios**:
  - `boundary`: Detección de contornos cerrados desde punto interior.
  - `join`: Unión de líneas contiguas en polilíneas con holgura.
  - `trim` y `extend`: Recorte y alargamiento de segmentos contra líneas de corte.

---

### PR #15: `feat(inspection): add geometric intersections query and object snapping assistant (OSNAP)`
- **Motivación**: Asistir a la IA en la localización de puntos de anclaje de alta precisión y cruces entre curvas.
- **Cambios**:
  - Modo `intersections` en `inspect_drawing` para calcular cruces entre entidades.
  - Modo `snap` para asistencia de imán OSNAP (`endpoint`, `midpoint`, `center`).

---

### PR #16: `feat(layouts): add manage_layouts for paperspace sheets, viewports, architectural scaling, and AECO title blocks`
- **Motivación**: Automatizar la maquetación y preparación de láminas para impresión oficial.
- **Cambios**:
  - Nueva herramienta `manage_layouts`: Formatos ISO (`A4` a `A0`), ventanas gráficas `MVIEW` a escalas normalizadas (1:50, 1:100) y cajetines AECO con rotulación.

---

### PR #17: `feat(drawing): add architectural hatch patterns (ANSI31, AR-CONC, GRAVEL, SOLID), scaling, rotation, and boundary associativity`
- **Motivación**: Permitir el rayado y sombreado técnico de planos para representación de materiales constructivos.
- **Cambios**:
  - Patrones estándar `ANSI31`, `AR-CONC`, `ANSI32`, `GRAVEL`, `EARTH`, `SOLID` con control de escala y ángulo.
  - Soporte de sombreado asociativo por handle de contorno (`boundary_handle`).

---

### PR #18: `feat(entities): add batch text find and replace across TEXT, MTEXT, and block attributes`
- **Motivación**: Permitir la búsqueda y modificación masiva de textos y leyendas de planos.
- **Cambios**:
  - Comandos `find_text` y `replace_text` en `manage_entities`.
  - Búsqueda en `TEXT`, `MTEXT` y atributos `ATTRIB` con soporte para expresiones regulares (`regex`) y filtrado de capas.
