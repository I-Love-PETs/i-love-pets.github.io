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

A review date applies to the stated snapshot scope. For a focused update, date the claim or subsection actually checked. Source edits, publication dates, and checks of product documentation are different from measurements of a workload.

Older deployment pages may still have a reference date or claim-level notes. Add the scoped review block as part of the next substantive review. The release validator checks structure and rendered output. Verification of facts and source currency is an editorial check.

## Stale Claim Policy

If a claim is plausibly stale and not easy to verify, mark it as needing evidence rather than preserving confident language.

If a stale claim materially affects a recommendation, soften or remove the recommendation until the claim is reviewed.
