"""Normalize page titles and expose Mermaid detection to Material."""

from rendered_page import Page


def on_page_markdown(markdown, page, config, files):
    # A null title shadows MkDocs' heading fallback even when Jinja uses `or`.
    if not page.meta.get("title"):
        page.meta.pop("title", None)
    return markdown


def on_env(env, config, files):
    env.filters["has_mermaid"] = lambda text: Page(text).has_mermaid
    return env
