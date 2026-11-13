"""Verify portable ECC bundle without executing bundled code or hooks."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "SHA256SUMS.json").read_text(encoding="utf-8"))
seen = set()
for row in manifest["files"]:
    relative = row["path"]
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or relative in seen:
        raise SystemExit(f"Unsafe or duplicate manifest path: {relative}")
    seen.add(relative)
    if not path.is_file() or path.stat().st_size != row["bytes"]:
        raise SystemExit(f"Missing/size mismatch: {relative}")
    if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
        raise SystemExit(f"SHA-256 mismatch: {relative}")
for descriptor, expected in [(".claude-plugin/marketplace.json", "./Claude-Code"), (".agents/plugins/marketplace.json", "./Codex")]:
    data = json.loads((root / descriptor).read_text(encoding="utf-8"))
    source = data["plugins"][0]["source"]
    actual = source["path"] if isinstance(source, dict) else source
    if actual != expected or not (root / actual).is_dir():
        raise SystemExit(f"Invalid marketplace source: {descriptor}")
for target, descriptor in [("Claude-Code", ".claude-plugin/plugin.json"), ("Codex", ".codex-plugin/plugin.json")]:
    base = root / target
    plugin = json.loads((base / descriptor).read_text(encoding="utf-8"))
    if plugin["name"] != "ecc":
        raise SystemExit(f"Unexpected plugin: {target}")
    skills = plugin["skills"]
    for reference in ([skills] if isinstance(skills, str) else skills):
        path = (base / reference).resolve()
        if not path.is_relative_to(base) or not path.is_dir():
            raise SystemExit(f"Invalid plugin skill path: {target}")
print(f"Verified {len(seen)} files, SHA-256 checksums and both native marketplace entrypoints.")
