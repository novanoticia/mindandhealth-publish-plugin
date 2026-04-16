# Modo: generate (volcado inicial de canvas)

## Cuándo usar
Hay que abrir un **canvas por primera vez**, típicamente porque:
- Venimos de una conversación exploratoria que ha cristalizado y Pablo ha aceptado abrir canvas.
- Pablo pide directamente "saca canvas sobre X" saltándose la conversación previa.

## Recordatorio crítico

**El canvas es un bloque markdown en el chat. Nunca un archivo en disco. Nunca en el vault.** Ver `references/modo-iterativo-canvas.md`.

## Pasos

### 1. Confirmar forma antes de redactar
Cuando se cristaliza (o Pablo pide canvas directo), antes de volcar el borrador preguntar brevemente:

- **Registro:** canónico (ensayo H2) / poético / fragmentario / diálogo / manifiesto.
- **Extensión orientativa:** breve (<800) / medio (800–2000) / largo (>2000).
- **Bilingüe ES/EN:** solo si tema lo pide (por defecto español).

Si venimos de conversación larga, muchas veces ya es evidente el registro y la extensión — entonces **proponer y confirmar en una línea**, no abrir interrogatorio:

> "Voy a sacar canvas en registro canónico, medio (unas 1200 palabras), en español. ¿Te parece, o ajustamos?"

### 2. Destilar lo conversado (si venimos de conversación)
Antes de redactar, tener claro en la cabeza:
- **Tesis emergente** (una frase).
- **Ideas fuerza** (3–4).
- **Metáforas o imágenes** que hayan circulado.
- **Citas o referencias** mencionadas por Pablo (a preservar).
- **Desacuerdos productivos** surgidos (pueden ser la disidencia útil del artículo).
- **Direcciones descartadas** (no volver a proponerlas).

### 3. Leer el vault para enlaces internos (opcional)
Antes del volcado, búsqueda rápida con Grep/Glob en la ruta del vault (ver `references/mapa-tematico.md` para la ruta configurada).
Para 2–4 artículos previos afines que se puedan proponer como enlaces internos.

### 4. Proponer estructura (antes del volcado completo)
Antes de volcar el canvas completo, presentar una **estructura breve** (6–10 líneas):

```
Título tentativo: ...
Metáfora orientadora: ... (o: sin metáfora explícita)
Estructura:
  - Apertura (epígrafe / blockquote / pregunta)
  - H2 1: ...
  - H2 2: ...
  - H2 3: ...
  - Cierre reflexivo
Enlaces internos propuestos: ... (2–4 artículos del vault)
```

Esperar visto bueno o ajustes de Pablo. **Esto evita reescrituras grandes.**

### 5. Volcar el canvas
Entregar el canvas completo como bloque markdown:

````
```markdown
---
title: "..."
subtitle: "..."
autor: "Pablo Rodríguez López & IA (Claude Sonnet 4.6)"
proyecto: "mindandhealth.org"
tipo: "articulo"
estado: "borrador - pendiente revision humana"
fecha: "YYYY-MM-DD"
canales:
  - web
tags:
  - tag1
  - tag2
# --- bloque coautoria va aquí (lo añade Pablo con Tagger) ---
---

[cuerpo del artículo]

[pie ético]
```
````

Sigue:
- `references/voz-editorial.md` rigurosamente.
- `references/estructura-yaml.md` para el frontmatter.
- `references/pie-etico.md` para el disclaimer (variante según tema).
- Al menos un momento de *disidencia útil* salvo que el registro sea poético-fragmentario.
- Metáfora orientadora recurrente si se acordó.
- Cierre que resuena, no concluye.

### 6. Recordar lo que falta (siempre, al final del volcado)
Después del bloque markdown, en chat:

```
Este canvas es un primer volcado. Queda iterar.

Recuerda que al copiarlo a tu vault tendrás que añadir:
- Bloque YAML de coautoría (con tu Tagger GPT).
- Etiquetas finales formateadas (plantilla Obsidian).
- Imagen, si decides incluirla (puedo darte un prompt 1570:881 si lo pides).

¿Quieres que pulamos algo o lo dejamos madurar?
```

### 7. Entrar en modo iteración
A partir de aquí, aplicar el protocolo de carriles (`references/modo-iterativo-canvas.md`). No seguir escribiendo versiones nuevas salvo en carriles "Petición" o "Sugerencia aprobada".

## Anti-patrones

- ❌ Escribir el canvas entero sin pasar por estructura preliminar (paso 4).
- ❌ Forzar metáfora que no pega con el tema o con lo conversado.
- ❌ Perder fragmentos, citas o matices que aparecieron en la conversación previa.
- ❌ Clichés de divulgación ("en este artículo exploraremos…", "en conclusión…").
- ❌ Inventar citas o referencias. Si Pablo mencionó a un autor, usar solo afirmaciones verificables o parafrasear declarando.
- ❌ Enlaces internos inventados — verificar antes en el vault.
- ❌ Guardar el canvas en disco. **Nunca.**
