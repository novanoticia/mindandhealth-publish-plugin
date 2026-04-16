# Estructura YAML del frontmatter

## Qué incluye el skill (mínimo funcional)

```yaml
---
title: "Título del artículo"
subtitle: "Subtítulo opcional"
autor: "Pablo Rodríguez López & IA (modelo)"
proyecto: "mindandhealth.org"
tipo: "articulo"        # o: ensayo, guia, manifiesto, reflexion, registro, poema
estado: "borrador - pendiente revision humana"
fecha: "YYYY-MM-DD"     # fecha actual
canales:
  - web
  # opcional, según conversación con Pablo:
  # - newsletter
  # - linkedin
nivel_divulgacion: "general"   # o: tecnico, academico, mixto
tags:
  - tag-tematico-1
  - tag-tematico-2
  - tag-tematico-3
---
```

## Qué NO incluye el skill (lo pone Pablo después)

### Bloque de coautoría
Pablo lo añade con su GPT personalizado "Tagger Coautoría Humano-IA" (https://chatgpt.com/g/g-691f7a5cd984819192de02e9de9a2623). Tiene esta forma:

```yaml
ia_asistencia:
  modelo: "GPT-5.1" # o Claude Sonnet 4.6, etc.
  rol: "descripcion del rol"
coautoria:
  nivel: 4
  voz: "AI++"
  descripcion: "..."
coauthorship:
  level: 4
  voice: "AI++"
  description: "..."
```

**Dejar un comentario en el YAML** indicándole dónde va:

```yaml
# --- bloque coautoria va aquí (lo añade Pablo con Tagger) ---
```

### Tags finales formateados
El bloque `🔖 **Etiquetas:**` con enlaces `[ #tag](/search?query=...)` al final del artículo lo genera su plantilla de Obsidian. El skill **solo** propone los tags temáticos base en el frontmatter `tags:`.

## Tags base sugeridos por eje temático

Cuando Pablo te diga el eje temático, propón 5–10 tags relevantes del siguiente vocabulario controlado (observado en sus artículos reales):

### IA y ética
`inteligencia-artificial`, `etica`, `ai-ethics`, `ethical-ai`, `ethical-technology-use`, `ethical-ai-use`, `ai-policy`, `ai-governance`, `human-ai-interaction`, `human-machine-interaction`, `digital-authenticity`, `transparencia`, `transparencia-datos`, `responsabilidad`, `reflective-practice`, `co-authorship`, `ai-assisted-writing`

### Psicología / salud mental
`psicologia`, `salud-mental`, `bienestar-mental`, `bienestar-emocional`, `bienestar-humano`, `bienestar-personal`, `desarrollo-personal`, `impacto-psicologico`, `afrontamiento`, `adaptacion`, `estrategias-de-afrontamiento`, `cambio`, `conciencia-reflexiva`, `psychological-impact`, `coping-strategies`

### Filosofía / pensamiento
`filosofia`, `existencialismo`, `nihilismo`, `esperanza`, `pensamiento-critico`, `critical-thinking`, `reflexion`, `sentido`, `autonomia`, `cognitive-transformation`, `metaphorical-analysis`

### Tecnología descentralizada / informática
`ipfs`, `redes-descentralizadas`, `digital-sovereignty`, `decentralized-knowledge`, `tecnologia`, `digital`, `digital-policy`

### Arte / cultura
`poesia`, `historia-del-arte`, `metafora`, `simbolo`

### Educación / inclusión
`educacion-digital`, `inclusion-digital`, `educacion-inclusiva`, `inclusion-equidad`

### SAPAME / comunidad
`sapame`, `salud-mental-comunitaria`, `participacion-comunitaria`

### Registro personal
`registro`, `reflexion-personal`, `autoayuda`

## Fecha de hoy

Usa siempre la fecha actual del sistema. Formato ISO `YYYY-MM-DD` en `fecha:`.
