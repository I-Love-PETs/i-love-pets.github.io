# Review Cadence

Some PET guidance changes slowly. Some changes fast enough to become dangerous when stale.

## Slow-Moving Pages

Review yearly unless a major issue is reported:

- Threat models
- Mental models
- Glossary
- PET taxonomy fundamentals
- Contribution principles

## Fast-Moving Pages

Review every six months:

- Cost and latency claims
- Tool maturity
- Deployment readiness
- Vendor or library comparisons
- Benchmark summaries
- AI and RAG guidance

## Page Metadata

Fast-moving pages should include a short review note near the top:

```markdown
!!! info "Review status"
    Last reviewed: YYYY-MM-DD
    Evidence level: Expert judgment
    Snapshot scope: Public tooling and benchmarks available at review time.
```

## Stale Claim Policy

If a claim is plausibly stale and not easy to verify, mark it as needing evidence rather than preserving confident language.
