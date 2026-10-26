#!/usr/bin/env python3
"""Check v1.0 content conventions and generated social/diagram metadata."""
from __future__ import annotations

from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urljoin

from mkdocs.config import load_config
from mkdocs.utils.meta import get_data

if __package__:
    from .check_site import Page
else:
    from check_site import Page

FIELDS = ("Protected asset", "Adversary", "Allowed output", "Leakage surface", "Assumptions", "Non-goals")
MERMAID = "https://unpkg.com/mermaid@10.9.1/dist/mermaid.min.js"
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|INSERT HERE)\b|\[Your Name\]|202\d-XX-XX|^# (?:(?:Pattern|Architecture|Tool|Problem) Name|Use Case)$", re.M)

LIMIT_HEADINGS = {
    "tool-reviews": ("Protected Assets", "Threat Model Support", "When Not To Use", "Failure Modes"),
    "use-cases": ("Failure Modes",),
}
FRAMING_PROMPTS = (
    "Name the data or artifacts to protect.",
    "Name capabilities, corruption model, and collusion threshold.",
    "Name the result, recipients, and permitted query frequency.",
    "Include outputs, intermediates, metadata, logs, and side channels.",
    "State concrete conditions on keys, hardware, parties, and accounting.",
    "State excluded attacks and properties; do not imply complete privacy.",
)


class Metadata(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.meta = defaultdict(list)
        self.canonical = []
        self.scripts = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "meta":
            key = values.get("property") or values.get("name")
            if key:
                self.meta[key].append(values.get("content", ""))
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical.append(values.get("href", ""))
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"])


def check_metadata(text: str, canonical: str, diagrams: bool) -> list[str]:
    page = Metadata(text)
    failures = []
    for key in ("og:type", "og:site_name", "og:title", "og:description", "og:url", "twitter:card", "twitter:title", "twitter:description"):
        values = page.meta[key]
        if len(values) != 1 or not values[0].strip():
            failures.append(f"missing, empty, or duplicate {key}")
    if page.meta["og:title"] in (["Home"], ["Overview"]):
        failures.append("og:title must identify the page, not its generic navigation label")
    if page.canonical != [canonical] or page.meta["og:url"] != [canonical]:
        failures.append("canonical and og:url must match the page URL")
    if page.meta["twitter:card"] != ["summary"]:
        failures.append("expected a text-first summary card")
    if page.meta["og:title"] != page.meta["twitter:title"] or page.meta["og:description"] != page.meta["twitter:description"]:
        failures.append("social titles and descriptions must agree")
    scripts = [src for src in page.scripts if "mermaid" in src.lower()]
    if scripts != ([MERMAID] if diagrams else []):
        failures.append("load pinned Mermaid exactly once, only on diagram pages")
    if diagrams:
        bundles = [i for i, src in enumerate(page.scripts) if "/bundle." in src]
        if not bundles or MERMAID not in page.scripts or page.scripts.index(MERMAID) > bundles[0]:
            failures.append("Mermaid must precede Material's renderer")
    return failures


def check_structure(text: str, allow_placeholders: bool = False) -> list[str]:
    failures = []
    for heading in ("Decision framing", "Does not protect", "Failure modes"):
        if not re.search(r"^## " + re.escape(heading) + r"\s*$", text, re.M):
            failures.append(f"missing {heading} section")
    framing = re.search(r"^## Decision framing\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    for field in FIELDS:
        row = re.search(r"^\|[ \t]*" + re.escape(field) + r"[ \t]*\|([^\n]*)", framing[1], re.M) if framing else None
        value = row[1].split("|", 1)[0].strip() if row else ""
        if not value:
            failures.append(f"missing or empty {field}")
        elif not allow_placeholders and (value in FRAMING_PROMPTS or PLACEHOLDER.search(value)):
            failures.append(f"unresolved placeholder in {field}")
    return failures


def check_headings(text: str, headings: tuple[str, ...]) -> list[str]:
    return [f"missing {heading} section" for heading in headings
            if not re.search(r"^##[ \t]+" + re.escape(heading) + r"[ \t]*$", text, re.M | re.I)]


def check_release(docs: Path, site: Path, site_url: str) -> list[str]:
    failures = []
    titles = {}
    for source in sorted(docs.rglob("*.md")):
        relative = source.relative_to(docs)
        if relative.as_posix() == "404.md":
            continue
        text = source.read_text(encoding="utf-8")
        if relative.parts[0] in ("pet-patterns", "pet-architectures"):
            failures.extend(f"{relative}: {error}" for error in check_structure(text))
        if relative.parts[0] in LIMIT_HEADINGS and source.stem != "index":
            failures.extend(f"{relative}: {error}" for error in check_headings(text, LIMIT_HEADINGS[relative.parts[0]]))
        if relative.parts[0] != "contributing" and PLACEHOLDER.search(text):
            failures.append(f"{relative}: unresolved placeholder marker")
        if source.stem == "index":
            target = relative.with_suffix(".html")
        else:
            target = relative.with_suffix("") / "index.html"
        built = site / target
        if not built.is_file():
            failures.append(f"{relative}: missing built page")
            continue
        html = built.read_text(encoding="utf-8")
        _, authored = get_data(text)
        description = authored.get("description")
        metadata = Metadata(html)
        if description and metadata.meta["og:description"] != [description]:
            failures.append(f"{relative}: authored description missing from social metadata")
        for title in metadata.meta["og:title"]:
            if title in titles:
                failures.append(f"{relative}: repeated og:title (also used by {titles[title]})")
            titles[title] = relative
        expected = urljoin(site_url, target.as_posix().removesuffix("index.html"))
        failures.extend(f"{relative}: {error}" for error in check_metadata(html, expected, Page(html).has_mermaid))
        if '--8<-- "decision-guidance.md"' in text and ('Evidence and assumptions' not in html or '--8&lt;--' in html):
            failures.append(f"{relative}: decision guidance include was not rendered")
    for name in ("pattern", "architecture"):
        template = docs / "contributing" / f"{name}-template.md"
        failures.extend(f"{template}: {error}" for error in check_structure(template.read_text(encoding="utf-8"), allow_placeholders=True))
    for name, section in (("tool", "tool-reviews"), ("use-case", "use-cases")):
        template = docs / "contributing" / f"{name}-template.md"
        failures.extend(f"{template}: {error}" for error in check_headings(template.read_text(encoding="utf-8"), LIMIT_HEADINGS[section]))
    return failures


def main() -> int:
    config = load_config()
    failures = check_release(Path(config.docs_dir), Path(config.site_dir), config.site_url)
    if failures:
        print("Release checks failed:\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("Decision framing, templates, placeholder scan, social metadata, and conditional Mermaid checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
