"""Render the Markdown error page in MkDocs' root-aware 404 template."""

from pathlib import Path

import markdown


def on_template_context(context, template_name, config):
    if template_name == "404.html":
        source = Path(config.docs_dir) / "404.md"
        context["not_found_content"] = markdown.markdown(source.read_text(encoding="utf-8"))
    return context
