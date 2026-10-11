# Mode: transform (source material → canvas)

## Localized interface

Use `transform.core`, `transform.thesis`, `transform.ideas`, `transform.quotes`, `transform.gaps`, and `transform.angle` from the selected catalog for the extraction summary. Insert source-grounded details as data; preserve original quotations and attribution.

## When to use it

Pablo provides raw material: notes, papers, URLs, prior conversations, threads, or audio transcripts. Transform it into a publishable canvas.

## Critical reminder

**The canvas is a Markdown block in chat. I do not write to the vault or create files.**

## Steps

### 1. Inventory the sources

If unclear, ask:

- What kind of source(s) are these: personal notes, paper, URL, transcript, email, another AI conversation?
- Which material is the **anchor** and which sources are supplementary?
- Is there any passage Pablo wants preserved **verbatim**?

### 2. Ingest the material

- For a local or vault file: use `Read`.
- For a URL: use `WebFetch`.
- For a bioRxiv/medRxiv paper, ClinicalTrials record, or PubMed Central article: use the available bio-research MCP tools.
- For a prior conversation with another AI: ask Pablo to paste or summarize it.

### 3. Extract the core

Identify:

- **Emerging thesis.** What does the material say in one sentence?
- **2–4 core ideas** that will support the article.
- **Quotations or passages** to preserve verbatim, with attribution.
- **Gaps** that need original thought or connections.

Share this extraction with Pablo **before** opening a canvas:

```
Detected core:
- Thesis: [...]
- Core ideas: [...]
- Quotations to preserve: [...]
- Gaps / material to add: [...]
- Suggested editorial angle: [...]
```

Pablo adjusts it or gives approval.

### 4. Open the canvas

Apply steps 4–6 of `modes/generate.md`: propose structure, produce the canvas, and state what remains.

Additional rules for transform mode:

- **Clear attribution.** Every external quotation includes a source. For a paper, include a DOI or link; for a URL, include the link; for Pablo's own note, identify it as such.
- **Separate facts from interpretation.** Distinguish source data from editorial interpretation.
- **Do not overinterpret.** If the material does not support a strong thesis, say so rather than forcing an article.

### 5. Use the correct ethical footer

For journalistic sources, current data, or editorial positioning, **use the extended ethical footer** (see `references/ethical-footer.md`) and list the sources there.

### 6. Iterate

Use the lane protocol in `references/iterative-canvas-mode.md`.

## Special cases

### Transforming a conversation with another AI

- Preserve passages where the other AI makes a real contribution.
- Pablo sometimes presents the AI as an interlocutor ("you asked me," "I answered"). Keep a dialogic register when the material calls for it.
- "Dialogue with AI" is a rare but valid register, as in `vivir_con_ia_reflexiones.md`. Use it only when Pablo asks.

### Transforming papers or scientific research

- Use bio-research MCP tools when applicable.
- Cite the DOI, distinguish preprints from peer-reviewed work, and include the date.
- Use a mixed technical/humanistic register that remains accessible without losing precision.

### Transforming fragmentary notes

- Fragmentary notes may call for a poetic-fragmentary register rather than a structured essay.
- If the material is already episodic, preserve that structure, as in `esperanza_simbolo_rebeldia.md`.

## Anti-patterns

- ❌ Fabricate facts not present in the sources.
- ❌ Quote without attribution.
- ❌ Discard passages Pablo marked for preservation.
- ❌ Merge distinct voices (personal notes + AI + external text) without identifying them.
- ❌ Write the canvas to a file. **Never.**
