# Changelog

All notable changes to `mindandhealth-publish` are documented here. This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- Translated the repository documentation, plugin metadata, command, skill instructions, examples, and bundled chat distribution into English.
- Repository instructions are in English, while Spanish remains the default language for conversations, canvases, derivatives, and image prompts. English or bilingual ES/EN output is available on request.
- Renamed Spanish internal guide filenames to English and updated all references.

## [1.2.0] — 2026-08-19

### Changed

- Renamed the chat variant to `mindandhealth-publish-chat`. The plugin variant remains `mindandhealth-publish`, preventing duplicate published skill names while preserving marketplace and `/publish` compatibility.
- Regenerated `mindandhealth-publish-claude-ai.zip` with an internal `mindandhealth-publish-chat/` folder.
- Added documentation for the two variants and updated the Mistral path.

### Migration

- **Claude.ai / Perplexity / Mistral:** uninstall the prior skill and upload the bundle again. It appears as `mindandhealth-publish-chat`; natural-language triggers are unchanged.
- **Claude Code:** no action required.

### Notes

- No behavior changes.
- The plugin and chat copies still differ where required by vault access. A future build script should generate the chat variant from the plugin source.

## [1.1.0] — 2026-06-10

### Added

- Mistral AI installation support through its **Work** space.

### Changed

- Shortened the chat variant's description to fit Mistral's 500-character limit and regenerated the bundle.
- Documented the Perplexity and Mistral description limits.

### Notes

- No skill behavior changes; the minor release reflects expanded platform support.

## [1.0.0] — Initial release

### Added

- Conversational editorial support for mindandhealth.org, including modes, LinkedIn derivatives, an image prompt, and a controlled-variation ethical footer. Released as both a Claude Code plugin and an uploadable chat skill.
