# Modo: pipeline (conversación → canvas → derivados)

## Cuándo usar
Pablo quiere recorrer el camino completo en una sesión: de conversación exploratoria a artículo publicable + newsletter LinkedIn + post feed + prompt imagen.

## Recordatorio crítico

**Todo vive en el chat. Ningún archivo en disco, ningún toque al vault.**

## Pasos

### 1. Clasificar punto de partida
- a) **Solo tema o intuición** → empezar en `modes/conversar.md` y dejar que cristalice.
- b) **Borrador propio** → empezar en `modes/refine.md`.
- c) **Material fuente** → empezar en `modes/transform.md`.

### 2. Ejecutar fase inicial
Según (a/b/c), seguir el modo correspondiente hasta tener un **canvas estable** (hito 2 o 3 de `references/modo-iterativo-canvas.md`).

**Pausa obligatoria antes de derivados.** Cuando el canvas esté listo, preguntar explícitamente:

> "Canvas listo. ¿Avanzamos a derivados (newsletter LinkedIn / post feed / prompt imagen 1570:881)? ¿Cuáles quieres?"

No avanzar automáticamente.

### 3. Derivados — orden fijo
Una vez validado el canvas y confirmados los derivados deseados, producir **en este orden**:

1. **Prompt imagen 1570:881** (`derivatives/banner-spec.md`)  
   — primero, porque Pablo puede encargarla en paralelo mientras revisa el resto.

2. **Newsletter LinkedIn** (`derivatives/linkedin-newsletter.md`)  
   — versión larga del artículo adaptada al formato newsletter.

3. **Post de feed LinkedIn** (`derivatives/linkedin-feed.md`)  
   — versión corta que acompaña la publicación de la newsletter.

Entregar los tres en **bloques separados y claramente etiquetados** dentro del chat.

### 4. Paquete final
Al terminar, ofrecer resumen:

```
Paquete listo:

1. ARTÍCULO OBSIDIAN (canvas markdown arriba) — para copiar a tu vault
2. PROMPT IMAGEN 1570:881 — para pasar a tu generador
3. NEWSLETTER LINKEDIN — para copiar al editor de newsletter
4. POST FEED LINKEDIN — para copiar al editor de feed

Falta todavía (lo haces tú):
- Bloque YAML de coautoría (Tagger GPT)
- Tags finales del artículo (plantilla Obsidian)
- Imagen generada y embebida
- Revisión editorial humana final
```

## Anti-patrones

- ❌ Producir los 4 outputs sin pausa para validación del canvas base.
- ❌ Cambiar el tono entre artículo y derivados. La newsletter debe sonar a Pablo, no a "post LinkedIn genérico".
- ❌ Repetir literalmente párrafos enteros del artículo en la newsletter — adaptar al formato.
- ❌ Generar imagen directamente — el skill solo produce el prompt descriptivo.
- ❌ Saltarse la conversación exploratoria si Pablo vino con "solo tema". Los artículos emergen; no se piden.
- ❌ Escribir cualquier cosa a archivo. **Todo vive en el chat.**
