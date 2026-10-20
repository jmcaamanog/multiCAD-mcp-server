# 📐 multiCAD-MCP AECO Edition

| 🏗️ Perfil & ConTech | 📈 Repositorio & Enlaces |
| :--- | :--- |
| ![Profesión](https://img.shields.io/badge/Profesi%C3%B3n-Arquitectos%20T%C3%A9cnicos-2e7d32?logo=micro%3Abit&logoColor=white&style=plastic) <br> ![Role](https://img.shields.io/badge/Role-BIM%20%26%20ConTech-007ACC?logo=bim360&style=plastic) <br> ![Location](https://img.shields.io/badge/Location-A%20Coru%C3%B1a%20%F0%9F%8C%8A-005B94?logo=lighthouse&logoColor=white&style=plastic) <br> ![Sector](https://img.shields.io/badge/Sector-ConTech%20%7C%20AECO-E65100?logo=construct3&style=plastic) <br> ![Maker](https://img.shields.io/badge/Maker-Software-red?logo=makerbot&style=plastic) <br> ![Hardware](https://img.shields.io/badge/Hardware---grey?style=plastic) <br> ![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&style=plastic) <br> ![Language](https://img.shields.io/badge/Language-Python%203.11-3776AB?logo=python&logoColor=white&style=plastic) | [![Versión](https://img.shields.io/badge/Versi%C3%B3n-0.2.1--AECO-3b82f6?logo=github&style=plastic)](https://github.com/jmcaamanog/multiCAD-mcp/releases) <br> [![Tests](https://img.shields.io/badge/Tests-316%20Passed%20(100%25)-10b981?logo=pytest&logoColor=white&style=plastic)](https://github.com/jmcaamanog/multiCAD-mcp) <br> [![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-8b5cf6?style=plastic)](./LICENSE) <br> [![FastMCP](https://img.shields.io/badge/FastMCP-2.x%20%26%203.x-06b6d4?style=plastic)](https://github.com/jlowin/fastmcp) <br> [![ezdxf](https://img.shields.io/badge/Engine-Headless%20ezdxf-f59e0b?style=plastic)](https://ezdxf.mozman.at/) <br> [![Glama](https://img.shields.io/badge/Glama-MCP%20Server-7c3aed?style=plastic)](https://glama.ai/mcp/servers) <br> [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin)](https://www.linkedin.com/in/jmcaamanog/) |

### Servidor MCP Universal de Grado Industrial para Control de CAD mediante IA, Motor Headless DXF, Estándares AECO, Trazado PDF Vectorial, Visor Gráfico Interactivo y Puente ConTech CE3X.
*Control interactivo por lenguaje natural de AutoCAD, ZWCAD, GstarCAD y BricsCAD vía Windows COM, con motor offline autónomo DXF para arquitectura, construcción, mediciones y certificación energética.*

---

## ⚡ Enlaces y Accesos Rápidos

| 🌟 Recurso | 🚀 Acción / Enlace | 📝 Descripción |
| :--- | :--- | :--- |
| **Instalador 1-Clic** | 📥 **[Descargar instalador .bat](./instalar_en_claude_desktop.bat)** | Inyección automática y segura en Claude Desktop y Cursor. |
| **Historial de Cambios** | 📜 **[Ver CHANGELOG.md](./docs/03-CHANGELOG.md)** | Registro pormenorizado de novedades, mejoras y correcciones. |
| **Documentación Técnica** | 📚 **[Ver Guías en /docs](./docs/)** | Documentación de herramientas, comandos shorthand y arquitectura. |
| **Puente CE3X** | ⚡ **[Ver CE3X-MCP-SERVER](https://github.com/jmcaamanog/CE3X-MCP-Server)** | Certificación energética oficial desde planos CAD. |
| **Repositorio Upstream** | 🔗 **[AnCode666/multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp)** | Repositorio base original de la comunidad. |

---

> [!IMPORTANT]
> ### 📥 Instalación Rápida en 1-Clic para Claude Desktop y Cursor
> Si deseas conectar tu cliente de Inteligencia Artificial con tus herramientas de dibujo en segundos:
> 1. Clona o descarga el repositorio en local.
> 2. Haz doble clic sobre **`instalar_en_claude_desktop.bat`**.
> 3. El instalador detecta automáticamente el binario ejecutable `multicad-mcp.exe`, genera una copia de respaldo de seguridad `.bak` e inyecta la configuración en Claude Desktop y Cursor sin alterar tus otros servidores MCP.

---

## 🌟 Características Principales (AECO & ConTech Edition)

| Módulo | Icono | Funcionalidades Destacadas |
| :--- | :---: | :--- |
| **Motor Headless DXF** | ⚡ | **Adaptador universal `ezdxf` autónomo**. Permite crear, modificar, cubicar y exportar planos CAD `.dxf` en segundo plano sin necesitar licencias ni tener AutoCAD/ZWCAD abierto en Windows. |
| **Espacio Papel & Maquetación** | 📐 | Herramienta `manage_layouts`: creación automática de presentaciones ISO (`A4`, `A3`, `A2`, `A1`, `A0`), ventanas gráficas `MVIEW` a escalas normalizadas (`1:50`, `1:100`, etc.) y cajetines AECO con rotulación. |
| **Edición Paramétrica & Geometría** | ✂️ | Comandos nativos de modelado: `OFFSET` (equidistancia), `FILLET` (empalme con radio), `CHAMFER` (chaflán), `EXPLODE` (descomposición) e igualación de propiedades `MATCHPROP`. |
| **Topología, Contornos, Trim & Extend** | 🔗 | Detección automática de polilíneas de contorno desde punto interior (`BOUNDARY`), unión de segmentos contiguos con tolerancia de holgura (`JOIN`), y recorte / alargamiento contra aristas de corte (`TRIM` & `EXTEND`). |
| **Asistente OSNAP & Intersecciones** | 🧲 | Localización exacta de cruces geométricos entre curvas/líneas (`intersections`) y sonda inteligente de puntos de enganche (`snap`) para anclaje a extremos, puntos medios y centros. |
| **Tramas Técnicas & Sombreados** | 🧱 | Rayados normalizados (`ANSI31`, `AR-CONC`, `GRAVEL`, `EARTH`, `SOLID`) con control de escala, ángulo y sombreado asociativo por entidad de contorno. |
| **Búsqueda & Reemplazo Semántico** | 🔎 | Herramienta `replace_text` / `find_text` para búsqueda y sustitución por lotes en rótulos `TEXT`, `MTEXT` y atributos de bloques `ATTRIB` con soporte para expresiones regulares. |
| **Visor CAD Interactivo HTML5** | 👁️ | Generación y apertura en 1 clic de un visor web interactivo en Canvas con zoom suave, paneo, conmutador de capas y selección de recintos con inspección de m² y datos BIM. |
| **Inteligencia Espacial & Minimapas** | 🧭 | Inferencia espacial directa en el chat: consulta Point-in-Polygon ("¿qué hay en x,y?"), cálculo del bounding box envolvente y generación de minimapas ASCII esquemáticos. |
| **Rotulación & Acotación Inteligente** | 🏷️ | Acotación automática (`auto_dimension`) de la envolvente o de tramos de muro, y rotulación automática de recintos (`label_spaces`) con texto centrado en sus centroides y m² calculados. |
| **Conector ConTech CAD ➔ CE3X** | 🏢 | Extracción paramétrica de la envolvente térmica del edificio con **cálculo trigonométrico de orientaciones (N, S, E, O)** a partir de vectores normales y generación de archivo `.json` listo para alimentar `CE3X-MCP-SERVER`. |
| **Trazado PDF Vectorial Nativo** | 📄 | Impresión directa de planos en formato **PDF 1.4 vectorial puro** con formatos normalizados (`A4`, `A3`, `A2`, `A1`, `A0`), escalado de encuadre y cartela de rotulación sin requerir librerías externas pesadas. |
| **Human-in-the-Loop Interactivo** | 🤝 | Interacción bidireccional asistida: la IA solicita al usuario que pinche un punto con la **mirilla de AutoCAD** (`prompt_user point`), seleccione entidades en pantalla o introduzca distancias con cancelación limpia (`ESC`). |
| **Control de Cámara & Vistas 3D** | 🎥 | Herramienta `manage_view` con auto-zoom a entidades (`ze`), encuadre de ventanas (`zw`), centrado dinámico (`zc`), perspectivas 3D (`preset\|iso_se`, `preset\|top`) y estilos visuales (`style\|conceptual`, `style\|realistic`). |
| **Enriquecimiento Semántico BIM** | 🏷️ | Inyección y lectura de metadatos estructurados en entidades CAD mediante **XDATA (`MULTICAD_BIM`)**: resistencia al fuego (EI-120), transmitancia (U), fabricante y códigos de coste. |
| **Gestor de XREFs & Ortofotas** | 🗺️ | Coordinación de proyectos multidisciplinares: enlace y recarga de referencias externas DWG (`attach_dwg`, `reload`, `detach`) e inserción de ortofotos PNOA o planos escaneados (`attach_raster`). |
| **Plantillas Normalizadas AECO** | 🏛️ | Comando `manage_layers template\|aeco` para generar al instante estructuras de capas estándar de edificación (muros, particiones, carpinterías, cotas, textos, MEP) con colores ACI y grosores según CTE DB-HE y COAM. |
| **Cálculo de Superficies & Cuadros** | 📐 | Medición analítica de recintos poligonales (algoritmo Shoelace / Gauss) y generación automática de **Tablas CAD de Cuadros de Superficies Útiles** (`area_table\|x,y\|capa\|título`). |
| **Presupuestos FIEBDC-3 (.bc3)** | 💰 | Exportación de líneas de medición CAD directamente a formato estándar de costes de edificación (`.bc3`), compatible con Presto, Arquímedes y Menfis. |
| **Macros Arquitectónicas** | 🧱 | Comandos shorthand compuestos de alta velocidad: `wall` (doble línea paramétrica), `door` (vano, batiente y arco abatible) y `window` (marco y vidrio). |
| **Auditoría QA & Purge** | 🔍 | Verificación de salud del dibujo CAD: detección de entidades en capa 0, líneas duplicadas y purga automática de capas vacías no referenciadas. |

---

## 🛠️ Herramientas Unificadas MCP Disponibles

1. **`manage_session`**: Ciclo de vida de la conexión, estado de instancias CAD y navegación histórica.
2. **`manage_view`**: Control de encuadre, cámara, auto-zoom extents/window, vistas 3D axonométricas y estilos visuales.
3. **`manage_layouts`**: Gestión completa de espacio papel, formatos ISO normalizados (`A4` a `A0`), ventanas gráficas `MVIEW` escaladas y cajetines AECO con rotulación.
4. **`prompt_user`**: Interacción "Human-in-the-Loop" solicitando clics en pantalla (`point`), selección de objetos (`entity`), distancias o texto vía AutoCAD Utility.
5. **`draw_entities`**: Primitivas vectoriales, tramas técnicas (`ANSI31`, `AR-CONC`, `GRAVEL`, `SOLID`) y macros arquitectónicas (`wall`, `door`, `window`, `table`, etc.).
6. **`manage_entities`**: Modificación paramétrica (`offset`, `fillet`, `chamfer`, `explode`, `matchprop`, `boundary`, `join`, `trim`, `extend`), búsqueda semántica (`find_text`, `replace_text`), medición (`area`, `area_table`), auditoría (`audit`) y metadatos BIM XDATA (`set_metadata`, `get_metadata`).
7. **`manage_layers`**: Creación, visibilidad, colores y plantillas normalizadas (`template\|aeco`, `template\|aia`, `template\|mep`, `purge`).
8. **`manage_blocks`**: Creación, inserción y lectura/escritura de atributos de bloques.
9. **`manage_files`**: Apertura, guardado, alternancia y cierre de archivos DWG/DXF.
10. **`manage_xrefs`**: Enlace, recarga y desenlace de referencias externas DWG e imágenes ráster/ortofotos.
11. **`export_data`**: Extracción a JSON, Excel, presupuestos FIEBDC-3 (`.bc3`) y planos en PDF vectorial (`.pdf`).
12. **`export_ce3x_envelope`**: Extracción paramétrica de la envolvente térmica (fachadas orientadas, huecos, forjados) para certificación energética oficial en `CE3X-MCP-SERVER`.
13. **`inspect_drawing`**: Inteligencia espacial, consulta Point-in-Polygon ("¿qué hay en x,y?"), detección de cruces (`intersections`), asistente de enganche `snap` (OSNAP) y minimapa ASCII.
14. **`manage_annotations`**: Acotación automática de edificios y paredes (`auto_dimension`), rotulación inteligente de recintos con m² en centroides (`label_spaces`) y directrices.
15. **`show_drawing_viewer`**: Generación y apertura en 1 clic de un visor CAD interactivo en HTML5/Canvas en el navegador con zoom, pan, control de capas e inspección de recintos.



---

## 📜 Historial de Versiones

> 📜 **[Ver Historial de Versiones Completo (CHANGELOG.md)](./docs/03-CHANGELOG.md)**

---

## 👨‍💻 Autor de la Versión Mejorada

**Jose Manuel Caamaño González** | Arquitecto Técnico & BIM Manager  
Digital Product Lead | ConTech & Digital Twin SaaS | Data Analytics (SQL, Power BI)  

Hecho con código y café desde A Coruña. ☕  
[LinkedIn](https://www.linkedin.com/in/jmcaamanog/) · [Web](https://jmcaamanog.pages.dev)
