# Review Cadence

Some PET guidance changes slowly. Some changes fast enough to become dangerous when stale.

## Slow-Moving Pages

Review yearly unless a major issue is reported:

- threat models;
- mental models;
- glossary;
- PET taxonomy fundamentals;
- contribution principles.

## Fast-Moving Pages

Review every six months:

- cost and latency claims;
- tool maturity;
- deployment readiness;
- vendor or library comparisons;
- benchmark summaries;
- AI and RAG guidance.

## Triggered Reviews

Review sooner when:

- a major PET tool changes capabilities or licensing;
- a deployment claim is corrected, withdrawn, or independently evaluated;
- a new attack changes a practical threat model;
- a benchmark result contradicts site guidance;
- a user reports that a recommendation led to a bad shortlist.

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

If a stale claim materially affects a recommendation, soften or remove the recommendation until the claim is reviewed.
