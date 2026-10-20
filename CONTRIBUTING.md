# 🛠️ Guía para Contribuir (O cómo ganarte un pedacito de cielo en CAD)

¡Buenas! Si estás leyendo esto es porque quieres arrimar el hombro a **multiCAD-MCP**, y eso ya te hace ser de mis personas favoritas de internet.

Este es un proyecto de código abierto enfocado a unir los modelos de lenguaje con el software CAD profesional (AutoCAD, ZWCAD, GstarCAD, BricsCAD y motores headless como `ezdxf`). Estamos aquí para cacharrear, aprender y hacer que la automatización técnica en arquitectura e ingeniería mole cada vez más. Se aceptan desde correcciones de comas o erratas en la documentación hasta nuevos comandos geométricos o conectores BIM épicos.

## 🚀 ¿Cómo puedes echar un cable?

No hace falta ser un *gurú* del kernel de AutoCAD para contribuir. Puedes ayudar de un montón de maneras, que aquí todo suma:

### 🐛 Cazando Bugs (Reportar errores)
¿Has encontrado una coordenada que no cuadra, un error COM con algún CAD específico, o un comando que hace cosas raras? Abre una *Issue*. 
Pero ojo, ayúdame a ayudarte:
- Dinos qué versión de CAD estás usando (AutoCAD 2024, ZWCAD 2025, modo headless DXF, etc.).
- La instrucción o shorthand que estabas ejecutando.
- La traza o mensaje de error de la terminal o de Claude / Cursor.
- Si puedes adjuntar un DXF mínimo o captura del problema, ¡oro puro!

### 💡 Proponer locuras (Nuevas ideas y comandos)
¿Se te ha ocurrido una macro arquitectónica increíble mientras te tomabas un café, calculabas una estructura o paseabas al perro? Abre una *Issue* con la etiqueta `enhancement` y cuéntame tu visión. Lo debatimos y vemos cómo integrarlo en la arquitectura de mixins o en el vocabulario shorthand.

### 🧪 Haciendo de "Crash Tester"
Instálate el servidor con `instalar_en_claude_desktop.bat` o vía CLI, dale caña con tus proyectos reales de arquitectura o ingeniería, y comprueba si aguanta el tirón. El feedback de usuarios reales en obra o despacho vale su peso en oro.

### 💻 Tirando código (Pull Requests)
¿Has solucionado un bug, optimizado una función geométrica o añadido un nuevo comando? ¡Ole tú! Sigue este pequeño ritual para que la PR vaya como la seda:

1. **Haz un *Fork*** de este repositorio a tu cuenta de GitHub.
2. **Crea una rama descriptiva**: `git checkout -b fix-calculo-orientaciones` o `feat-fillet-3d`. Evita nombres crípticos como `parche-1` o `mis-cambios`.
3. **Pica el código** manteniendo la arquitectura modular basada en mixins en `src/adapters/mixins/` y herramientas en `src/mcp_tools/tools/`.
4. **Verifica la suite de pruebas**: Todos los tests deben pasar antes de proponer cambios:
   ```powershell
   .venv\Scripts\pytest.exe -v
   ```
5. **Haz *commits* claros y atómicos**: Explica brevemente qué cambia y por qué.
6. **Sube tus cambios** a tu fork y **abre la Pull Request** hacia la rama `main`. Explica qué aporta tu cambio y qué has probado.

## 📜 Reglas de la casa

- **Sentido común y buen rollo**: Respeta el estilo de código existente, tipado estricto y docstrings en español / inglés técnico.
- **No rompas los cimientos**: Los tests existentes (316+) deben seguir pasando al 100%.
- **Soporte dual GUI y Headless**: Si añades una función de dibujo o edición, intenta que funcione tanto en AutoCAD/ZWCAD COM como en el motor autónomo `EzdxfAdapter`.
- **Documenta un poquito**: Si creas un nuevo comando o parámetro, refléjalo en `docs/05-REFERENCE.md` o en el docstring de la herramienta. Un comando sin documentar es como un comando secreto de consola que nadie sabe usar.

¡Y ya estaría! Anímate a trastear, proponer y equivocarte, que para eso estamos. ¡Muchas gracias por pasarte por aquí y aportar tu talento al ecosistema ConTech!
