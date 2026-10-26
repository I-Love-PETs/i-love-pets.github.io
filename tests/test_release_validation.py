"""Regression cases for release checks that could otherwise pass silently."""
import unittest
from pathlib import Path
from scripts.check_release import FIELDS, MERMAID, PLACEHOLDER, Metadata, check_metadata, check_structure, check_headings


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

    def framing(self, value='Records'):
        return ('## Decision framing\n\n' +
                ''.join(f'| {field} | {value} |\n' for field in FIELDS) +
                '\n## Does not protect\n\n## Failure modes\n')

    def test_empty_framing_cells(self):
        for value in ('', ' ', '   ', '\t'):
            with self.subTest(value=value):
                self.assertIn('missing or empty Protected asset', check_structure(self.framing(value)))
        self.assertEqual(check_structure(self.framing()), [])

    def test_template_heading_placeholders(self):
        for title in ('# Use Case', '# Problem Name', '# Pattern Name', '# Architecture Name', '# Tool Name'):
            with self.subTest(title=title):
                self.assertIsNotNone(PLACEHOLDER.search(title))

    def test_template_framing_prompts(self):
        template = Path('docs/contributing/pattern-template.md').read_text()
        self.assertTrue(any('placeholder' in error for error in check_structure(template)))

    def test_generic_social_titles(self):
        for title in ('Home', 'Overview'):
            text = self.page().replace('Keys &amp; &quot;outputs&quot;', title)
            self.assertTrue(any('title' in error for error in check_metadata(text, 'https://example.org/a/', False)))

    def test_limits_headings_ignore_case_and_require_whole_heading(self):
        self.assertEqual(check_headings('## failure modes\n', ('Failure Modes',)), [])
        self.assertTrue(check_headings('## Failure Modes Elsewhere\n', ('Failure Modes',)))
