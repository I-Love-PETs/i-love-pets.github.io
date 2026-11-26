"""Read markup shared by the MkDocs build hooks and publishing checks."""

from collections import defaultdict
from html.parser import HTMLParser


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.meta = defaultdict(list)
        self.document_titles: list[str] = []
        self._in_head = False
        self._in_title = False
        self.canonical = []
        self.scripts = []
        self.ids: set[str] = set()
        self.targets: list[str] = []
        self.noindex = False
        self.has_mermaid = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "head":
            self._in_head = True
        if tag == "title" and self._in_head:
            self.document_titles.append("")
            self._in_title = True
        if "mermaid" in (values.get("class") or "").split():
            self.has_mermaid = True
        if tag == "meta":
            property_key = values.get("property") or ""
            name = values.get("name") or ""
            # OpenGraph uses property and Twitter cards use name.
            content = values.get("content", "")
            if property_key.startswith("og:"):
                self.meta[property_key].append(content)
            elif name and not name.startswith("og:"):
                self.meta[name].append(content)
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

    def handle_endtag(self, tag):
        if tag == "head":
            self._in_head = False
        if tag == "title" or tag == "head":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.document_titles[-1] += data
