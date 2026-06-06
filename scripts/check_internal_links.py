#!/usr/bin/env python3
"""Check local Markdown links and anchors.

This is intentionally small and dependency-free. It checks links of the form
`path.md` and `path.md#anchor` inside docs/*.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


DOCS = Path("docs")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def slugify(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify(match.group(2))
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def split_target(target: str) -> tuple[str, str | None]:
    if "#" in target:
        path, anchor = target.split("#", 1)
        return path, anchor
    return target, None


def is_external(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def main() -> int:
    markdown_files = sorted(DOCS.rglob("*.md"))
    anchor_cache = {path: anchors_for(path) for path in markdown_files}
    failures: list[str] = []

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split()[0].strip("<>")
            if is_external(target):
                continue

            target_path, anchor = split_target(target)
            if not target_path.endswith(".md"):
                continue

            resolved = (source.parent / target_path).resolve()
            try:
                relative = resolved.relative_to(Path.cwd().resolve())
            except ValueError:
                failures.append(f"{source}: link escapes repo: {target}")
                continue

            if not relative.exists():
                failures.append(f"{source}: missing target: {target}")
                continue

            if anchor and anchor not in anchor_cache.get(relative, set()):
                failures.append(f"{source}: missing anchor #{anchor} in {target_path}")

    if failures:
        print("Internal link check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Checked {len(markdown_files)} Markdown files; internal links look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
