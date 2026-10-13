#!/usr/bin/env python3
"""Raise the plugin version in both manifests and open the changelog entry.

Run from the repository root:

    python3 scripts/bump_version.py 0.13.0 "First change." "Second change."

Each further argument becomes one line of the changelog entry. Review the
entry, then run scripts/validate.py.
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = [
    ROOT / "business-ops" / ".claude-plugin" / "plugin.json",
    ROOT / "business-ops" / ".codex-plugin" / "plugin.json",
]
CHANGELOG = ROOT / "CHANGELOG.md"


def as_tuple(version):
    return tuple(int(part) for part in version.split("."))


def main(argv):
    if len(argv) < 2 or not re.fullmatch(r"\d+\.\d+\.\d+", argv[0]):
        print(__doc__)
        return 2
    version, lines = argv[0], argv[1:]
    texts = [path.read_text(encoding="utf-8") for path in MANIFESTS]
    pattern = r'("version"\s*:\s*")(\d+\.\d+\.\d+)(")'
    for path, text in zip(MANIFESTS, texts):
        current = re.search(pattern, text)
        if not current:
            print(f"no version found in {path.relative_to(ROOT)}")
            return 1
        if as_tuple(version) <= as_tuple(current.group(2)):
            print(f"{version} is not above {current.group(2)} in {path.relative_to(ROOT)}")
            return 1
    # The manifests are edited as text so that their formatting and key order stay as written.
    for path, text in zip(MANIFESTS, texts):
        path.write_text(re.sub(pattern, rf"\g<1>{version}\g<3>", text, count=1), encoding="utf-8")
    changelog = CHANGELOG.read_text(encoding="utf-8")
    first = re.search(r"(?m)^## ", changelog)
    entry = f"## {version} ({date.today().isoformat()})\n\n" + "".join(f"- {line}\n" for line in lines) + "\n"
    CHANGELOG.write_text(changelog[: first.start()] + entry + changelog[first.start():], encoding="utf-8")
    print(f"version {version} written to both manifests and to CHANGELOG.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
