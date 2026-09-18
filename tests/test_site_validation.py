"""Regression tests for SEO artifacts and broken links in built output."""

import gzip
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("check_site", Path(__file__).parents[1] / "scripts/check_site.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SiteValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name)
        self.url = "https://example.test/guide/"
        (self.site / "index.html").write_text('<h1 id="home">Home</h1><a href="topic/#detail">Topic</a>')
        (self.site / "topic").mkdir()
        (self.site / "topic/index.html").write_text('<h1 id="detail">Topic</h1><a href="../">Home</a>')
        (self.site / "404.html").write_text('<meta name="robots" content="noindex"><h1>Page not found</h1><a href="/guide/">Home</a>')
        (self.site / "robots.txt").write_text(f"User-agent: *\nSitemap: {self.url}sitemap.xml\n")
        self.sitemap([self.url, self.url + "topic/"])

    def sitemap(self, locations):
        xml = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(
            f'<url><loc>{url}</loc></url>' for url in locations) + '</urlset>'
        (self.site / "sitemap.xml").write_text(xml)
        (self.site / "sitemap.xml.gz").write_bytes(gzip.compress(xml.encode()))

    def check(self):
        return module.check_site(self.site, self.url)

    def test_valid_site_in_subdirectory(self):
        self.assertEqual(self.check(), [])

    def test_missing_link_and_anchor_fail(self):
        (self.site / "index.html").write_text('<a href="missing/">Missing</a><a href="topic/#absent">Anchor</a>')
        failures = self.check()
        self.assertTrue(any("missing local target" in item for item in failures))
        self.assertTrue(any("missing anchor" in item for item in failures))

    def test_relative_error_page_link_fails_at_nested_path(self):
        p = self.site / "404.html"
        p.write_text(p.read_text().replace('/guide/', './'))
        self.assertTrue(any("404.html: missing local target" in item for item in self.check()))

    def test_sitemap_requires_complete_canonical_unique_urls(self):
        for urls in ([self.url], [self.url, self.url, self.url + "topic/"],
                     [self.url, self.url + "topic/", self.url + "404.html"],
                     [self.url, "https://wrong.test/guide/topic/"]):
            with self.subTest(urls=urls):
                self.sitemap(urls)
                self.assertTrue(any("Sitemap must" in item for item in self.check()))

    def test_missing_sitemap_fails(self):
        (self.site / "sitemap.xml").unlink()
        self.assertTrue(any("Invalid or missing sitemap" in item for item in self.check()))

    def test_robots_and_noindex_are_required(self):
        (self.site / "robots.txt").write_text("User-agent: *\n")
        p = self.site / "404.html"
        p.write_text(p.read_text().replace('noindex', 'index'))
        failures = self.check()
        self.assertTrue(any("robots.txt" in item for item in failures))
        self.assertTrue(any("noindex" in item for item in failures))

    def test_robots_rejects_commented_embedded_or_inexact_sitemap(self):
        canonical = f"Sitemap: {self.url}sitemap.xml"
        for directive in (f"# {canonical}", f"Other: {canonical}",
                          f"{canonical}.backup", f"{canonical}?wrong=1"):
            with self.subTest(directive=directive):
                (self.site / "robots.txt").write_text(f"User-agent: *\n{directive}\n")
                self.assertTrue(any("robots.txt" in item for item in self.check()))

    def test_robots_accepts_directive_whitespace_case_and_comment(self):
        (self.site / "robots.txt").write_text(
            f"User-agent: *\n  sitemap :  {self.url}sitemap.xml  # canonical map\n")
        self.assertEqual(self.check(), [])

    def test_compressed_sitemap_must_match(self):
        (self.site / "sitemap.xml.gz").write_bytes(gzip.compress(b"different"))
        self.assertTrue(any("Compressed sitemap differs" in item for item in self.check()))


if __name__ == "__main__":
    unittest.main()
