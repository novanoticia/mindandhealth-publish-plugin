"""Integration checks for the installable plugin and generated chat package."""

from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.build_distribution import CHAT, PLUGIN, ROOT, build, validate


class DistributionTests(unittest.TestCase):
    def test_installation_layout(self):
        validate()
        command = (PLUGIN / "commands/publish.md").read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/skills/mindandhealth-publish/SKILL.md", command)
        self.assertFalse((ROOT / "commands/publish.md").exists())

    def test_bundle_matches_chat_source_exactly(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build(Path(directory))
            with zipfile.ZipFile(archive) as bundle:
                expected = {
                    "mindandhealth-publish-chat/" + p.relative_to(CHAT).as_posix(): p.read_bytes()
                    for p in CHAT.rglob("*.md")
                }
                self.assertEqual(set(bundle.namelist()), set(expected))
                for name, data in expected.items():
                    self.assertEqual(bundle.read(name), data, name)
                self.assertIsNone(bundle.testzip())

    def test_build_is_reproducible(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = build(Path(directory))
            original = archive.read_bytes()
            self.assertEqual(build(Path(directory)).read_bytes(), original)

    def test_language_policy_is_shared_and_included(self):
        relative = "references/languages.md"
        canonical = PLUGIN / "skills/mindandhealth-publish" / relative
        self.assertEqual(canonical.read_bytes(), (CHAT / relative).read_bytes())
        for language in ("Spanish", "English", "French", "Simplified Chinese"):
            self.assertIn(language, canonical.read_text(encoding="utf-8"))
        for root in (PLUGIN / "skills/mindandhealth-publish", CHAT):
            self.assertIn(relative, (root / "SKILL.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
