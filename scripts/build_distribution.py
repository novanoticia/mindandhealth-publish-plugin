#!/usr/bin/env python3
"""Validate packaging and build a reproducible chat ZIP using only Python's stdlib."""

import argparse
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/mindandhealth-publish"
CHAT = ROOT / "claude-ai/mindandhealth-publish"
ARCHIVE_NAME = "mindandhealth-publish-claude-ai.zip"


def manifest_outputs():
    """The portable manifest owns the shared metadata."""
    portable = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    claude = {key: value for key, value in portable.items()
              if key not in {"$schema", "repository"}}
    marketplace_path = ROOT / ".claude-plugin/marketplace.json"
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    if len(marketplace["plugins"]) != 1:
        raise ValueError("Expected one marketplace entry")
    entry = marketplace["plugins"][0]
    entry.update(name=portable["name"], version=portable["version"],
                 description=portable["description"], source="./plugins/mindandhealth-publish")
    return {
        PLUGIN / ".claude-plugin/plugin.json": claude,
        marketplace_path: marketplace,
    }


def sync_manifests():
    for path, content in manifest_outputs().items():
        path.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")


def validate():
    for path, expected in manifest_outputs().items():
        if json.loads(path.read_text(encoding="utf-8")) != expected:
            raise ValueError(f"Stale manifest: {path.relative_to(ROOT)}; run --sync-manifests")
    if (ROOT / ".claude-plugin/plugin.json").exists():
        raise ValueError("The marketplace root must not also declare a plugin")
    if not (PLUGIN / "commands/publish.md").is_file():
        raise ValueError("/publish must be inside the installed plugin")
    version = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))["version"]
    plugin_skill = PLUGIN / "skills/mindandhealth-publish"
    if f'version: "{version}"' not in (plugin_skill / "SKILL.md").read_text(encoding="utf-8"):
        raise ValueError("Plugin skill version differs from manifest")
    for root, name in [(plugin_skill, "mindandhealth-publish"),
                       (CHAT, "mindandhealth-publish-chat")]:
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        if not skill.startswith(f"---\nname: {name}\n"):
            raise ValueError(f"Unexpected skill name in {root}")
        for file in root.rglob("*.md"):
            for relative in re.findall(r"`((?:modes|references|derivatives)/[^`\s]+\.md)`",
                                       file.read_text(encoding="utf-8")):
                if not (root / relative).is_file():
                    raise ValueError(f"Broken reference in {file}: {relative}")
    header = (CHAT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
    description = header.split("description: >-", 1)[1].strip()
    description = " ".join(line.strip() for line in description.splitlines())
    if len(description) > 500 or len(description.encode("utf-8")) > 1024:
        raise ValueError("Chat description exceeds platform limits")


def build(output_dir):
    validate()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / ARCHIVE_NAME
    # Fixed timestamps, permissions, and ordering make repeat builds identical.
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(CHAT.rglob("*.md")):
            relative = path.relative_to(CHAT).as_posix()
            info = zipfile.ZipInfo(f"mindandhealth-publish-chat/{relative}",
                                   date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, path.read_bytes())
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync-manifests", action="store_true",
                        help="Refresh Claude and marketplace metadata from plugin.json")
    parser.add_argument("--check", action="store_true", help="Validate without creating a ZIP")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    if args.sync_manifests:
        sync_manifests()
    if args.check:
        validate()
        print("Packaging validation passed.")
    else:
        print(build(args.output_dir))


if __name__ == "__main__":
    main()
