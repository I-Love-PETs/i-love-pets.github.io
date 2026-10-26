#!/usr/bin/env python3
"""Check v1.0 content conventions and generated social/diagram metadata."""
from __future__ import annotations

from pathlib import Path
import re
import sys

from mkdocs.config import load_config
from mkdocs.utils.meta import get_data

if __package__:
    from .check_site import Page, documentation_pages
else:
    from check_site import Page, documentation_pages

FIELDS = ("Protected asset", "Adversary", "Allowed output", "Leakage surface", "Assumptions", "Non-goals")
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


def check_metadata(text: str, canonical: str, diagrams: bool, mermaid_url: str) -> list[str]:
    page = Page(text)
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
    if scripts != ([mermaid_url] if diagrams else []):
        failures.append("load pinned Mermaid exactly once, only on diagram pages")
    if diagrams:
        bundles = [i for i, src in enumerate(page.scripts) if "/bundle." in src]
        if not bundles or mermaid_url not in page.scripts or page.scripts.index(mermaid_url) > bundles[0]:
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


def check_release(config) -> list[str]:
    docs = Path(config.docs_dir)
    failures = []
    titles = {}
    for file, canonical in documentation_pages(config):
        relative = Path(file.src_uri)
        text = file.content_string
        if relative.parts[0] in ("pet-patterns", "pet-architectures") and relative.stem != "index":
            failures.extend(f"{relative}: {error}" for error in check_structure(text))
        if relative.parts[0] in LIMIT_HEADINGS and relative.stem != "index":
            failures.extend(f"{relative}: {error}" for error in check_headings(text, LIMIT_HEADINGS[relative.parts[0]]))
        if relative.parts[0] != "contributing" and PLACEHOLDER.search(text):
            failures.append(f"{relative}: unresolved placeholder marker")
        built = Path(file.abs_dest_path)
        if not built.is_file():
            failures.append(f"{relative}: missing built page")
            continue
        html = built.read_text(encoding="utf-8")
        _, authored = get_data(text)
        description = authored.get("description")
        metadata = Page(html)
        if description and metadata.meta["og:description"] != [description]:
            failures.append(f"{relative}: authored description missing from social metadata")
        for title in metadata.meta["og:title"]:
            if title in titles:
                failures.append(f"{relative}: repeated og:title (also used by {titles[title]})")
            titles[title] = relative
        failures.extend(f"{relative}: {error}" for error in check_metadata(html, canonical, Page(html).has_mermaid, config.extra["mermaid_script"]))
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
    failures = check_release(config)
    if failures:
        print("Release checks failed:\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("Decision framing, templates, placeholder scan, social metadata, and conditional Mermaid checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
