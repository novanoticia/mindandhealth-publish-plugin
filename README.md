# mindandhealth-publish-plugin

Plugin de Claude Code para **acompañamiento editorial conversacional** de las publicaciones de [mindandhealth.org](https://mindandhealth.org) (Obsidian Publish).

No es un redactor automático. Es un interlocutor: conversa primero, destila cuando la idea cristaliza, genera derivados (LinkedIn + prompt de imagen) bajo petición. **Todo vive en el chat; nunca toca el vault.**

---

## Modelo mental

Los artículos de Pablo **no se piden, emergen**. El flujo que asume el skill:

1. **Conversación exploratoria** (modo por defecto). Tema, intuición, duda, lectura. Se cruzan perspectivas, se matiza, se contraargumenta. Rol del asistente: interlocutor, no redactor.
2. **Punto de cristalización.** Pablo pide canvas — o el asistente lo sugiere una sola vez, sin insistir, cuando detecta materia.
3. **Canvas.** Un bloque markdown vivo en el chat con lo destilado. No es un archivo en disco.
4. **Iteración.** Pablo comenta, pide, sugiere. El canvas se actualiza solo en los carriles "Petición" y "Sugerencia aprobada".
5. **Cierre.** Pablo copia manualmente el canvas a su vault de Obsidian. Si procede, se generan derivados.

---

## Qué NO hace (crítico)

- **Nunca** escribe en el vault ni en ningún archivo de disco. Todo el trabajo vive en la conversación.
- **Nunca** usa `Edit` o `Write` para guardar borradores.
- **No** genera las etiquetas `🔖 **Etiquetas:**` — las pone Pablo con plantilla de Obsidian.
- **No** genera el bloque YAML de coautoría — lo produce el GPT Tagger.
- **No** genera imágenes — solo prompts descriptivos bajo petición.
- **No** publica nada.
- **No** precipita hacia la redacción cuando la conversación apenas empieza.

## Qué SÍ hace

- Conversa como interlocutor transdisciplinar: perspectiva, contraargumento, referencia, metáfora candidata, pregunta devolutiva.
- Cuando se cristaliza y Pablo acepta: abre canvas con YAML mínimo, cuerpo Obsidian-compatible y pie ético al cierre.
- Itera el canvas según los carriles conversacionales (ver tabla más abajo).
- Bajo petición: derivados (newsletter LinkedIn, post feed, prompt imagen 1570:881).
- Bajo petición: propuestas de enlaces internos a artículos previos del vault (solo lectura).

---

## Instalación

Añadir el marketplace y activar el plugin desde Claude Code:

```bash
/plugin marketplace add novanoticia/mindandhealth-publish-plugin
/plugin install mindandhealth-publish@mindandhealth-publish-plugin
```

Funciona en Claude Code (CLI) y en Claude Desktop → pestaña **Code**.

---

## Uso

### Slash command

```
/publish [contexto opcional]
```

- **Sin argumento** → entra en modo conversar. Pregunta qué traes hoy.
- **Tema / intuición / pregunta abierta** → conversa con ese tema como punto de partida.
- **Borrador pegado** → entra en modo refinar (diagnóstico breve primero).
- **URL / cita / material fuente** → entra en modo transformar (inventario de fuentes primero).
- **Petición explícita** ("abre canvas con…", "dame la newsletter de…") → salta al modo correspondiente.

### Lenguaje natural

También se activa con frases como:

- "pensemos sobre X"
- "me ronda esta idea"
- "¿qué opinas de…?"
- "ayúdame a pulir este borrador"
- "saca canvas con lo que llevamos"
- "haz la newsletter del último artículo"
- "dame el prompt de imagen para este post"

---

## Protocolo de iteración (cuando hay canvas)

| Carril | Señal | Respuesta |
|---|---|---|
| **Pregunta** | "¿qué opinas de §2?" | Responde en chat. No reedita el canvas. |
| **Sugerencia** | "¿y si…?" | Evalúa; si hay acuerdo, aplica y devuelve canvas actualizado. |
| **Petición** | "cambia X" | Aplica y devuelve canvas actualizado (con diff breve). |
| **Exploración** | "dame tres aperturas" | Variantes en chat. No reedita el canvas. |
| **Conversación paralela** | "por cierto…" | Vuelve a modo conversar sin cerrar canvas. |
| **Validación** | "déjalo así" | Fija estado. Propone siguiente hito. |
| **Pausa** | "déjame pensarlo" | Reporta estado y se detiene. |

Solo **Petición** y **Sugerencia aprobada** devuelven canvas actualizado. En los demás carriles, conversación sin reedición.

---

## Principios editoriales

1. **Transdisciplinariedad.** Cruce entre técnica y humanidades.
2. **Honestidad epistémica.** "me quedo con la pregunta", "sospecho que…", "elección provisional".
3. **Matiz activo.** Disidencia útil, contraargumento, tensión productiva. Evitar dogmatismo.
4. **Metáfora orientadora.** Concreta, sensorial, sin estrépito. Cuando el tema lo pida.
5. **Cierre reflexivo, no conclusivo.** Pregunta abierta o gesto pequeño; no "en conclusión".
6. **Pie ético** al final del cuerpo, antes del divisor de Navegación. Siempre.
7. **Canvas vive en el chat.** Nunca en disco.

---

## Arquitectura del skill

```
plugins/mindandhealth-publish/
├── .claude-plugin/plugin.json
└── skills/mindandhealth-publish/
    ├── SKILL.md                         # Orquestador y flujo
    ├── modes/
    │   ├── conversar.md                 # Modo por defecto
    │   ├── generate.md                  # Volcado inicial a canvas
    │   ├── refine.md                    # Pulido de borrador aportado
    │   ├── transform.md                 # Canvas desde fuente (paper, URL, notas)
    │   └── pipeline.md                  # Recorrido completo conversación → derivados
    ├── references/
    │   ├── voz-editorial.md             # Tono, ritmo, metáforas
    │   ├── estructura-yaml.md           # Frontmatter mínimo
    │   ├── pie-etico.md                 # Disclaimer estándar ES/EN
    │   ├── mapa-tematico.md             # Taxonomía del sitio
    │   └── modo-iterativo-canvas.md     # Carriles, hitos, anti-patrones
    └── derivatives/
        ├── linkedin-newsletter.md       # Artículo → newsletter
        ├── linkedin-feed.md             # Newsletter → post feed
        └── banner-spec.md               # Prompt imagen 1570:881
```

---

## Vault (solo lectura)

El skill puede **leer** los `.md` del vault para extraer patrones, proponer enlaces internos o verificar citas. Ruta por defecto:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Pablo's Vault/website/
```

Ajustable en `plugins/mindandhealth-publish/skills/mindandhealth-publish/references/mapa-tematico.md`. **Nunca escribe en esa ruta.**

---

## Derivados disponibles

Bajo petición, a partir de un canvas maduro o un artículo ya publicado:

- **Newsletter LinkedIn** — adaptación extendida con apertura propia.
- **Post feed LinkedIn** — versión corta derivada de la newsletter.
- **Prompt de imagen 1570:881** — descripción para banner (no genera imagen; solo el prompt).

---

## Autor

**Pablo Rodríguez López** — [mindandhealth.org](https://mindandhealth.org)

## Licencia

Apache-2.0
