#!/usr/bin/env python3
"""Validate generated local links, sitemap, robots.txt, and the GitHub Pages 404."""

from __future__ import annotations

from collections import defaultdict
import gzip
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

from mkdocs.config import load_config
from mkdocs.structure.files import get_files
from mkdocs.structure.pages import Page as MkDocsPage


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.meta = defaultdict(list)
        self.canonical = []
        self.scripts = []
        self.ids: set[str] = set()
        self.targets: list[str] = []
        self.noindex = False
        self.has_mermaid = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "mermaid" in (values.get("class") or "").split():
            self.has_mermaid = True
        if tag == "meta":
            key = values.get("property") or values.get("name")
            if key:
                self.meta[key].append(values.get("content", ""))
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical.append(values.get("href", ""))
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"])
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "meta" and values.get("name") == "robots":
            self.noindex = "noindex" in values.get("content", "")
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.targets.append(values[attribute])


def on_page_markdown(markdown, page, config, files):
    # A null title shadows MkDocs' heading fallback even when Jinja uses `or`.
    if not page.meta.get("title"):
        page.meta.pop("title", None)
    return markdown


def on_env(env, config, files):
    env.filters["has_mermaid"] = lambda text: Page(text).has_mermaid
    return env


def documentation_pages(config):
    for file in get_files(config).documentation_pages():
        yield file, MkDocsPage(None, file, config).canonical_url


def check_site(site: Path, site_url: str, config=None) -> list[str]:
    failures: list[str] = []
    origin = urlsplit(site_url)
    base_path = origin.path.rstrip("/") + "/"
    pages = {p.relative_to(site).as_posix(): Page(p.read_text(encoding="utf-8"))
             for p in site.rglob("*.html")}
    urls = {file.dest_uri: canonical for file, canonical in documentation_pages(config)} if config else {
        name: urljoin(site_url, name.removesuffix("index.html")) for name in pages if name != "404.html"
    }
    if "index.html" not in pages:
        failures.append("Missing built home page: index.html")

    def local_file(url: str) -> str | None:
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or parsed.netloc != origin.netloc:
            return None
        if not parsed.path.startswith(base_path):
            return None
        path = unquote(parsed.path[len(base_path):])
        return path + "index.html" if not path or path.endswith("/") else path

    for name, page in pages.items():
        # A 404 response is served at arbitrary missing paths. Root-aware URLs
        # must also work when that path has several levels.
        page_url = urljoin(site_url, "missing/deep/page/") if name == "404.html" else urls.get(name, urljoin(site_url, name))
        for target in page.targets:
            if name == "404.html" and target.startswith("#"):
                continue
            resolved = urljoin(page_url, target)
            local = local_file(resolved)
            if local is None:
                continue
            if not (site / local).is_file():
                failures.append(f"{name}: missing local target: {target}")
                continue
            fragment = unquote(urlsplit(resolved).fragment)
            if fragment and local in pages and fragment not in pages[local].ids:
                failures.append(f"{name}: missing anchor: {target}")

    try:
        xml = (site / "sitemap.xml").read_bytes()
        locations = [node.text for node in ElementTree.fromstring(xml).findall(
            "{http://www.sitemaps.org/schemas/sitemap/0.9}url/"
            "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        expected = set(urls.values())
        if set(locations) != expected or len(locations) != len(set(locations)):
            failures.append("Sitemap must list every content page once, at its canonical URL, without 404.")
        if gzip.decompress((site / "sitemap.xml.gz").read_bytes()) != xml:
            failures.append("Compressed sitemap differs from sitemap.xml")
    except (OSError, ElementTree.ParseError, EOFError) as error:
        failures.append(f"Invalid or missing sitemap: {error}")

    robots = site / "robots.txt"
    sitemap_urls = set()
    if robots.is_file():
        for line in robots.read_text(encoding="utf-8").splitlines():
            directive, separator, value = line.split("#", 1)[0].partition(":")
            if separator and directive.strip().lower() == "sitemap":
                sitemap_urls.add(value.strip())
    if urljoin(site_url, "sitemap.xml") not in sitemap_urls:
        failures.append("robots.txt must point to the canonical sitemap")
    error_page = pages.get("404.html")
    if error_page is None or not error_page.noindex:
        failures.append("404.html must exist and include a noindex meta tag")
    elif "Page not found" not in (site / "404.html").read_text(encoding="utf-8"):
        failures.append("404.html is missing the friendly error content")
    return failures


def main() -> int:
    config = load_config()
    failures = check_site(Path(config.site_dir), config.site_url, config)
    if failures:
        print("Built-site validation failed:\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("Built links, anchors, sitemap, robots.txt, and nested-path 404 links pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
