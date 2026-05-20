# Derivado: Prompt de imagen 1570:880

## Propósito
Generar un **prompt descriptivo** que Pablo pueda pasar a su generador de imagen habitual (DALL·E, Midjourney, Gemini, etc.). El skill **no genera la imagen**; solo el prompt.

## Formato de la imagen objetivo

- **Proporción:** 1570:880 (aproximadamente 16:9, pero exacto para LinkedIn newsletter banner).
- **Uso principal:** portada de newsletter LinkedIn.
- **Uso secundario:** imagen de cierre o apertura del artículo Obsidian (opcional).
- **Puede o no contener texto** (depende de la pieza; preguntar a Pablo si lo quiere).

## Estilo visual observado en sus imágenes previas

Basado en los archivos del vault (`banneretico.png`, `index-portada.png`, `imagen_inicio.webp`, imágenes de poemas de Juan Haro, ilustraciones de artículos):

- **Paletas frecuentes:** azules profundos y ámbar cálido; ocres y beiges; blanco y negro con acento de color.
- **Registros visuales que aparecen:**
  - Abstracto geométrico / cubista (hexágonos, fractales).
  - Ilustración vectorial plana con textura.
  - Fotografía editorial con tono cálido.
  - Collage simbólico (raíces, voces, laberintos).
- **Símbolos recurrentes:** panales/hexágonos (inteligencia colectiva), laberintos, lámparas, raíces, fragmentos, grietas de luz, árboles.
- **Tipografías:** góticas modernas para títulos principales; sans-serif limpia para subtítulos.

## Plantilla del prompt

```
Imagen horizontal, proporción 1570:880, [ESTILO VISUAL].

[DESCRIPCIÓN DEL MOTIVO CENTRAL] — [símbolo/metáfora orientadora del artículo].

[PALETA DE COLOR] — [2-3 colores dominantes y cómo se distribuyen].

[AMBIENTE / TONO]: [adjetivos: sereno, reflexivo, denso, luminoso, melancólico, sobrio…].

[COMPOSICIÓN]: [cómo se distribuye el espacio — centrado, asimétrico, con masa a la izquierda, con horizonte bajo, etc.].

[TEXTO EN IMAGEN]: [o bien "sin texto", o bien "incluye el texto: '[TEXTO]' en tipografía gótica moderna, [posición]"].

Referencias estéticas: [1-2 referencias si aplican — p.ej. "ilustración vectorial plana al estilo editorial contemporáneo", "grabado digital", "fotografía editorial tonalidad cálida"].

Evitar: texto ilegible, estética de stock genérica, figuras humanas con rasgos distorsionados, exceso de elementos decorativos.
```

## Ejemplos concretos según tema

### Tema: ética de IA / pensamiento asistido
```
Imagen horizontal, proporción 1570:880, ilustración vectorial plana con textura.

Una lámpara de aceite antigua suspendida en medio de un laberinto geométrico que se extiende hacia el horizonte. La lámpara proyecta un haz de luz que ilumina solo una parte del camino.

Paleta: azul profundo (60% del espacio), ámbar cálido (zona iluminada), blanco roto (detalles del laberinto).

Ambiente sereno, reflexivo, con tensión latente entre lo que se ve y lo que queda en sombra.

Composición: la lámpara descentrada a la izquierda, el laberinto se abre hacia la derecha como campo de interrogación.

Sin texto en la imagen.

Referencias estéticas: ilustración editorial contemporánea, minimalismo simbólico.

Evitar: texto ilegible, figuras humanas, estética de stock.
```

### Tema: esperanza / filosofía existencial
```
Imagen horizontal, proporción 1570:880, collage digital con textura de grabado.

Una grieta vertical en un muro oscuro por la que entra un haz de luz cálida. De la grieta brota una pequeña planta.

Paleta: gris-azulado oscuro dominante, luz dorada focal, verde apagado para la planta.

Ambiente melancólico pero con gesto afirmativo, sin sentimentalismo.

Composición: muro ocupa dos tercios, grieta vertical ligeramente a la derecha del centro, luz se proyecta hacia abajo a la izquierda.

Sin texto en la imagen.

Referencias estéticas: grabado simbolista, ilustración editorial sobria.

Evitar: estética inspiracional genérica, tonos saturados, texto motivacional.
```

### Tema: IPFS / tecnología descentralizada
```
Imagen horizontal, proporción 1570:880, estilo geométrico-abstracto.

Una red de nodos hexagonales interconectados que se expande desde el centro hacia los bordes. Algunos nodos están más luminosos, otros apagados, sugiriendo distribución no jerárquica.

Paleta: azul profundo de fondo, ámbar y blanco para los nodos activos.

Ambiente tecnológico pero con calidez humanista — no futurista frío.

Composición: red descentralizada, sin punto focal único, equilibrio visual entre nodos.

Texto en imagen: "mindandhealth.org" en tipografía sans-serif delicada, esquina inferior derecha.

Referencias estéticas: cubismo digital, ilustración conceptual editorial.

Evitar: estética de criptomonedas, neones, gráficos tipo stock tecnológico.
```

## Preguntas para personalizar el prompt

Antes de redactar el prompt, pregunta a Pablo (solo si no queda claro del artículo):

1. ¿Quieres **texto en la imagen**? Si sí, ¿qué texto y en qué idioma?
2. ¿Algún **símbolo o motivo** concreto que quieras que aparezca (siguiendo la metáfora orientadora del artículo)?
3. ¿**Paleta** preferida para esta pieza, o libre?
4. ¿**Registro visual**: ilustración / fotografía editorial / abstracto / collage / grabado?

Si Pablo dice "tú decide", elige según el tema y los ejemplos anteriores.

## Entrega

Entregar **solo el prompt**, en un bloque de código, listo para copiar/pegar. No generar variantes múltiples salvo que lo pida.
