#!/usr/bin/env python3
"""Fail when MkDocs icon shortcodes leak into rendered HTML."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SITE = Path("site")
SHORTCODE_RE = re.compile(r":(?:material|octicons|fontawesome)-[a-z0-9-]+:")


def main() -> int:
    if not SITE.exists():
        print("Rendered site directory is missing. Run `mkdocs build` first.")
        return 1

    failures: list[str] = []
    for path in sorted(SITE.rglob("*.html")):
        text = path.read_text(encoding="utf-8")
        matches = sorted(set(SHORTCODE_RE.findall(text)))
        if matches:
            failures.append(f"{path}: {', '.join(matches)}")

    if failures:
        print("Rendered shortcode check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Rendered HTML contains no unexpanded Material/Octicons/FontAwesome shortcodes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
