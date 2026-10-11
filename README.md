# mindandhealth-publish-plugin

[English](README.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md)

A Claude Code plugin providing **conversational editorial support** for [mindandhealth.org](https://mindandhealth.org) publications on Obsidian Publish.

> **Compatible with [Agent Plugins 1.0.0](https://agent-plugins.org/specification)**, the portable packaging format of the Agentic AI Foundation. The package contains a portable `plugin.json` manifest and an Agent Skills-compatible `SKILL.md`.
>
> **Also works in ChatGPT.** The skill consists only of instructions and editorial criteria, with no local execution. Add it from **Plugins** after enabling **Work** in the ChatGPT selector. It is also available on the free plan, subject to usage limits.

This is not an automatic article writer. It is a thinking partner: it converses first, distills an article when the idea crystallizes, and creates LinkedIn or image-prompt derivatives on request. **Everything stays in chat; the vault is never modified.**

The skill instructions are written in English, but the **default output language is Spanish**. Request English, French, Simplified Chinese, or bilingual output explicitly; the skill keeps that choice until you change it. Source language and README language do not change this default. See the [language guide](plugins/mindandhealth-publish/skills/mindandhealth-publish/references/languages.md).

## Mental model

Pablo's articles **are not commissioned; they emerge**:

1. **Exploratory conversation** (default mode). A topic, intuition, doubt, or reading is examined from different perspectives. The assistant is a thinking partner, not a writer.
2. **Crystallization.** Pablo asks for a canvas, or the assistant suggests one once when enough material has emerged.
3. **Canvas.** A living Markdown block in chat containing what the conversation has distilled. It is not a disk file.
4. **Iteration.** Pablo comments, requests, and suggests. The canvas changes only for direct requests and approved suggestions.
5. **Closure.** Pablo manually copies the final canvas to his Obsidian vault. Derivatives can then be generated.

## What it never does

- Write to the vault or any file on disk.
- Use editing tools to save drafts.
- Generate the final `🔖 **Tags:**` block; Pablo's Obsidian template adds it.
- Generate the co-authorship YAML block; Pablo's Tagger GPT adds it.
- Generate images; it produces descriptive prompts only.
- Publish anything.
- Rush into drafting during the opening stages of a conversation.

## What it does

- Converses as a transdisciplinary thinking partner, offering perspective, counterargument, references, metaphors, and questions.
- Opens an Obsidian-compatible Markdown canvas, with minimal YAML and an ethical footer, after the idea crystallizes.
- Iterates the canvas through a clear conversational protocol.
- Creates a LinkedIn newsletter, LinkedIn feed post, and 1570:880 image prompt on request.
- In the Claude Code variant, reads the vault when asked to propose verified internal links.

## Two variants

| Variant | Path | `name` | Environment |
|---|---|---|---|
| Plugin | `plugins/mindandhealth-publish/skills/mindandhealth-publish/` | `mindandhealth-publish` | Claude Code / Claude Desktop Code. Can read the vault and provides `/publish`. |
| Chat | `claude-ai/mindandhealth-publish/` and the `.zip` bundle | `mindandhealth-publish-chat` | Claude.ai, Perplexity, Mistral, and ChatGPT. No disk access; source material must be supplied in chat. |

Do not install both variants in the same environment: they serve the same purpose and their triggers may overlap.

## Installation

### Claude Code and Claude Desktop Code

Add the marketplace and install the plugin:

```bash
/plugin marketplace add novanoticia/mindandhealth-publish-plugin
/plugin install mindandhealth-publish@mindandhealth-publish-plugin
```

This enables the `/publish` command and natural-language triggers.

### Claude.ai

1. Download [`mindandhealth-publish-claude-ai.zip` from Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest/download/mindandhealth-publish-claude-ai.zip). Its readable source is in [`claude-ai/mindandhealth-publish/`](./claude-ai/mindandhealth-publish/).
2. In Claude.ai, open your avatar → **Settings** → **Capabilities** → **Skills** → **Upload skill**.
3. Upload the ZIP and enable the skill.

Invoke it in natural language: "let's publish something about X," "open a canvas," or "make a newsletter from the latest article."

> Custom skills require a **Max**, **Team**, or **Enterprise** plan with Skills enabled.

### Perplexity

1. Download [`mindandhealth-publish-claude-ai.zip` from Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest/download/mindandhealth-publish-claude-ai.zip).
2. Open **Skills** management and choose **Upload / Import skill**.
3. Upload the ZIP and activate it.

### Mistral AI

1. Download and extract [`mindandhealth-publish-claude-ai.zip` from Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases/latest/download/mindandhealth-publish-claude-ai.zip).
2. In the Mistral **Work** space, open **Skills**.
3. Select the extracted `mindandhealth-publish-chat/` folder containing `SKILL.md`.

> **Description limits:** Perplexity validates the field as UTF-8 bytes with a 1,024-byte limit; Mistral imposes a 500-character limit. Keep the chat variant's description below 500 characters.

## Usage

### Slash command

```text
/publish [optional context]
```

- **No argument** → enter converse mode and ask what Pablo brings today.
- **Topic / intuition / open question** → begin a conversation without imposing a structure.
- **Pasted draft** → enter refine mode, starting with a brief diagnosis.
- **URL / quotation / source material** → enter transform mode, starting with a source inventory.
- **Explicit request** → go directly to the relevant canvas or derivative mode.

Natural-language examples:

- "Let's think about X."
- "This idea has been on my mind."
- "What do you think about…?"
- "Help me polish this draft."
- "Open a canvas from our discussion."
- "Make a newsletter from the latest article."
- "Give me an image prompt for this post."

To select another output language:

- «Continuons en français et préparons la newsletter.»
- “请用简体中文继续，帮我润色这篇草稿。”
- “Continue in English.”
- «Volvamos al español.»

Changing the language does not automatically rewrite an already approved canvas.

## Canvas iteration protocol

| Lane | Signal | Response |
|---|---|---|
| **Question** | "What do you think of §2?" | Answer in chat; do not re-edit the canvas. |
| **Suggestion** | "What if…?" | Evaluate it; if approved, apply it and return the canvas. |
| **Request** | "Change X" | Apply it and return the canvas with a brief diff. |
| **Exploration** | "Give me three openings" | Offer variants in chat without changing the canvas. |
| **Parallel conversation** | "By the way…" | Return to converse mode without closing the canvas. |
| **Validation** | "Leave it like that" | Fix the state and suggest the next milestone. |
| **Pause** | "Let me think about it" | Report the state and stop. |

Only **Request** and **Approved suggestion** return an updated canvas.

## Editorial principles

1. **Transdisciplinarity.** Connect technology and the humanities.
2. **Epistemic honesty.** Preserve uncertainty and provisional choices.
3. **Active nuance.** Include useful dissent and productive tension; avoid dogmatism.
4. **Guiding metaphor.** Use a concrete, sensory, restrained metaphor when appropriate.
5. **Reflective ending.** End with an open question or small gesture, not a closed conclusion.
6. **Ethical footer.** Always place a freshly written footer at the end of the article body.
7. **In-chat canvas.** Never save it to disk.

## Architecture

```text
mindandhealth-publish-plugin/
├── plugins/mindandhealth-publish/       # Claude Code variant
│   ├── plugin.json                     # Canonical shared metadata (portable format)
│   ├── .claude-plugin/plugin.json      # Claude-compatible manifest, synchronized
│   ├── commands/publish.md             # Installed /publish command
│   └── skills/mindandhealth-publish/
│       ├── SKILL.md                     # Orchestrator and flow
│       ├── modes/
│       │   ├── converse.md                 # Default mode
│       │   ├── generate.md                 # Initial canvas
│       │   ├── refine.md                   # Polish a supplied draft
│       │   ├── transform.md                # Canvas from source material
│       │   └── pipeline.md                 # Full journey
│       ├── references/
│       │   ├── editorial-voice.md
│       │   ├── languages.md
│       │   ├── yaml-structure.md
│       │   ├── ethical-footer.md
│       │   ├── topic-map.md
│       │   └── iterative-canvas-mode.md
│       └── derivatives/
│           ├── linkedin-newsletter.md
│           ├── linkedin-feed.md
│           └── banner-spec.md
├── claude-ai/mindandhealth-publish/     # Chat variant
├── README.fr.md                        # French documentation
├── README.zh-CN.md                     # Simplified Chinese documentation
├── scripts/build_distribution.py       # Validation and reproducible ZIP build
├── .github/workflows/distribution.yml  # CI and release packaging
└── .claude-plugin/marketplace.json      # Marketplace manifest
```

The root `.claude-plugin/` directory describes the **marketplace**, not a second plugin. Its catalog points to `plugins/mindandhealth-publish/`, the only installable plugin directory. Within that directory, `plugin.json` serves portable Agent Plugins clients, while `.claude-plugin/plugin.json` serves Claude. Both are required for compatibility; shared metadata is authored only in the portable manifest.

The chat directory is a separate distribution for clients without local vault access. It retains a distinct skill name and instructions appropriate to that environment.

## Building and releasing

The ZIP is a **release asset**, not a file on `main`. Download it from [Releases](https://github.com/novanoticia/mindandhealth-publish-plugin/releases), or build it locally with Python 3.10+:

```bash
python3 scripts/build_distribution.py
```

This creates `dist/mindandhealth-publish-claude-ai.zip`. The `dist/` directory is ignored by Git. The archive contains the `mindandhealth-publish-chat/` folder and all its guides; identical sources produce identical archives.

After changing shared metadata in `plugins/mindandhealth-publish/plugin.json`, synchronize the compatibility manifests:

```bash
python3 scripts/build_distribution.py --sync-manifests --check
python3 -m unittest discover -s tests -v
```

Keep the plugin skill's version aligned with the portable manifest. For a release, add matching notes in `docs/releases/<version>.md` and push a `v<version>` tag. GitHub Actions validates the package, builds the ZIP, and attaches it to the release. Ordinary pushes validate the same package and retain a downloadable Actions artifact.

Older tracked ZIPs remain recoverable from Git history; removing the current copy does not rewrite history.

## Vault access (Claude Code only)

The plugin may **read** Markdown files in the vault to extract patterns, propose internal links, or verify citations. The default path is:

```text
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Pablo's Vault/website/
```

Change it in `plugins/mindandhealth-publish/skills/mindandhealth-publish/references/topic-map.md`. The plugin **never writes to this path**.

## Available derivatives

- **LinkedIn newsletter**—extended adaptation with its own opening.
- **LinkedIn feed post**—short version derived from the newsletter.
- **1570:880 image prompt**—banner description only; it does not generate an image.

## Author

**Pablo Rodríguez López** — [mindandhealth.org](https://mindandhealth.org)

## License

Apache-2.0
