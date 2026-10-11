# YAML frontmatter structure

## What the skill includes (functional minimum)

```yaml
---
title: "Título del artículo"
subtitle: "Subtítulo opcional"
autor: "Pablo Rodríguez López & AI (model)"
proyecto: "mindandhealth.org"
tipo: "articulo"        # or: ensayo, guia, manifiesto, reflexion, registro, poema
estado: "borrador - pendiente revision humana"
fecha: "YYYY-MM-DD"     # current date
canales:
  - web
  # optional, based on the conversation with Pablo:
  # - newsletter
  # - linkedin
nivel_divulgacion: "general"   # or: tecnico, academico, mixto
tags:
  - topic-tag-1
  - topic-tag-2
  - topic-tag-3
---
```

## What the skill does NOT include

### Co-authorship block

Pablo adds it later with his custom "Human–AI Co-authorship Tagger" GPT. Its shape is:

```yaml
ia_asistencia:
  modelo: "GPT-5.1" # or Claude Sonnet 4.6, etc.
  rol: "role description"
coautoria:
  nivel: 4
  voz: "AI++"
  descripcion: "..."
coauthorship:
  level: 4
  voice: "AI++"
  description: "..."
```

Leave a YAML comment marking its position:

```yaml
# --- co-authorship block goes here (Pablo adds it with Tagger) ---
```

### Formatted final tags

Pablo's Obsidian template generates the `🔖 **Tags:**` block with search links at the end. The skill only proposes base topic tags in frontmatter.

## Suggested base tags by topic

Propose 5–10 relevant tags from the site's controlled vocabulary. Preserve existing Spanish slugs where they correspond to the live site's taxonomy.

### AI and ethics

`inteligencia-artificial`, `etica`, `ai-ethics`, `ethical-ai`, `ethical-technology-use`, `ethical-ai-use`, `ai-policy`, `ai-governance`, `human-ai-interaction`, `human-machine-interaction`, `digital-authenticity`, `transparencia`, `responsabilidad`, `reflective-practice`, `co-authorship`, `ai-assisted-writing`

### Psychology / mental health

`psicologia`, `salud-mental`, `bienestar-mental`, `bienestar-emocional`, `bienestar-humano`, `desarrollo-personal`, `impacto-psicologico`, `afrontamiento`, `adaptacion`, `cambio`, `conciencia-reflexiva`, `psychological-impact`, `coping-strategies`

### Philosophy / thought

`filosofia`, `existencialismo`, `nihilismo`, `esperanza`, `pensamiento-critico`, `critical-thinking`, `reflexion`, `sentido`, `autonomia`, `cognitive-transformation`, `metaphorical-analysis`

### Decentralized technology / computing

`ipfs`, `redes-descentralizadas`, `digital-sovereignty`, `decentralized-knowledge`, `tecnologia`, `digital`, `digital-policy`

### Art / culture

`poesia`, `historia-del-arte`, `metafora`, `simbolo`

### Education / inclusion

`educacion-digital`, `inclusion-digital`, `educacion-inclusiva`, `inclusion-equidad`

### SAPAME / community

`sapame`, `salud-mental-comunitaria`, `participacion-comunitaria`

### Personal journal

`registro`, `reflexion-personal`, `autoayuda`

## Today's date

Always use the current system date in ISO `YYYY-MM-DD` format.
