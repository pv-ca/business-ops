#!/usr/bin/env python3
"""Check the plugin against its own rules. Standard library only.

Run from the repository root: python3 scripts/validate.py
Exits 1 when any check fails.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "business-ops"
SKILLS = PLUGIN / "skills"
errors = []


def fail(path, message):
    errors.append(f"{Path(path).relative_to(ROOT)}: {message}")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(path, "no frontmatter")
        return {}, text
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, text


def check_skills():
    names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    for name in names:
        path = SKILLS / name / "SKILL.md"
        if not path.exists():
            fail(SKILLS / name, "missing SKILL.md")
            continue
        fields, text = frontmatter(path)
        if set(fields) != {"name", "description"}:
            fail(path, "frontmatter must hold name and description only")
        if fields.get("name") != name:
            fail(path, "name differs from the folder name")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            fail(path, "name must be lowercase words joined by hyphens, up to 64 characters")
        description = fields.get("description", "").strip('"').replace('\\"', '"')
        if not description.startswith("Use "):
            fail(path, "description must start with the trigger wording (Use ...)")
        if len(description) > 1024:
            fail(path, f"description has {len(description)} characters (limit 1024)")
        if len(text.splitlines()) > 500:
            fail(path, "SKILL.md has more than 500 lines")
        if "${CLAUDE_PLUGIN_ROOT}" in text:
            fail(path, "${CLAUDE_PLUGIN_ROOT} may appear only in commands/")
        if "coach-protocol.md" not in text:
            fail(path, "does not point to the coach protocol")
    return names


def check_relative_paths():
    """Every `../x` or `references/x` path written in backticks must exist."""
    for path in SKILLS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        skill_dir = SKILLS / path.relative_to(SKILLS).parts[0]
        for ref in re.findall(r"`((?:\.\./|references/)[^`\s]+\.md)`", text):
            if "<" in ref:
                continue
            bases = [path.parent, skill_dir]
            if not any((base / ref).exists() for base in bases):
                fail(path, f"path does not exist: {ref}")


def check_playbooks():
    for path in SKILLS.glob("*/references/*playbook.md"):
        text = path.read_text(encoding="utf-8")
        numbers = [int(n) for n in re.findall(r"(?m)^## (\d+)\. ", text)]
        if numbers != list(range(1, len(numbers) + 1)):
            fail(path, "section numbers are not consecutive")
        if "## Contents" not in text:
            fail(path, "no table of contents")
        skill_dir = path.parent.parent
        for other in [skill_dir / "SKILL.md", path.parent / "books.md"]:
            if not other.exists():
                continue
            for cited in re.findall(r"sections? (\d+)(?: (?:and|to) (\d+))?[^.\n]*playbook", other.read_text(encoding="utf-8")):
                for number in filter(None, cited):
                    if int(number) > len(numbers):
                        fail(other, f"cites section {number}, playbook has {len(numbers)}")


def check_no_business_data():
    """The plugin holds nothing from a particular company or machine."""
    patterns = [r"/home/[a-z]", r"/Users/[A-Za-z]", r"[A-Za-z]:\\\\Users"]
    extra = ROOT / "scripts" / "forbidden-terms.txt"
    if extra.exists():
        patterns += [re.escape(t.strip()) for t in extra.read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")]
    for path in PLUGIN.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json"}:
            text = path.read_text(encoding="utf-8")
            for pattern in patterns:
                if re.search(pattern, text, re.I):
                    fail(path, f"holds a machine path or forbidden term: {pattern}")


def check_manifests(names):
    claude = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    codex = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = claude["version"]
    for key in ("name", "version", "description", "license", "repository"):
        if claude.get(key) != codex.get(key):
            fail(PLUGIN / ".codex-plugin" / "plugin.json", f"{key} differs from the Claude Code manifest")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    first = re.search(r"(?m)^## (\S+)", changelog)
    if not first or first.group(1) != version:
        fail(ROOT / "CHANGELOG.md", f"top entry is not version {version}")
    count = str(len(names))
    for readme in (ROOT / "README.md", ROOT / "docs" / "readme" / "README_pt-BR.md"):
        text = readme.read_text(encoding="utf-8")
        if f"{count} skills" not in text:
            fail(readme, f"does not say {count} skills")
        for name in names:
            if f"`{name}`" not in text:
                fail(readme, f"skill {name} is not listed")
    notes = (PLUGIN / "README.md").read_text(encoding="utf-8")
    for name in names:
        if f"`{name}`" not in notes:
            fail(PLUGIN / "README.md", f"skill {name} is not listed")


def check_commands():
    for path in (PLUGIN / "commands").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for skill in re.findall(r"Use the `([a-z-]+)` skill", text):
            if not (SKILLS / skill).is_dir():
                fail(path, f"routes to a skill that does not exist: {skill}")


def main():
    names = check_skills()
    check_relative_paths()
    check_playbooks()
    check_no_business_data()
    check_manifests(names)
    check_commands()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s)")
        return 1
    print(f"ok: {len(names)} skills, manifests in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
