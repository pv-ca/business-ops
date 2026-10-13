#!/usr/bin/env python3
"""Check a business-ops context folder, or list what uses a catalog entry.

Read-only, standard library only, Python 3.9 or newer.

    python3 check_context.py <context folder>
    python3 check_context.py <context folder> --company acme
    python3 check_context.py <context folder> --company acme --uses basic-plan

The first two forms check the files against the structure in
references/context-formats.md and exit 1 when an error is found. The third
lists the templates whose `uses` names the entry and the other files that
mention its ID or name; it always exits 0.
"""
import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

STATUSES = {"planned", "in_development", "pilot", "available", "retired", "unknown"}
ID_PATTERN = r"[a-z0-9]+(?:-[a-z0-9]+)*"
TEXT_SUFFIXES = {".md", ".txt", ".html", ".htm", ".csv"}
SKIPPED_DIRS = {"archive", "node_modules", "__pycache__"}
UPDATES_CEILING = 20


class Report:
    def __init__(self, root):
        self.root = root
        self.errors = []
        self.warnings = []

    def _where(self, path, line):
        where = str(Path(path).relative_to(self.root))
        return f"{where}:{line}" if line else where

    def error(self, path, message, line=None):
        self.errors.append(f"error    {self._where(path, line)}: {message}")

    def warning(self, path, message, line=None):
        self.warnings.append(f"warning  {self._where(path, line)}: {message}")


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def cells(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line)]


def tables(text):
    """Yield (header cells, [(line number, row cells)]) for each Markdown table."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and re.match(r"\s*\|?\s*:?-{3,}", lines[i + 1]):
            header = cells(lines[i])
            rows = []
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append((i + 1, cells(lines[i])))
                i += 1
            yield header, rows
        else:
            i += 1


def read_catalog(path, report=None):
    """Return {id: {"status", "name", "line"}} from every table whose first column is ID."""
    entries = {}
    for header, rows in tables(read(path)):
        if not header or header[0].lower() != "id":
            continue
        lowered = [h.lower() for h in header]
        status_at = lowered.index("status") if "status" in lowered else None
        for line, row in rows:
            entry_id = row[0].strip("`").strip()
            status = None
            if status_at is not None and status_at < len(row):
                # The status word may be followed by a note in the same cell.
                status = row[status_at].strip().lower()
                leading = re.match(r"`?([a-z_]+)`?", status)
                if leading and leading.group(1) in STATUSES:
                    status = leading.group(1)
            name = row[1] if len(row) > 1 else ""
            if report:
                if not re.fullmatch(ID_PATTERN, entry_id):
                    report.error(path, f"ID cell `{entry_id}` must hold one ID: lowercase words joined by hyphens", line)
                if entry_id in entries:
                    report.error(path, f"ID `{entry_id}` is repeated (first on line {entries[entry_id]['line']})", line)
                if status_at is not None and status not in STATUSES:
                    report.error(path, f"`{entry_id}`: the Status cell must start with one of {', '.join(sorted(STATUSES))}; it holds \"{status}\"", line)
            entries.setdefault(entry_id, {"status": status, "name": name, "line": line})
        if report and status_at is None:
            report.warning(path, "a table with an ID column has no Status column, so its entries have no status", rows[0][0] - 2 if rows else None)
    return entries


def front_matter(text):
    """Return the scalar fields and the `uses` list of a template, or None without front matter."""
    match = re.match(r"---\r?\n(.*?)\r?\n---", text, re.S)
    if not match:
        return None
    fields = {"uses": []}
    key = None
    for line in match.group(1).splitlines():
        item = re.match(r"\s+-\s+(.*)", line)
        if item and key == "uses":
            fields["uses"].append(item.group(1).split("#")[0].strip().strip("`'\""))
            continue
        pair = re.match(r"([A-Za-z_][\w-]*):\s*(.*)", line)
        if not pair:
            continue
        key, value = pair.group(1), pair.group(2)
        if key == "uses":
            inline = re.match(r"\[(.*?)\]", value)
            if inline:
                fields["uses"] = [v.strip().strip("`'\"") for v in inline.group(1).split(",") if v.strip()]
        else:
            fields[key] = re.sub(r"\s+#.*$", "", value).strip().strip("'\"")
    return fields


def templates_of(company_dir):
    folder = company_dir / "templates"
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.glob("*.md") if p.name.lower() != "readme.md")


def dated_headings(text, level):
    """Return [(line number, date)] for headings of that level that start with YYYY-MM-DD."""
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(rf"{'#' * level} (\d{{4}})-(\d{{2}})-(\d{{2}})\b", line)
        if match:
            try:
                found.append((number, date(*map(int, match.groups()))))
            except ValueError:
                found.append((number, None))
    return found


def check_dates(path, entries, report, max_age_days, what, archive):
    for number, day in entries:
        if day is None:
            report.error(path, "heading holds a date that does not exist", number)
    days = [(n, d) for n, d in entries if d]
    for (_, newer), (number, older) in zip(days, days[1:]):
        if older > newer:
            report.warning(path, f"{what} are not newest first", number)
            break
    old = [d for _, d in days if (date.today() - d).days > max_age_days]
    if old:
        report.warning(path, f"{len(old)} of the {what} are past the ceiling; move them to {archive}")


def check_company(company_dir, report):
    catalog_path = company_dir / "catalog.md"
    catalog = read_catalog(catalog_path, report) if catalog_path.exists() else {}
    templates = templates_of(company_dir)
    if templates and not catalog_path.exists():
        report.error(company_dir, "has templates and no catalog.md, so their `uses` cannot be checked")

    for path in templates:
        fields = front_matter(read(path))
        if fields is None:
            report.error(path, "no front matter (template, company, uses)")
            continue
        if fields.get("template") and fields["template"] != path.stem:
            report.warning(path, f"`template: {fields['template']}` differs from the file name")
        if fields.get("company") and fields["company"] != company_dir.name:
            report.warning(path, f"`company: {fields['company']}` differs from the folder `{company_dir.name}`")
        if not fields["uses"]:
            report.warning(path, "`uses` is empty, so no catalog change will point to this template")
        for entry_id in fields["uses"]:
            if not catalog_path.exists():
                break
            if entry_id not in catalog:
                report.error(path, f"`uses` names `{entry_id}`, which is not an ID in catalog.md")
            elif catalog[entry_id]["status"] not in (None, "available"):
                report.warning(path, f"`uses` names `{entry_id}`, whose status is `{catalog[entry_id]['status']}`: only available entries go into customer-facing material")

    changelog = company_dir / "changelog.md"
    if changelog.exists():
        check_dates(changelog, dated_headings(read(changelog), 2), report, 730, "changelog entries", "archive/changelog-YYYY.md")

    context = company_dir / "context.md"
    if context.exists():
        text = read(context)
        section = re.search(r"(?m)^## (?:\d+\. )?Updates\b.*$", text)
        if section:
            offset = text[: section.end()].count("\n") + 1
            rest = text[section.end():]
            following = re.search(r"(?m)^## ", rest)
            body = rest[: following.start()] if following else rest
            updates = [(n + offset - 1, d) for n, d in dated_headings(body, 3)]
            check_dates(context, updates, report, 365, "\"Updates\" entries", "archive/context-updates-YYYY.md")
            if len(updates) > UPDATES_CEILING:
                report.warning(context, f"\"Updates\" has {len(updates)} entries (ceiling about {UPDATES_CEILING}); fold what still holds into its section and archive the rest")
        else:
            report.warning(context, "no \"Updates\" section")


def find_companies(root):
    return sorted(
        p for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and ((p / "context.md").exists() or (p / "catalog.md").exists())
    )


def text_files(folder):
    """Text files under the folder, skipping archives, hidden folders and nested repositories."""
    for current, dirs, files in os.walk(folder):
        dirs[:] = sorted(
            d for d in dirs
            if not d.startswith(".") and d not in SKIPPED_DIRS and not (Path(current) / d / ".git").exists()
        )
        for name in sorted(files):
            path = Path(current) / name
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def list_uses(root, company_dir, entry_id):
    catalog_path = company_dir / "catalog.md"
    catalog = read_catalog(catalog_path) if catalog_path.exists() else {}
    entry = catalog.get(entry_id)
    if entry:
        print(f"`{entry_id}`: {entry['name']} (status: {entry['status'] or 'none'})")
    else:
        print(f"`{entry_id}` is not an ID in {company_dir.name}/catalog.md; searching for the text anyway")

    named = [p for p in templates_of(company_dir) if entry_id in (front_matter(read(p)) or {"uses": []})["uses"]]
    print(f"\nTemplates whose `uses` names it: {len(named)}")
    for path in named:
        print(f"  {path.relative_to(root)}")

    # A short name ("Pro", "Plus") matches unrelated text, so only longer names are searched.
    terms = ["(?i:" + re.escape(entry_id) + ")"]
    if entry and len(entry["name"]) >= 5:
        terms.append(re.escape(entry["name"]))
    pattern = re.compile(r"(?<![\w-])(?:" + "|".join(terms) + r")(?![\w-])")
    skipped = set(named) | {catalog_path, company_dir / "changelog.md"}
    mentions = []
    for path in text_files(company_dir):
        if path in skipped:
            continue
        lines = [n for n, line in enumerate(read(path).splitlines(), 1) if pattern.search(line)]
        if lines:
            mentions.append((path, lines))
    print(f"\nOther files that mention the ID or the name: {len(mentions)}")
    for path, lines in mentions:
        shown = ", ".join(map(str, lines[:8])) + (", ..." if len(lines) > 8 else "")
        print(f"  {path.relative_to(root)} (lines {shown})")
    print("\nNot searched: archive folders, nested repositories, binary files and the document library.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folder", help="the context folder (holds business-ops-context.md)")
    parser.add_argument("--company", help="check or search one company folder only")
    parser.add_argument("--uses", metavar="ID", help="list what uses this catalog entry (needs --company)")
    args = parser.parse_args(argv)

    root = Path(args.folder).expanduser().resolve()
    if not root.is_dir():
        print(f"not a folder: {root}")
        return 2
    if args.company:
        companies = [root / args.company]
        if not companies[0].is_dir():
            print(f"no company folder named {args.company} in {root}")
            return 2
    else:
        companies = find_companies(root)

    if args.uses:
        if not args.company:
            print("--uses needs --company, because IDs are unique per catalog only")
            return 2
        list_uses(root, companies[0], args.uses)
        return 0

    report = Report(root)
    if not (root / "business-ops-context.md").exists():
        report.error(root / "business-ops-context.md", "missing: the profile and index of companies")
    if not companies:
        report.warning(root, "no company folder found (a folder with context.md or catalog.md)")
    for company_dir in companies:
        check_company(company_dir, report)

    for line in report.errors + report.warnings:
        print(line)
    names = ", ".join(c.name for c in companies) or "none"
    print(f"\ncompanies checked: {names}; {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
