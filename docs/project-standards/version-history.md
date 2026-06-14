# Version History

!!! info "Release status"
    Status: Current through the v0.6 cleanup release
    Last updated: 2026-06-14
    Scope: Shipped milestones and near-term cleanup work for decision-ready PET guidance.

This page tracks what each site version is meant to change. It is not a changelog for every line edit; it is the editorial map readers and contributors can use to understand the maturity of the guide.

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

## Known Follow-Ups

- Replace hypothetical benchmark examples with measured or literature-backed runs where possible.
- Add source-backed claim notes for high-impact claims in the claim register.
- Revisit fast-moving tool version and performance claims before major releases.
- Add a lightweight stale-content check for pages with dated review metadata.
