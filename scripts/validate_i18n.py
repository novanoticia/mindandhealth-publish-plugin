"""Validate fixed-text catalogs; no third-party dependencies or model calls."""

import hashlib
import json
from pathlib import Path
import re
from string import Formatter
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "plugins/mindandhealth-publish/skills/mindandhealth-publish/i18n"
CHAT = ROOT / "claude-ai/mindandhealth-publish/i18n"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_catalog(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    if text.startswith("\ufeff") or not text.endswith("\n"):
        raise ValueError(f"{path.name}: expected UTF-8 without BOM and a final newline")
    if unicodedata.normalize("NFC", text) != text:
        raise ValueError(f"{path.name}: expected Unicode NFC")
    data = json.loads(text, object_pairs_hook=unique_object)
    if set(data) != {"_meta", "messages"}:
        raise ValueError(f"{path.name}: unexpected catalog structure")
    if not isinstance(data["_meta"], dict) or not isinstance(data["messages"], dict):
        raise ValueError(f"{path.name}: metadata and messages must be objects")
    if data["_meta"].get("locale") != path.stem:
        raise ValueError(f"{path.name}: locale must match filename")
    if not data["messages"]:
        raise ValueError(f"{path.name}: empty catalog")
    for key, value in data["messages"].items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path.name}: empty or non-string message {key}")
        placeholders(value)
    return data


def placeholders(message):
    fields = set()
    for _, field, spec, conversion in Formatter().parse(message):
        if field is None:
            continue
        if not re.fullmatch(r"[a-z][a-z_]*", field) or spec or conversion:
            raise ValueError(f"Only simple named placeholders are allowed: {field}")
        fields.add(field)
    return fields


def validate_catalogs(directory=CANONICAL):
    source = read_catalog(directory / "es.json")
    if source["_meta"].get("status") != "reference":
        raise ValueError("Spanish must be the reference catalog")
    digest = hashlib.sha256((directory / "es.json").read_bytes()).hexdigest()
    paths = sorted(directory.glob("*.json"))
    for path in paths:
        data = read_catalog(path)
        if data["messages"].keys() != source["messages"].keys():
            raise ValueError(f"{path.name}: key parity differs from Spanish")
        for key, value in data["messages"].items():
            if placeholders(value) != placeholders(source["messages"][key]):
                raise ValueError(f"{path.name}: placeholder mismatch for {key}")
            # These literals are technical contracts, not translatable text.
            for token in ("1570:880", "YAML", "Tagger GPT", "Obsidian"):
                if token in source["messages"][key] and token not in value:
                    raise ValueError(f"{path.name}: missing invariant {token} in {key}")
        if path.stem == "es":
            continue
        meta = data["_meta"]
        if meta.get("source") != "es.json" or meta.get("source_sha256") != digest:
            raise ValueError(f"{path.name}: stale source fingerprint; review the translation")
        if meta.get("status") not in {"ai-draft", "reviewed"}:
            raise ValueError(f"{path.name}: unexpected translation status")
        if not meta.get("drafted_by"):
            raise ValueError(f"{path.name}: translation author is required")
        if meta["status"] == "reviewed" and not meta.get("reviewed_by"):
            raise ValueError(f"{path.name}: reviewed status requires a named human reviewer")
    return {path.stem for path in paths}


def validate_distribution():
    locales = validate_catalogs()
    if not {"es", "en", "fr", "zh-CN"} <= locales:
        raise ValueError("A documented locale is missing")
    source_files = {p.name: p.read_bytes() for p in CANONICAL.iterdir() if p.is_file()}
    chat_files = {p.name: p.read_bytes() for p in CHAT.iterdir() if p.is_file()}
    if source_files != chat_files:
        raise ValueError("Chat catalogs differ; run build_distribution.py --sync-i18n")
    return locales


if __name__ == "__main__":
    print("Validated locales: " + ", ".join(sorted(validate_distribution())))
