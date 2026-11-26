"""Build real Material pages to exercise release validation and template output."""
import html
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.parse import urljoin

from mkdocs.commands.build import build
from mkdocs.config import load_config

from scripts.check_site import Page, check_site
from scripts.check_release import check_release

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
        (cls.docs / 'assets').mkdir()
        shutil.copy(ROOT / 'docs/assets/social-card.png', cls.docs / 'assets')
        snippets = root / 'includes'
        snippets.mkdir()
        shutil.copy(ROOT / 'includes/decision-guidance.md', snippets)
        (snippets / 'diagram.md').write_text('```mermaid\ngraph LR\n A --> B\n```\n')
        pages = {
            'index.md': '# Welcome\n',
            'excluded.md': '# Excluded draft\n',
            'guidance.md': '# Root guidance\n\n--8<-- "decision-guidance.md"\n',
            'section/guidance.md': '# Section guidance\n\n--8<-- "decision-guidance.md"\n',
            'deep/nested/guidance.md': '# Deep guidance\n\n--8<-- "decision-guidance.md"\n',
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
            'punctuation.md': '---\ntitle: \'Keys & "outputs"\'\ndescription: \'A < B & "quoted"\'\n---\n# Punctuation\n',
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
        for name in ('project-standards/evidence-policy.md', 'start-here/glossary.md', 'benchmarks/scorecards.md'):
            path = cls.docs / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('# ' + path.stem + '\n')
        cls.config = load_config(
            config_file=str(ROOT / 'mkdocs.yml'), docs_dir=str(cls.docs),
            site_dir=str(cls.site), site_url='https://example.org/guide/',
            nav=[{'Start': [{'Home': 'index.md'}]}, {'One': [{'Overview': 'one/index.md'}]},
                 {'Two': [{'Overview': 'two/index.md'}]}],
            hooks=[str(ROOT / 'scripts/site_hooks.py')], exclude_docs='/excluded.md',
            extra={
                'mermaid_script': 'https://cdn.example/mermaid@10.9.1/mermaid.min.js',
                'social_image': 'assets/social-card.png',
                'social_image_alt': 'Privacy engineering & design',
            }, extra_css=[], extra_javascript=[],
            validation={'nav': {'omitted_files': 'ignore'}, 'links': {'absolute_links': 'relative_to_docs'}},
        )
        cls.config.mdx_configs['pymdownx.snippets']['base_path'] = [str(snippets)]
        build(cls.config)
        cls.errors = check_release(cls.config)

    def built(self, target):
        return (self.site / target).read_text()

    def test_social_titles_match_document_titles(self):
        for target in ('index.html', 'one/index.html', 'two/index.html'):
            with self.subTest(target=target):
                page = Page(self.built(target))
                self.assertEqual(len(page.document_titles), 1)
                self.assertEqual(page.meta['og:title'], page.document_titles)

    def test_nested_home_uses_the_site_name_for_all_titles(self):
        page = Page(self.built('index.html'))
        self.assertEqual(page.document_titles, [self.config.site_name])
        self.assertEqual(page.meta['og:title'], [self.config.site_name])
        self.assertEqual(page.meta['twitter:title'], [self.config.site_name])

    def test_release_rejects_a_homepage_with_a_navigation_title(self):
        path = self.site / 'index.html'
        original = path.read_text()
        title = html.escape(self.config.site_name)
        replacements = (
            f'<title>{title}</title>',
            f'<meta property="og:title" content="{title}">',
            f'<meta name="twitter:title" content="{title}">',
        )
        try:
            for tag in replacements:
                with self.subTest(tag=tag):
                    self.assertIn(tag, original)
                    path.write_text(original.replace(tag, tag.replace(title, 'Home - ' + title), 1))
                    self.assertIn('index.md: browser and social titles must match the site name', check_release(self.config))
        finally:
            path.write_text(original)

    def test_social_metadata_escapes_authored_punctuation(self):
        meta = Page(self.built('punctuation/index.html')).meta
        title = [f'Keys & "outputs" - {self.config.site_name}']
        description = ['A < B & "quoted"']
        self.assertEqual(meta['og:title'], title)
        self.assertEqual(meta['twitter:title'], title)
        self.assertEqual(meta['og:description'], description)
        self.assertEqual(meta['twitter:description'], description)

    def test_duplicate_social_titles_rejected(self):
        self.assertTrue(any('duplicate-b.md' in error and 'repeated og:title' in error for error in self.errors))

    def test_social_image_resolves_under_site_base_path(self):
        image_url = urljoin(self.config.site_url, self.config.extra['social_image'])
        self.assertTrue((self.site / 'assets/social-card.png').is_file())
        for target in ('index.html', 'deep/nested/guidance/index.html'):
            with self.subTest(target=target):
                meta = Page(self.built(target)).meta
                self.assertEqual(meta['og:image'], [image_url])
                self.assertEqual(meta['twitter:image'], [image_url])
                self.assertEqual(meta['og:image:alt'], ['Privacy engineering & design'])
                self.assertEqual(meta['twitter:image:alt'], meta['og:image:alt'])
                self.assertEqual(meta['twitter:card'], ['summary_large_image'])

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
        self.assertEqual(Page(self.built('delimiter/index.html')).meta['og:description'], ['Before --- after'])

    def test_bare_metadata_uses_fallbacks(self):
        page = Page(self.built('bare/index.html'))
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

    def test_excluded_docs_are_not_validated(self):
        self.assertFalse([error for error in self.errors if error.startswith('excluded.md:')])

    def test_non_directory_urls_follow_mkdocs(self):
        config = load_config(
            config_file=str(ROOT / 'mkdocs.yml'), docs_dir=str(self.docs),
            site_dir=str(self.site.parent / 'flat-site'), site_url=self.config.site_url,
            use_directory_urls=False, exclude_docs='/excluded.md',
            nav=self.config.nav, hooks=[str(ROOT / 'scripts/site_hooks.py')],
            extra_css=[], extra_javascript=[], validation={'nav': {'omitted_files': 'ignore'}, 'links': {'absolute_links': 'relative_to_docs'}},
        )
        config.mdx_configs['pymdownx.snippets']['base_path'] = self.config.mdx_configs['pymdownx.snippets']['base_path']
        build(config)
        errors = check_release(config)
        self.assertFalse([error for error in errors if 'missing built page' in error or 'canonical' in error])
        site = Path(config.site_dir)
        (site / '404.html').write_text('<meta name="robots" content="noindex"><h1>Page not found</h1>')
        (site / 'robots.txt').write_text(f'Sitemap: {config.site_url}sitemap.xml\n')
        self.assertEqual(check_site(site, config.site_url, config), [])

    def test_mermaid_url_comes_from_config(self):
        self.assertIn(self.config.extra['mermaid_script'], Page(self.built('tilde/index.html')).scripts)

    def test_guidance_links_work_at_any_depth(self):
        for target in ('guidance/index.html', 'section/guidance/index.html', 'deep/nested/guidance/index.html'):
            with self.subTest(target=target):
                page = Page(self.built(target))
                links = [urljoin(page.canonical[0], link) for link in page.targets
                         if 'evidence-policy' in link or 'scorecards' in link]
                self.assertEqual(set(links), {self.config.site_url + 'project-standards/evidence-policy/',
                                              self.config.site_url + 'benchmarks/scorecards/'})
