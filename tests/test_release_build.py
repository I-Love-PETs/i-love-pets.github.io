"""Build real Material pages to exercise release validation and template output."""
import html
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from mkdocs.commands.build import build
from mkdocs.config import load_config

from scripts.check_release import Metadata, check_release

ROOT = Path(__file__).resolve().parents[1]


class ReleaseBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        root = Path(cls.temporary.name)
        cls.docs = root / 'docs'
        cls.site = root / 'site'
        cls.docs.mkdir()
        snippets = root / 'includes'
        snippets.mkdir()
        (snippets / 'diagram.md').write_text('```mermaid\ngraph LR\n A --> B\n```\n')
        pages = {
            'index.md': '# Welcome\n',
            'pet-patterns/index.md': '---\ntitle: Pattern catalog\n---\n# Pattern catalog\n',
            'pet-architectures/index.md': '---\ntitle: Architecture catalog\n---\n# Architecture catalog\n',
            'use-cases/missing.md': '# Incomplete use case\n',
            'tool-reviews/missing.md': '# Incomplete tool review\n\n## Protected Assets\n\n## Threat Model Support\n\n## When Not To Use\n',
            'one/index.md': '---\ntitle: First overview\n---\n# First overview\n',
            'two/index.md': '---\ntitle: Second overview\n---\n# Second overview\n',
            'tilde.md': '# Tilde diagram\n\n~~~mermaid\ngraph LR\n A --> B\n~~~\n',
            'snippet.md': '# Included diagram\n\n--8<-- "diagram.md"\n',
            'nested.md': '# Nested example\n\n````markdown\n```mermaid\ngraph LR\n A --> B\n```\n````\n',
            'prose.md': '# Literal markup\n\nAn example of `class="mermaid"` in prose.\n',
            'delimiter.md': '---\ndescription: "Before --- after"\n---\n# Delimiter\n',
            'empty.md': '---\n---\n# Empty metadata\n',
            'bare.md': '---\ntitle:\ndescription:\n---\n# Bare metadata\n',
            'duplicate-a.md': '---\ntitle: Repeated\n---\n# Duplicate A\n',
            'duplicate-b.md': '---\ntitle: Repeated\n---\n# Duplicate B\n',
        }
        for name, content in pages.items():
            path = cls.docs / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        (cls.docs / 'contributing').mkdir()
        for name in ('pattern', 'architecture', 'tool', 'use-case'):
            shutil.copy(ROOT / f'docs/contributing/{name}-template.md', cls.docs / 'contributing')
        for name in ('project-standards/evidence-policy.md', 'start-here/glossary.md'):
            path = cls.docs / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('# ' + path.stem + '\n')
        cls.config = load_config(
            config_file=str(ROOT / 'mkdocs.yml'), docs_dir=str(cls.docs),
            site_dir=str(cls.site), site_url='https://example.org/guide/',
            nav=[{'Home': 'index.md'}, {'One': [{'Overview': 'one/index.md'}]},
                 {'Two': [{'Overview': 'two/index.md'}]}],
            hooks=[str(ROOT / 'scripts/check_site.py')], extra_css=[], extra_javascript=[],
            validation={'nav': {'omitted_files': 'ignore'}},
        )
        cls.config.mdx_configs['pymdownx.snippets']['base_path'] = [str(snippets)]
        build(cls.config)
        cls.errors = check_release(cls.docs, cls.site, cls.config.site_url)

    def built(self, target):
        return (self.site / target).read_text()

    def test_social_titles_match_document_titles(self):
        for target in ('index.html', 'one/index.html', 'two/index.html'):
            with self.subTest(target=target):
                text = self.built(target)
                title = html.unescape(re.search(r'<title>(.*?)</title>', text)[1])
                self.assertEqual(Metadata(text).meta['og:title'], [title])
        self.assertEqual(Metadata(self.built('index.html')).meta['og:title'], [self.config.site_name])

    def test_duplicate_social_titles_rejected(self):
        self.assertTrue(any('duplicate-b.md' in error and 'repeated og:title' in error for error in self.errors))

    def test_rendered_diagrams_match_script_loading(self):
        for name, diagram in (('tilde', True), ('snippet', True), ('nested', False), ('prose', False)):
            with self.subTest(name=name):
                text = self.built(f'{name}/index.html')
                self.assertEqual('<pre class="mermaid"' in text, diagram)
                self.assertFalse([error for error in self.errors if error.startswith(f'{name}.md:')])

    def test_front_matter_uses_mkdocs_parsing(self):
        for name in ('delimiter', 'empty'):
            with self.subTest(name=name):
                self.assertFalse([error for error in self.errors if error.startswith(f'{name}.md:')])
        self.assertEqual(Metadata(self.built('delimiter/index.html')).meta['og:description'], ['Before --- after'])

    def test_bare_metadata_uses_fallbacks(self):
        page = Metadata(self.built('bare/index.html'))
        self.assertEqual(page.meta['og:description'], [self.config.site_description])
        self.assertEqual(page.meta['og:title'], ['Bare metadata - ' + self.config.site_name])

    def test_missing_limits_headings_rejected(self):
        for name in ('use-cases/missing.md', 'tool-reviews/missing.md'):
            with self.subTest(name=name):
                self.assertTrue(any(error.startswith(name + ':') and 'missing Failure Modes' in error for error in self.errors))

    def test_catalog_indexes_do_not_require_design_sections(self):
        for name in ('pet-patterns/index.md', 'pet-architectures/index.md'):
            with self.subTest(name=name):
                self.assertFalse([error for error in self.errors if error.startswith(name + ':')])
