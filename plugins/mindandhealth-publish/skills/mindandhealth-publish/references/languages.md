# Output languages

## Selection and persistence

1. Start in **Spanish (es)** unless Pablo explicitly selects another language.
2. Support **English (en)**, **French (fr)**, and **Simplified Chinese (zh-CN)** on request. Recognize the request in any of these languages.
3. Keep the selected language across conversation, outlines, canvases, revisions, ethical footers, newsletters, feed posts, and image prompts until Pablo changes it.
4. A source quotation, URL, English example, translated README, or topic about another country does not change the selected language.
5. For bilingual work, confirm the two languages and their order. Never silently add a second language.
6. If a requested language is unclear, ask one short question in the current language.

## Catalog loading

Read `i18n/README.md` and then `i18n/es.json` (default), `i18n/en.json`, `i18n/fr.json`, or `i18n/zh-CN.json` according to the explicit selection. Read the new catalog whenever the selected language changes. For bilingual output, load both requested catalogs.

Use the fixed-message keys specified by the active mode; do not translate their English examples ad hoc. For unsupported or ambiguous requests, use `language.unknown` or `language.pair` in the current supported language. If the selected catalog cannot be used, switch the complete response to Spanish and emit `language.unavailable` from `i18n/es.json`. If Spanish is unavailable too, stop as specified in `i18n/README.md`.

These files contain fixed prompts and labels, not full translations of the skill. Translation review status is recorded in `i18n/STATUS.md`; terminology lives in `i18n/GLOSSARY.md`.

## Generated content

Translate headings, explanations, editorial feedback, article text, image-prompt instructions, and free-text frontmatter fields such as title and subtitle. Adapt tone naturally; French and Chinese should preserve Pablo's reflective voice, nuance, and ethical attribution rather than copy English sentence structure.

For Simplified Chinese, use simplified characters and natural Chinese punctuation. Word-count ranges in English examples are approximate editorial lengths, not Chinese character counts; agree on a suitable character count when length matters.

For French, use natural French typography and idiom. Avoid unnecessary English jargon in French and Spanish prose.

## What to preserve

- Skill names, slash commands, paths, URL slugs, DOI identifiers, tool names, and proper names.
- YAML keys, controlled values such as `tipo: articulo`, and the site's existing tag taxonomy.
- Verbatim quotations and their original attribution. Label a translated quotation as a translation; do not pass it off as the original.
- The meaning of ethical safeguards: human editorial responsibility, disclosed AI assistance, manifesto link, and relevant professional-advice clauses.
- All permission boundaries: language choice never authorizes publication, vault writes, image generation, or unsolicited canvas edits.

The examples in other guides are structural and tonal references, not instructions to switch to English.

## Example requests

| Language | Request | Expected behavior |
|---|---|---|
| Español | «Sigamos en español y preparemos la newsletter.» | Spanish conversation and newsletter. |
| English | “Continue in English and help me refine this draft.” | English diagnosis, then English edits at the agreed depth. |
| Français | «Continuons en français et préparons la newsletter.» | French conversation and newsletter; keep French in later turns. |
| 简体中文 | “请用简体中文继续，帮我润色这篇草稿。” | Simplified Chinese diagnosis and editing; keep the chosen edit depth. |
| Bilingual | «Prepara una versión bilingüe en francés y chino simplificado, primero francés.» | Separate French and Simplified Chinese sections in the requested order. |

## Editorial terminology

| Español | English | Français | 简体中文 |
|---|---|---|---|
| Conversación exploratoria | Exploratory conversation | Conversation exploratoire | 探索性对话 |
| Canvas / borrador en el chat | Canvas / in-chat draft | Canevas / brouillon dans le chat | 对话中的草稿 |
| Disidencia útil | Useful dissent | Désaccord constructif | 建设性异议 |
| Pie ético | Ethical footer | Note éthique finale | 文末伦理声明 |
| Juicio editorial humano | Human editorial judgment | Jugement éditorial humain | 人类编辑判断 |
| Petición | Request | Demande | 修改请求 |
| Sugerencia aprobada | Approved suggestion | Suggestion approuvée | 已获批准的建议 |

## Acceptance scenarios

- With no language request, answer in Spanish even when source material is French or Chinese.
- After “Continuons en français”, write the next canvas and its ethical footer in French. A later “change section 2” does not switch back to English.
- After “请用简体中文继续”, write the diagnosis, canvas, footer, and requested derivatives in Simplified Chinese.
- Preserve `tipo: articulo` and verified URLs in all four languages; localize the article title.
- A French question about a canvas receives a conversational answer in the selected language without rewriting the canvas.
- Switching languages does not automatically translate or replace an already approved canvas; ask or wait for an explicit editing request.

