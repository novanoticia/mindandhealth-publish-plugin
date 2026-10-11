# Mode: generate (initial canvas draft)

## When to use it

Open a **canvas for the first time**, typically because:

- An exploratory conversation has crystallized and Pablo has agreed to open a canvas.
- Pablo directly asks to "open a canvas about X," skipping the prior conversation.

## Critical reminder

**The canvas is a Markdown block in chat. Never a file on disk. Never in the vault.** See `references/iterative-canvas-mode.md`.

## Steps

### 1. Confirm the form before drafting

When the idea crystallizes (or Pablo asks directly for a canvas), briefly confirm:

- **Register:** canonical (H2 essay) / poetic / fragmentary / dialogue / manifesto.
- **Approximate length:** short (<800) / medium (800–2000) / long (>2000).
- **Bilingual ES/EN:** only when the topic calls for it (Spanish by default).

If a long conversation already makes the register and length obvious, **propose and confirm them in one line** rather than opening an interview:

> "Voy a abrir un canvas de extensión media en registro canónico (unas 1.200 palabras), en español. ¿Te parece, o ajustamos?"

### 2. Distill the conversation

Before drafting, identify:

- **Emerging thesis** (one sentence).
- **Core ideas** (3–4).
- **Metaphors or images** that circulated.
- **Quotations or references** Pablo mentioned and wants preserved.
- **Productive disagreements** that could supply the article's useful dissent.
- **Discarded directions** that should not be proposed again.

### 3. Read the vault for internal links (optional)

Before drafting, perform a quick read-only search with Grep/Glob in the configured vault path (see `references/topic-map.md`). Identify 2–4 related articles that could be suggested as internal links.

### 4. Propose a structure

Before producing the full canvas, present a **short outline** (6–10 lines):

```
Working title: ...
Guiding metaphor: ... (or: no explicit metaphor)
Structure:
  - Opening (epigraph / blockquote / question)
  - H2 1: ...
  - H2 2: ...
  - H2 3: ...
  - Reflective ending
Suggested internal links: ... (2–4 vault articles)
```

Wait for Pablo's approval or adjustments. **This prevents major rewrites.**

### 5. Produce the canvas

Return the complete canvas as a Markdown block:

````
```markdown
---
title: "..."
subtitle: "..."
autor: "Pablo Rodríguez López & AI (model)"
proyecto: "mindandhealth.org"
tipo: "articulo"
estado: "borrador - pendiente revision humana"
fecha: "YYYY-MM-DD"
canales:
  - web
tags:
  - tag1
  - tag2
# --- co-authorship block goes here (Pablo adds it with Tagger) ---
---

[article body]

[ethical footer]
```
````

Follow:

- `references/editorial-voice.md` precisely.
- `references/yaml-structure.md` for frontmatter.
- `references/ethical-footer.md` for the appropriate disclaimer.
- At least one moment of *useful dissent*, unless the register is poetic-fragmentary.
- A recurring guiding metaphor if one was agreed.
- An ending that resonates rather than concludes.

### 6. State what remains

After the Markdown block, say:

```
This canvas is a first draft. It still needs iteration.

When you copy it to your vault, remember to add:
- The co-authorship YAML block (with your Tagger GPT).
- Formatted final tags (Obsidian template).
- An image, if you choose to include one (I can provide a 1570:880 prompt on request).

Would you like to refine something, or let it rest?
```

### 7. Enter iteration mode

From here, apply the lane protocol in `references/iterative-canvas-mode.md`. Do not produce new versions unless the lane is **Request** or **Approved suggestion**.

## Anti-patterns

- ❌ Write the entire canvas before the preliminary outline in step 4.
- ❌ Force a metaphor that does not fit the topic or conversation.
- ❌ Lose fragments, quotations, or nuances from the prior conversation.
- ❌ Use clichés such as "in this article we will explore…" or "in conclusion…".
- ❌ Invent quotations or references. Use only verifiable claims or clearly identified paraphrases.
- ❌ Invent internal links—verify them in the vault first.
- ❌ Save the canvas to disk. **Never.**
