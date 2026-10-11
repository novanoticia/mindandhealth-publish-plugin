# Mode: pipeline (conversation → canvas → derivatives)

## Localized interface

Use `derivatives.confirm` for the mandatory approval question. Use `package.ready` and the applicable `package.article`, `package.image`, `package.newsletter`, `package.feed` keys for the final handoff, listing only outputs actually requested and produced. Use `remaining.heading` and the applicable `remaining.*` reminders. Read them from the selected catalog; English examples below do not override it.

## When to use it

At final handoff, include `remaining.review` to remind Pablo that final human editorial review is still required.

Pablo wants to complete the entire journey in one session: exploratory conversation, publishable article, LinkedIn newsletter, feed post, and image prompt.

## Critical reminder

**Everything stays in chat. No files on disk and no changes to the vault.**

## Steps

### 1. Classify the starting point

- a) **Only a topic or intuition** → start in `modes/converse.md` and let it crystallize.
- b) **Pablo's own draft** → start in `modes/refine.md`.
- c) **Source material** → start in `modes/transform.md`.

### 2. Run the initial phase

Following (a/b/c), use the relevant mode until there is a **stable canvas** (milestone 2 or 3 in `references/iterative-canvas-mode.md`).

**Mandatory pause before derivatives.** When the canvas is ready, ask explicitly:

> "The canvas is ready. Shall we move on to derivatives (LinkedIn newsletter / feed post / 1570:880 image prompt)? Which ones would you like?"

Do not proceed automatically.

### 3. Derivatives—fixed order

Once the canvas is approved and Pablo has confirmed the desired derivatives, produce them **in this order**:

1. **1570:880 image prompt** (`derivatives/banner-spec.md`)
   — first, so Pablo can commission it in parallel while reviewing the rest.

2. **LinkedIn newsletter** (`derivatives/linkedin-newsletter.md`)
   — a long-form adaptation of the article for the newsletter format.

3. **LinkedIn feed post** (`derivatives/linkedin-feed.md`)
   — the short version accompanying publication of the newsletter.

Deliver the three in **separate, clearly labeled blocks** in chat.

### 4. Final package

At the end, offer this summary:

```
Package ready:

1. OBSIDIAN ARTICLE (Markdown canvas above) — to copy to your vault
2. 1570:880 IMAGE PROMPT — to send to your generator
3. LINKEDIN NEWSLETTER — to copy into the newsletter editor
4. LINKEDIN FEED POST — to copy into the feed editor

Still to be done by you:
- Co-authorship YAML block (Tagger GPT)
- Final article tags (Obsidian template)
- Generated and embedded image
- Final human editorial review
```

## Anti-patterns

- ❌ Produce all four outputs without pausing for validation of the base canvas.
- ❌ Change tone between the article and its derivatives. The newsletter should sound like Pablo, not a generic LinkedIn post.
- ❌ Repeat entire article paragraphs verbatim in the newsletter—adapt them to the medium.
- ❌ Generate an image directly—the skill only produces the descriptive prompt.
- ❌ Skip exploratory conversation when Pablo arrives with "only a topic." Articles emerge; they are not commissioned.
- ❌ Write anything to a file. **Everything stays in chat.**
