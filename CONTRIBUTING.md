# Contributing

I ❤️ PETs is a practical field guide, not an awesome list.

## Contribution Principles

- Prefer explanation over link dumping.
- Every pattern must explain when not to use it.
- Every architecture must state a threat model.
- Every research problem must be actionable.
- Avoid hype.
- Prefer evidence and tradeoffs.
- Date claims that may become stale.
- Mark unsourced tradeoff claims as expert judgment or needs evidence.

## What Makes A Good Contribution

A good contribution helps someone make a decision. It states the problem, assumptions, tradeoffs, failure modes, and next step.

The primary reader is a privacy engineer, platform engineer, or architect scoping a PET-based system. Write for someone who must decide what to shortlist, what to measure, and what could break.

## Evidence Expectations

Claims about cost, latency, maturity, deployment readiness, security properties, or tooling quality should include an evidence level:

- **Measured**: benchmarked with workload, environment, and date.
- **Deployment-backed**: supported by a named deployment, postmortem, or case study.
- **Literature-backed**: supported by papers, standards, or technical reports.
- **Expert judgment**: editorial judgment that should be reviewed.
- **Needs evidence**: useful but not yet decision-grade.

Fast-moving pages should include a last-reviewed date and should avoid timeless wording for snapshot claims.

## Local Development

Use Python 3.12, matching CI.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Validate Before Opening A PR

Run the same checks CI runs on every pull request and before deployment:

```bash
pip install -r requirements.txt
pymarkdown --disable-rules '*' --enable-rules MD010,MD040,MD047 scan -r docs README.md CONTRIBUTING.md
python3 -m unittest discover -s tests
python3 scripts/check_internal_links.py
python3 scripts/check_nav_coverage.py
mkdocs build --strict --clean
python3 scripts/check_rendered_shortcodes.py
python3 scripts/check_site.py
```

The Markdown check requires language tags on fenced code (MD040), forbids hard tabs (MD010), and requires a final newline (MD047). Other style rules remain off to preserve the guide's tables, Material admonitions, and existing formatting. MkDocs validates rendered Markdown links and anchors; the built-site check also catches missing local assets and broken 404 recovery links.

`requirements.txt` pins the Python 3.12 build and validation environment, including transitive dependencies. Update pins together in an isolated environment and rerun the checks above before opening a dependency PR.

MkDocs core generates `sitemap.xml` and `sitemap.xml.gz` from `site_url`; no sitemap plugin is needed. `docs/robots.txt` must point to that canonical sitemap. The error-page hook renders `docs/404.md` through `overrides/404.html` so GitHub Pages receives a root-aware, non-indexed `404.html`. It is intentionally absent from normal navigation and the sitemap. If the site URL changes, update the absolute recovery links in `docs/404.md` too.

Mermaid uses the configured SuperFences renderer and JavaScript in `mkdocs.yml`. The `mkdocs-mermaid2-plugin` package is not needed. Check diagrams in a browser after changing that configuration.
