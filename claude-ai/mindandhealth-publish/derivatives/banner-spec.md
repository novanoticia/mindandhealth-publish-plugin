# Derivative: 1570:880 image prompt

## Purpose

Generate a **descriptive prompt** Pablo can send to his usual image generator (DALL·E, Midjourney, Gemini, etc.). The skill **does not generate the image**; it only writes the prompt.

## Target image format

- **Aspect ratio:** 1570:880 (approximately 16:9, but exact for a LinkedIn newsletter banner).
- **Primary use:** LinkedIn newsletter cover.
- **Secondary use:** optional closing or opening image for the Obsidian article.
- It **may or may not contain text**; ask Pablo when unclear.

## Visual style observed in earlier images

Based on vault files such as `banneretico.png`, `index-portada.png`, `imagen_inicio.webp`, images for Juan Haro poems, and article illustrations:

- **Frequent palettes:** deep blue and warm amber; ochre and beige; black and white with a color accent.
- **Visual registers:**
  - Geometric abstraction / cubism (hexagons, fractals).
  - Flat vector illustration with texture.
  - Warm-toned editorial photography.
  - Symbolic collage (roots, voices, mazes).
- **Recurring symbols:** honeycombs/hexagons (collective intelligence), mazes, lamps, roots, fragments, cracks of light, trees.
- **Typography:** modern Gothic for main titles; clean sans serif for subtitles.

## Prompt template

```
Horizontal image, 1570:880 aspect ratio, [VISUAL STYLE].

[CENTRAL SUBJECT DESCRIPTION]—[the article's guiding symbol/metaphor].

[COLOR PALETTE]—[2–3 dominant colors and their distribution].

[MOOD / TONE]: [serene, reflective, dense, luminous, melancholy, restrained…].

[COMPOSITION]: [centered, asymmetric, visual mass on the left, low horizon, etc.].

[TEXT IN IMAGE]: [either "no text" or "include the text '[TEXT]' in modern Gothic type, [position]"]

Aesthetic references: [1–2 where useful, e.g. contemporary flat editorial illustration, digital engraving, warm-toned editorial photography].

Avoid: illegible text, generic stock imagery, distorted human features, excessive decoration.
```

## Examples by topic

### AI ethics / assisted thought

```
Horizontal image, 1570:880 aspect ratio, textured flat vector illustration.

An antique oil lamp suspended in the middle of a geometric maze extending toward the horizon. Its beam illuminates only part of the path.

Palette: deep blue (60% of the image), warm amber (illuminated area), off-white (maze details).

Serene and reflective, with latent tension between what is visible and what remains in shadow.

Composition: lamp off-center to the left; the maze opens toward the right like a field of questions.

No text.

Aesthetic references: contemporary editorial illustration, symbolic minimalism.

Avoid: illegible text, human figures, stock imagery.
```

### Hope / existential philosophy

```
Horizontal image, 1570:880 aspect ratio, digital collage with engraved texture.

A vertical crack in a dark wall lets through a warm beam of light. A small plant emerges from the crack.

Palette: dominant dark blue-gray, focused golden light, muted green for the plant.

Melancholy but quietly affirmative, without sentimentality.

Composition: wall occupies two thirds; the vertical crack sits just right of center; light falls down and to the left.

No text.

Aesthetic references: symbolist engraving, restrained editorial illustration.

Avoid: generic inspirational aesthetics, saturated colors, motivational text.
```

### IPFS / decentralized technology

```
Horizontal image, 1570:880 aspect ratio, geometric-abstract style.

A network of interconnected hexagonal nodes expands from the center toward the edges. Some nodes glow while others are dim, suggesting non-hierarchical distribution.

Palette: deep-blue background, amber and white active nodes.

Technological yet humanly warm—not cold futurism.

Composition: decentralized network with no single focal point; balanced visual weight among nodes.

Text: "mindandhealth.org" in delicate sans-serif type at the bottom right.

Aesthetic references: digital cubism, conceptual editorial illustration.

Avoid: cryptocurrency aesthetics, neon, generic technology stock graphics.
```

## Questions for customization

Ask Pablo only when the article does not make these clear:

1. Do you want **text in the image**? If so, what text and in which language?
2. Should a particular **symbol or motif** appear, following the article's guiding metaphor?
3. Is there a preferred **palette**, or should I choose freely?
4. Which **visual register**: illustration, editorial photography, abstract, collage, or engraving?

If Pablo says "you decide," choose based on the topic and examples above.

## Delivery

Return **only the prompt** in a code block, ready to copy and paste. Do not generate multiple variants unless requested.
