"""Catalog contracts and negative tests; these do not evaluate model behavior."""

import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_i18n import (
    CANONICAL, CHAT, placeholders, read_catalog, validate_catalogs, validate_distribution,
)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.catalogs = Path(self.temp.name) / "i18n"
        shutil.copytree(CANONICAL, self.catalogs)

    def mutate(self, locale, update):
        path = self.catalogs / f"{locale}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        update(data)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_complete_catalogs_and_chat_parity(self):
        self.assertEqual(validate_distribution(), {"es", "en", "fr", "zh-CN"})
        for path in CANONICAL.iterdir():
            self.assertEqual(path.read_bytes(), (CHAT / path.name).read_bytes())

    def test_missing_key_fails(self):
        self.mutate("fr", lambda data: data["messages"].pop("canvas.offer"))
        with self.assertRaisesRegex(ValueError, "key parity"):
            validate_catalogs(self.catalogs)

    def test_extra_key_fails(self):
        self.mutate("en", lambda data: data["messages"].update(unexpected="Extra text"))
        with self.assertRaisesRegex(ValueError, "key parity"):
            validate_catalogs(self.catalogs)

    def test_changed_placeholder_fails(self):
        self.mutate("zh-CN", lambda data: data["messages"].update(
            {"canvas.confirm": data["messages"]["canvas.confirm"].replace("{length}", "{words}")}))
        with self.assertRaisesRegex(ValueError, "placeholder mismatch"):
            validate_catalogs(self.catalogs)

    def test_source_change_invalidates_translations(self):
        self.mutate("es", lambda data: data["messages"].update(
            {"conversation.open": "¿Qué te gustaría explorar hoy?"}))
        with self.assertRaisesRegex(ValueError, "stale source fingerprint"):
            validate_catalogs(self.catalogs)

    def test_missing_technical_literal_fails(self):
        self.mutate("fr", lambda data: data["messages"].update(
            {"package.image": data["messages"]["package.image"].replace("1570:880", "16:9")}))
        with self.assertRaisesRegex(ValueError, "missing invariant"):
            validate_catalogs(self.catalogs)

    def test_human_review_cannot_be_claimed_without_reviewer(self):
        self.mutate("en", lambda data: data["_meta"].update(status="reviewed", reviewed_by=None))
        with self.assertRaisesRegex(ValueError, "named human reviewer"):
            validate_catalogs(self.catalogs)

    def test_empty_translation_fails(self):
        self.mutate("fr", lambda data: data["messages"].update({"canvas.updated": " "}))
        with self.assertRaisesRegex(ValueError, "empty or non-string"):
            validate_catalogs(self.catalogs)

    def test_duplicate_json_keys_fail(self):
        path = self.catalogs / "en.json"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace('"locale": "en",', '"locale": "en", "locale": "fr",', 1),
                        encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            read_catalog(path)

    def test_non_nfc_translation_fails(self):
        self.mutate("fr", lambda data: data["messages"].update({"canvas.updated": "Cafe\u0301"}))
        with self.assertRaisesRegex(ValueError, "Unicode NFC"):
            read_catalog(self.catalogs / "fr.json")

    def test_named_fields_only(self):
        for invalid in ("{}", "{0}", "{user.name}", "{text!r}", "{count:02d}"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                placeholders(invalid)

    def test_catalog_keys_are_connected_to_instructions(self):
        root = CANONICAL.parent
        paths = [root / "references/languages.md"]
        paths += list((root / "modes").glob("*.md"))
        paths += [root / "references/iterative-canvas-mode.md", root / "i18n/README.md"]
        instructions = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        for key in read_catalog(CANONICAL / "es.json")["messages"]:
            if key == "language.no_default":
                continue  # The same Spanish emergency text is embedded for unreadable catalogs.
            self.assertTrue(f"`{key}`" in instructions, f"Unconnected catalog key: {key}")

    def test_recorded_fingerprint_is_full_source_hash(self):
        digest = hashlib.sha256((CANONICAL / "es.json").read_bytes()).hexdigest()
        for locale in ("en", "fr", "zh-CN"):
            self.assertEqual(read_catalog(CANONICAL / f"{locale}.json")["_meta"]["source_sha256"],
                             digest)


if __name__ == "__main__":
    unittest.main()
