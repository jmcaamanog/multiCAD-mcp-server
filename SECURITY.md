# 🛡️ Política de Seguridad (O cómo evitar que el chiringuito arda)

## 🛠️ Versiones Soportadas

Solo damos soporte a lo último de lo último en la rama activa. Si vives en el pasado, estás por tu cuenta.

| Versión | ¿Te hacemos casito? |
|---------|---------------------|
| `main` / `0.2.x` | ✅ Sí, a tope. |
| Anteriores      | 💀 Buena suerte. |

## 🚨 Cómo reportar una pifia de seguridad

**¡ALTO AHÍ, COWBOY! 🛑 Bajo ningún concepto abras una *issue* pública para reportar una vulnerabilidad.** Reportar un fallo de seguridad en público es como gritar "¡He dejado la puerta del estudio abierta y la caja fuerte sin clave!" en mitad de la plaza. No le des el trabajo masticado a los curiosos de turno.

Si has estado trasteando con multiCAD-MCP y has detectado una brecha seria (por ejemplo: evasión de *path traversal* en guardado/exportación de archivos CAD, inyección de comandos en el intérprete COM, o exposición indebida del dashboard local):

1. Envíame un correo directo a mi atención (**Jose Manuel Caamaño González** | `5682292+jmcaamanog@users.noreply.github.com`). Pon en el asunto algo como `[SECURITY] Reporte en multiCAD-MCP`.
2. Cuéntamelo con todo detalle:
   - **¿Qué tipo de brujería es esta?** (Tipo de vulnerabilidad: *path traversal*, RCE, fuga de datos, etc.).
   - **El truco de magia (PoC):** Pasos exactos o payload shorthand/JSON para reproducirla paso a paso.
   - **El nivel de drama:** ¿Qué es lo peor que podría pasar si cae en malas manos? (Impacto potencial en el sistema host).
   - **Dónde está el fuego:** Archivo, función o versión afectada.

Te responderé lo antes posible (normalmente en menos de 48-72 horas hábiles, a no ser que esté en obra, corriendo un 10K o paseando al perro). Una vez confirmemos y parchemos el agujero, te pondremos una mención de honor en las notas de la versión para reconocer tu ayuda ética, a menos que prefieras mantener un perfil discreto a lo Batman.

## 🤫 Pacto de silencio (Divulgación Responsable)

Te lo pido por lo que más quieras: sé buena gente y no vayas cascando la vulnerabilidad por foros, redes o barras de bar hasta que hayamos liberado el parche oficial. Vamos a dar un margen de cortesía razonable para que los usuarios puedan actualizar con tranquilidad.
