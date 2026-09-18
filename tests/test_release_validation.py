"""Regression cases for release checks that could otherwise pass silently."""
import unittest
from scripts.check_release import MERMAID, Metadata, check_metadata, check_structure


class ReleaseValidationTests(unittest.TestCase):
    def page(self, diagrams=False):
        values = {'og:type': 'website', 'og:site_name': 'I &amp; PETs',
                  'og:title': 'Keys &amp; &quot;outputs&quot;', 'og:description': 'A &lt; B',
                  'og:url': 'https://example.org/a/', 'twitter:card': 'summary',
                  'twitter:title': 'Keys &amp; &quot;outputs&quot;', 'twitter:description': 'A &lt; B'}
        text = '<link rel="canonical" href="https://example.org/a/">'
        text += ''.join(f'<meta name="{key}" content="{value}">' for key, value in values.items())
        if diagrams:
            text += f'<script src="{MERMAID}"></script>'
        return text + '<script src="/assets/javascripts/bundle.example.js"></script>'

    def test_valid_pages_and_escaping(self):
        for diagrams in (False, True):
            self.assertEqual(check_metadata(self.page(diagrams), 'https://example.org/a/', diagrams), [])
        self.assertEqual(Metadata(self.page()).meta['og:title'], ['Keys & "outputs"'])

    def test_wrong_canonical_and_duplicate_metadata(self):
        text = self.page() + '<meta name="og:title" content="duplicate">'
        errors = check_metadata(text, 'https://example.org/b/', False)
        self.assertTrue(any('duplicate og:title' in error for error in errors))
        self.assertTrue(any('canonical' in error for error in errors))

    def test_missing_and_global_mermaid(self):
        self.assertTrue(check_metadata(self.page(), 'https://example.org/a/', True))
        self.assertTrue(check_metadata(self.page(True), 'https://example.org/a/', False))

    def test_mermaid_must_precede_material(self):
        text = self.page() + f'<script src="{MERMAID}"></script>'
        self.assertTrue(any('precede' in error for error in check_metadata(text, 'https://example.org/a/', True)))

    def test_fields_outside_framing_do_not_count(self):
        text = '## Decision framing\n\n## Does not protect\n| Protected asset | Records |\n\n## Failure modes\n'
        self.assertIn('missing or empty Protected asset', check_structure(text))
