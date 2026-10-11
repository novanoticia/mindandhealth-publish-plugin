# Mode: refine (Pablo's draft → polished canvas)

## Localized interface

Use `refine.diagnosis`, `refine.level`, and `refine.log` from the selected catalog for the diagnosis heading, editing-depth question, and optional editorial log. Write the actual diagnosis and log entries freshly in the selected language.

## When to use it

Pablo already has a draft—his own or produced by another AI—and wants to polish it for publication. He pastes or shares it in chat.

## Critical reminder

**The canvas is a Markdown block in chat. I do not write to the vault or create files.** When refinement is complete, Pablo manually copies the canvas into Obsidian.

## Steps

### 1. Read the entire draft before suggesting anything

Do not begin with line edits. First identify:

- **Central thesis.** Is it clear and introduced early enough?
- **Voice.** Does it sound like Pablo or generic prose? Compare with `references/editorial-voice.md`.
- **Structure.** Do the sections flow? Does it need a stronger opening or a resonant ending?
- **Nuance.** Is there *useful dissent*, or does everything point one way?
- **Metaphor.** Is there a guiding one? Is it concrete or abstract?
- **Ethical footer.** Is it present and is it the correct variant?
- **YAML.** Is there frontmatter? Are the tags reasonable?

### 2. Give a brief diagnosis before rewriting

Offer 5–8 points covering what works, what falters, and what is missing:

```
Diagnosis:
- Opening: the question works, but it needs more room to breathe (I suggest a blockquote).
- Section 2: the thesis tangles two ideas; I would separate them.
- Register: at times it becomes too technical and loses its humanistic thread (see §4).
- Missing: a clear guiding metaphor; possible option: [proposal].
- Missing: ethical footer.
- Internal links: none; [X] and [Y] might fit.
```

### 3. Ask how ambitious the edit should be

- **Light:** preserve the voice; polish rhythm, punctuation, and repetition.
- **Medium:** reorganize sections, rewrite openings/endings, add nuance.
- **Deep:** restructure and rewrite substantial sections.

Pablo chooses the level. **Do not assume a deep edit** without an explicit request.

### 4. Open the polished canvas

Return the full canvas as a Markdown block. Preserve Pablo's original YAML when present; suggest additions or corrections rather than replacing it.

Verify that any proposed internal-link files exist in the vault.

### 5. Editorial decision log (optional)

After a medium or deep edit, offer an editorial decision log:

```
**Editorial decision log**
- Rewrote the opening to bring the thesis into the first third.
- Added the oak-and-reed metaphor in §3.
- Split §2 into 2a (diagnosis) and 2b (nuance) for clarity.
- Standardized italics (internal quotations only, not emphasis).
```

### 6. Iterate

From here, use the lane protocol in `references/iterative-canvas-mode.md`.

## Anti-patterns

- ❌ Rewrite everything without asking for the editing level.
- ❌ Erase Pablo's voice by "improving" it into neutral explanatory prose.
- ❌ Remove doubts, nuances, "I suspect," or "I am left with the question"—these are part of his signature.
- ❌ Replace his metaphor with a "better" one without an explicit request.
- ❌ Write the canvas to a file. **Never.**
