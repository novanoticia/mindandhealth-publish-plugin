# Modo: refine (borrador de Pablo → canvas pulido)

## Cuándo usar
Pablo ya tiene un borrador (propio, o salido de otra IA) y quiere que lo pulamos para publicar. Lo pega en el chat o lo comparte.

## Recordatorio crítico

**El canvas es un bloque markdown en el chat. No escribo en el vault ni creo archivos.** Cuando termine el pulido, Pablo copia manualmente el canvas a su Obsidian.

## Pasos

### 1. Leer el borrador entero antes de sugerir nada
No empieces a editar línea por línea. Primero identifica:
- **Tesis central.** ¿Está clara? ¿Aparece pronto?
- **Voz.** ¿Suena a Pablo o suena genérico? (Comparar con `references/voz-editorial.md`.)
- **Estructura.** ¿Las secciones fluyen? ¿Falta apertura fuerte o cierre que resuene?
- **Matiz.** ¿Hay *disidencia útil* o va todo en una dirección?
- **Metáfora.** ¿Hay una orientadora? ¿Es concreta o abstracta?
- **Pie ético.** ¿Está? ¿Es la variante correcta?
- **YAML.** ¿Existe frontmatter? ¿Tags razonables?

### 2. Diagnóstico breve (antes de reescribir)
Dar a Pablo un diagnóstico en 5–8 puntos: qué funciona, qué cojea, qué falta.

```
Diagnóstico:
- Apertura: funciona la pregunta, pero le falta respiración (sugiero blockquote).
- Sección 2: la tesis se enreda entre dos ideas; propondría separar.
- Registro: por momentos muy técnico, pierde humanismo (ver §4).
- Falta: metáfora orientadora clara; posible: [propuesta].
- Falta: pie ético.
- Enlaces internos: ninguno — podrían encajar [X] y [Y].
```

### 3. Preguntar ambición de la edición
- **Ligera** (respetar voz, pulir ritmo, puntuación, repeticiones).
- **Media** (reorganizar secciones, reescribir aperturas/cierres, añadir matices).
- **Profunda** (reestructurar, reescribir amplias secciones).

Pablo decide el nivel. **No asumir profunda** salvo petición explícita.

### 4. Abrir canvas con el borrador pulido
Entregar el canvas completo como bloque markdown (incluyendo YAML original de Pablo si lo traía; solo sugerir adiciones/correcciones, no sustituirlo).

Si añades enlaces internos, verifica antes que los archivos existen en el vault.

### 5. Log de decisiones editoriales (opcional)
Si la edición fue media o profunda, ofrecer después del canvas un "Log de decisiones editoriales" (Pablo a veces lo incluye como transparencia):

```
**Log de decisiones editoriales**
- Se reescribió la apertura para subir la tesis al primer tercio.
- Se añadió la metáfora del roble y el junco en §3.
- Se separó §2 en 2a (diagnóstico) y 2b (propuesta) para mayor claridad.
- Se unificó el uso de cursivas (solo citas internas, no énfasis).
```

### 6. Iteración
A partir de aquí, protocolo de carriles (`references/modo-iterativo-canvas.md`).

## Anti-patrones

- ❌ Reescribir todo sin preguntar el nivel de edición.
- ❌ Perder la voz de Pablo "mejorándola" hacia tono neutro/divulgativo.
- ❌ Eliminar dudas, matices, "sospecho que", "me quedo con la pregunta" — eso es su marca.
- ❌ Sustituir su metáfora por otra "mejor" salvo petición explícita.
- ❌ Escribir el canvas a archivo. **Nunca.**
