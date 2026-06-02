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

```bash
pip install -r requirements.txt
mkdocs serve
```

## Validate Before Opening A PR

```bash
mkdocs build
```

Also check navigation, links, empty pages, and Mermaid diagrams.
