# mindandhealth-publish-plugin

Plugin de Claude Code para **acompañamiento editorial conversacional** de las publicaciones de [mindandhealth.org](https://mindandhealth.org) (Obsidian Publish).

> **Compatible con [Agent Plugins 1.0.0](https://agent-plugins.org/specification)** — el formato portátil de empaquetado de la Agentic AI Foundation (OpenAI, Amazon,
> Microsoft, Cursor y Vercel, con Google como *core maintainer*).
> El paquete lleva el manifiesto portable `plugin.json` en la raíz del plugin y
> el skill en `plugins/mindandhealth-publish/skills/mindandhealth-publish/SKILL.md`, así que cualquier cliente conformante lo descubre.
>
> **Funciona en ChatGPT.** El skill es texto: instrucciones y criterios, sin
> ejecución local, así que se instala activando **Work** en el selector de ChatGPT y
> añadiéndolo desde **Complementos**, por nombre o por la URL de este repositorio.
> Funciona igual que en Claude. Su frontmatter
> valida contra el conjunto cerrado de [Agent Skills](https://agentskills.io/specification),
> que es lo que ChatGPT, claude.ai y la Skills API exigen para aceptar la subida
> —una clave de más ahí no se ignora, falla con error duro—. Están también en el
> **plan gratuito**, con límites de uso.

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
- Bajo petición: derivados (newsletter LinkedIn, post feed, prompt imagen 1570:880).
- Bajo petición: propuestas de enlaces internos a artículos previos del vault (solo lectura).

---

## Instalación

Hay tres formas de instalar el skill según dónde quieras usarlo.

### Claude Code (CLI) y Claude Desktop → pestaña Code

Añadir el marketplace y activar el plugin:

```bash
/plugin marketplace add novanoticia/mindandhealth-publish-plugin
/plugin install mindandhealth-publish@mindandhealth-publish-plugin
```

Una vez activo, dispones del slash command `/publish` y de los disparadores en lenguaje natural.

### Claude.ai (Claude Chat) — versión empaquetada como skill

Para usarlo en la web/app de Claude.ai:

1. Descarga el bundle: [`mindandhealth-publish-claude-ai.zip`](./mindandhealth-publish-claude-ai.zip) (≈33 KB).
   Versión legible del contenido en [`claude-ai/mindandhealth-publish/`](./claude-ai/mindandhealth-publish/).
2. En claude.ai: tu avatar (arriba a la derecha) → **Settings** → **Capabilities** → **Skills** → **Upload skill**.
3. Sube el zip y activa el toggle.

A partir de ahí se invoca en **lenguaje natural** ("publiquemos sobre X", "pensemos sobre Y para la web", "saca canvas", "haz la newsletter del último artículo"…). Claude.ai mostrará una insignia indicando que está usando el skill.

> **Requiere** plan **Max**, **Team** o **Enterprise** con Skills personalizadas habilitadas.

**Diferencias respecto a la versión Claude Code:** no incluye slash command `/publish` (Claude.ai no lo soporta) y no lee el vault local de Obsidian; los enlaces internos solo se proponen si Pablo aporta los títulos o el texto de artículos previos en el chat. Todo lo demás (flujo, principios, modos, derivados, pie ético de variación controlada) es idéntico.

### Perplexity (Skills)

Perplexity admite el mismo bundle que Claude.ai, sin pasos adicionales:

1. Descarga [`mindandhealth-publish-claude-ai.zip`](./mindandhealth-publish-claude-ai.zip).
2. En Perplexity, entra en la gestión de **Skills** y elige **subir / importar skill**.
3. Sube el zip y actívalo.

Se invoca en **lenguaje natural**, igual que en Claude.ai (sin slash command `/publish`). Aplican las mismas diferencias respecto a la versión Claude Code señaladas arriba.

> **Nota técnica:** el límite de longitud del campo `description` depende de la plataforma: Perplexity valida **en bytes UTF-8** (límite 1024) y Mistral **en caracteres** (límite 500). En español, los acentos y la `ñ` cuentan como 2 bytes. La descripción de este skill mide **453 caracteres / 458 bytes**, dentro de ambos umbrales. Si la editas, no superes los **500 caracteres** para conservar la compatibilidad con Mistral.

---

### Mistral AI (Skills)

Mistral admite el mismo bundle, instalado desde su espacio **Work**:

1. Descarga [`mindandhealth-publish-claude-ai.zip`](./mindandhealth-publish-claude-ai.zip) y **descomprímelo**.
2. En Mistral AI, dentro del espacio **Work**, abre la sección de **Skills**.
3. Selecciona la **carpeta** resultante (`mindandhealth-publish/`, la que contiene `SKILL.md`).

Se invoca en **lenguaje natural**, igual que en Claude.ai y Perplexity (sin slash command `/publish`).

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
mindandhealth-publish-plugin/
├── plugins/mindandhealth-publish/       # Versión Claude Code (plugin con marketplace)
│   ├── .claude-plugin/plugin.json
│   └── skills/mindandhealth-publish/
│       ├── SKILL.md                     # Orquestador y flujo
│       ├── modes/
│       │   ├── conversar.md             # Modo por defecto
│       │   ├── generate.md              # Volcado inicial a canvas
│       │   ├── refine.md                # Pulido de borrador aportado
│       │   ├── transform.md             # Canvas desde fuente (paper, URL, notas)
│       │   └── pipeline.md              # Recorrido completo conversación → derivados
│       ├── references/
│       │   ├── voz-editorial.md         # Tono, ritmo, metáforas
│       │   ├── estructura-yaml.md       # Frontmatter mínimo
│       │   ├── pie-etico.md             # Variación controlada del pie
│       │   ├── mapa-tematico.md         # Taxonomía del sitio
│       │   └── modo-iterativo-canvas.md # Carriles, hitos, anti-patrones
│       └── derivatives/
│           ├── linkedin-newsletter.md   # Artículo → newsletter
│           ├── linkedin-feed.md         # Newsletter → post feed
│           └── banner-spec.md           # Prompt imagen 1570:880
├── claude-ai/mindandhealth-publish/     # Versión Claude.ai (mismo contenido, sin slash command ni acceso al vault)
├── mindandhealth-publish-claude-ai.zip  # Bundle listo para subir a Claude.ai → Settings → Skills
├── commands/publish.md                  # Slash command /publish (solo Claude Code)
└── .claude-plugin/marketplace.json      # Manifest del marketplace
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
- **Prompt de imagen 1570:880** — descripción para banner (no genera imagen; solo el prompt).

---

## Autor

**Pablo Rodríguez López** — [mindandhealth.org](https://mindandhealth.org)

## Licencia

Apache-2.0
