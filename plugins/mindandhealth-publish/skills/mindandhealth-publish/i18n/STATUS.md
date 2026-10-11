# Translation status

As of 2026-10-11, version 1.3.1:

| Locale | Coverage | Status | Prepared by | Human reviewer |
|---|---|---|---|---|
| es | All fixed-text keys; canonical source | reference | OpenAI Codex, consolidated for this workflow | None recorded |
| en | All Spanish keys and placeholders | ai-draft | OpenAI Codex | None |
| fr | All Spanish keys and placeholders | ai-draft | OpenAI Codex | None |
| zh-CN | All Spanish keys and placeholders | ai-draft | OpenAI Codex | None |

The Spanish catalog is the normative fixed-text reference, not a claim of human review. Its creation consolidates the workflow's interface messages; it is not a byte-for-byte extraction of earlier output.

Automated checks verify key coverage, placeholders, source fingerprints, encoding, and packaging. They do not assess translation accuracy, naturalness, or real platform behavior. No locale is labeled human-reviewed.

README.fr.md and README.zh-CN.md are user guides authored with AI assistance; no human linguistic review has been recorded. They are not full translations of every skill instruction.

Still requiring manual evaluation: language selection and persistence on the target chat platforms; French editorial idiom; Simplified Chinese editorial terminology and character-count expectations. Use the scenarios in references/languages.md and tests/i18n-scenarios.md.
