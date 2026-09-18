---
description: "Read the v1.0 definition of done, release-readiness checks, earlier milestones, and remaining evidence gaps."
---

# Version History

!!! info "Release status"
    Status: v1.0 release candidate; publication follows review and merge
    Last updated: 2026-09-18
    Scope: v1.0 acceptance criteria, shipped milestones, and explicit evidence follow-ups.

This page tracks what each site version is meant to change. It is not a changelog for every line edit; it is the editorial map readers and contributors can use to understand the maturity of the guide.

## v1.0 definition of done

v1.0 means a stable decision framework, a consistent evidence model, usable core
content, contributor conventions, and a trustworthy publishing baseline. It does
not mean complete PET coverage or that every workload claim has measured evidence.

- Every pattern and architecture states Protected asset, Adversary, Allowed output, Leakage surface, Assumptions, and Non-goals, with protection limits and failure modes.
- Decision-critical claims use the existing Evidence Policy; unsupported guidance stays visibly Expert judgment or Needs evidence.
- The homepage and onboarding lead readers to a shortlist, a pattern, a worked decision, or an open problem.
- Contributor templates preserve these conventions and terminology.
- Publishing checks cover internal links, navigation, diagrams, social metadata, sitemap, robots, and the error page.

### v1.0 release-readiness checks

Run the commands in [Contributing](../contributing/index.md) and the repository’s
`CONTRIBUTING.md`; CI and deployment run the same automated gates.

- Install `requirements.txt`; run the strict MkDocs build, Markdown lint, and validator tests.
- Check source and built internal links and anchors, navigation coverage, and local assets.
- Check framing coverage, contributor structure, rendered evidence notes, and primary-path placeholder markers.
- Check canonical URLs and OpenGraph/Twitter title and description metadata, including punctuation escaping.
- Confirm Mermaid loads only on diagram pages and every diagram renders in a browser.
- Check sitemap (including compressed copy), robots, and nested-path 404 recovery.
- Review the homepage, chooser, a pattern, and diagram pages at mobile and desktop widths in light and dark mode. Check navigation, table scrolling, readable diagrams, focus visibility, and theme switching.

Browser review is a release gate, not something a successful static build proves.
Record the browser, viewports, inspected pages, and any limits in the release PR.
Templates under Contributing are intentionally instructional; primary reader paths
must not contain unfilled template prompts or placeholder dates.

## v0.9 — Quality and SEO baseline

Merged before v1.0: pinned build dependencies, evidence labels for benchmark and
tool guidance, expanded benchmark methods, strict publishing checks, and a
canonical sitemap, robots file, and friendly 404 page.

## v0.7 — Evidence-Backed Guidance

v0.7 moves deployment and benchmark guidance from strong editorial advice toward sourced field-guide evidence. The goal is to help readers distinguish measured deployments, pilots, vendor case studies, proposed use cases, and illustrative examples before they make decisions.

| Area | Shipped improvement |
| --- | --- |
| Evidence policy | Add source-quality labels and clearer deployment maturity labels. |
| Deployments | Separate production/recurring deployments, pilots, vendor case studies, and proposed use cases on domain pages. |
| Deep dives | Add source-backed studies for EXAM COVID-19 federated learning and Japanese bank fraud-detection FL. |
| Existing deep dives | Add source-quality fields to the snapshot tables. |
| Benchmarks | Add benchmark source-quality labels and mark illustrative values as Unsourced / illustrative. |
| Claim register | Refresh the claim snapshot around deployment maturity, benchmark evidence, and remaining unresolved claims. |

## v0.6 — Consistency And Evidence Hygiene

v0.6 is a cleanup release after the larger v0.3-v0.5 content expansion. The goal is to make the site easier to trust: no hidden sections, no stale release language, and no illustrative benchmark values that look like measured results.

| Area | Shipped improvement |
| --- | --- |
| Navigation | Add Tool Reviews to the main nav and keep every Markdown page reachable. |
| Homepage | Route readers to Worked Decisions, Tool Reviews, and Benchmark Example Runs. |
| Evidence hygiene | Reframe benchmark examples as hypothetical scorecard exercises unless a value is measured or literature-backed. |
| Claim register | Update the snapshot scope to the current evidence backlog. |
| Reader paths | Remove stale wording that described the decision tree as a single diagram. |
| CI | Add navigation coverage checking and build with MkDocs strict mode so warnings fail early. |

## v0.5 — Tool Reviews And Worked Evaluation

v0.5 added practical evaluation artifacts around PET tools and decision workflows.

| Area | Shipped improvement |
| --- | --- |
| Tool reviews | Added worked examples for Flower, OpenDP, Microsoft SEAL, and confidential-computing platforms. |
| Tool evaluation | Added a framework and template for reviewing tools by architecture fit, threat model, evidence, operations, and first benchmark. |
| Worked decisions | Added concrete scenario pages for hospital model training, cross-bank fraud detection, private RAG, synthetic data release, private model inference, and public-sector statistics. |
| Benchmarks | Added example scorecard runs to show how benchmark templates can be applied to realistic workloads. |

## v0.4 — Decision Kit Foundations

v0.4 made I ❤️ PETs more usable as a decision kit: clearer use cases, reusable benchmark scorecards, stronger architecture review, and better evidence discipline.

| Area | Shipped improvement |
| --- | --- |
| Use cases | Turned domain summaries into playbooks with scenarios, PET stacks, non-use guidance, failure modes, and measurements. |
| Benchmarks | Added scorecards for private RAG, private inference, cross-silo FL, synthetic data release, and federated/MPC analytics. |
| Architectures | Added trust-boundary reviews, assumptions, non-protections, and evaluation checklists. |
| Evidence | Strengthened claim states, dated review workflow, and claim-register backlog. |
| Tools | Added a framework for evaluating PET tools by fit, threat model, evidence, operations, and first benchmark. |
| Start Here | Improved onboarding with wrong-assumption checks, routing, and practical glossary examples. |
| Site quality | Added internal-link checking and kept navigation aligned with new guidance. |

## Release Checklist

- `mkdocs build --strict --clean` passes.
- Internal-link check passes.
- Navigation coverage check passes.
- New navigation entries point to existing pages and every docs page is intentionally reachable.
- Decision pages include at least one concrete table, checklist, worked example, or scorecard.
- No page claims a PET solves privacy without naming assumptions and outputs.
- Illustrative examples cannot be mistaken for measured production evidence.
- Deployment and benchmark claims carry source-quality labels when they affect a decision.

## Known Follow-Ups

- Replace hypothetical benchmark examples with measured or literature-backed runs where possible.
- Add source-backed claim notes for high-impact claims in the claim register.
- Revisit fast-moving tool version and performance claims before major releases.
- Add a lightweight stale-content check for pages with dated review metadata.
