#!/usr/bin/env python3
"""Fail when Markdown docs pages are not reachable from mkdocs.yml nav."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


DOCS = Path("docs")
MKDOCS = Path("mkdocs.yml")


class MkDocsLoader(yaml.SafeLoader):
    """Safe loader that tolerates MkDocs/Python tags outside the nav tree."""


def construct_unknown(loader: MkDocsLoader, node: yaml.Node) -> Any:
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


MkDocsLoader.add_constructor(None, construct_unknown)


def nav_paths(items: list[Any]) -> set[Path]:
    paths: set[Path] = set()
    for item in items:
        if isinstance(item, str):
            if item.endswith(".md"):
                paths.add(Path(item))
            continue

        if not isinstance(item, dict):
            continue

        for value in item.values():
            if isinstance(value, str):
                if value.endswith(".md"):
                    paths.add(Path(value))
            elif isinstance(value, list):
                paths.update(nav_paths(value))

    return paths


def main() -> int:
    config = yaml.load(MKDOCS.read_text(encoding="utf-8"), Loader=MkDocsLoader)
    configured = nav_paths(config.get("nav", []))
    existing = {path.relative_to(DOCS) for path in DOCS.rglob("*.md")}

    missing_from_nav = sorted(existing - configured)
    missing_files = sorted(configured - existing)

    if missing_from_nav or missing_files:
        print("Navigation coverage check failed:")

        if missing_from_nav:
            print("\nDocs pages missing from mkdocs.yml nav:")
            for path in missing_from_nav:
                print(f"- {path}")

        if missing_files:
            print("\nmkdocs.yml nav entries with no matching docs file:")
            for path in missing_files:
                print(f"- {path}")

        return 1

    print(f"Navigation covers all {len(existing)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
