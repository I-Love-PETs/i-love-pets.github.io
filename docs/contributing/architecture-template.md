# Architecture Template

Use this template when the page explains a concrete system shape rather than a general pattern.

```markdown
# Architecture Name

## Decision framing

| Field | Scope |
| --- | --- |
| Protected asset | Name the data or artifacts to protect. |
| Adversary | Name capabilities, corruption model, and collusion threshold. |
| Allowed output | Name the result, recipients, and permitted query frequency. |
| Leakage surface | Include outputs, intermediates, metadata, logs, and side channels. |
| Assumptions | State concrete conditions on keys, hardware, parties, and accounting. |
| Non-goals | State excluded attacks and properties; do not imply complete privacy. |

## Evidence and review

State Last reviewed and the scope of the review. Use the existing Evidence Policy
levels: Measured, Deployment-backed, Literature-backed, Expert judgment, Needs evidence.
Use its source-quality labels: Primary / official, Peer-reviewed / academic,
Independent analysis, Vendor case study, Press / secondary, Unsourced / illustrative.
Attach a source and its limits to each decision-critical factual claim. Explain
why editorial guidance is plausible and what would change it. Do not promote
illustrative examples to measured evidence.

## Goal

What should the architecture achieve?

## Actors

Name every actor: data owner, model owner, coordinator, key holder, auditor, user, platform operator, and attacker where relevant.

## Data Flow

Show what moves: records, identifiers, updates, ciphertexts, embeddings, prompts, logs, model weights, and outputs.

## Trust Boundaries

Where does trust change? Who controls code, keys, policy, logs, and outputs?

## Assumptions

List hardware trust, collusion thresholds, participant behavior, legal constraints, and operational assumptions.

## PET Stack

Explain the role of each PET. Do not just list names.

## Privacy Properties

What is protected, from whom, and under which assumptions?

## Does not protect

Name output leakage, compromised endpoints, side channels, weak governance, or bad data quality.

## Deployment Notes

What must be configured, monitored, rotated, audited, or reviewed?

## Tradeoffs

State privacy, utility, cost, latency, and operational tradeoffs.

## Failure modes

How does the design fail in practice?

## Evaluation Checklist

What should be tested before production?
```

## Review Checklist

- Are actors named?
- Are trust boundaries explicit?
- Are data flows clear?
- Are assumptions listed?
- Are operational risks included?

Use the [Evidence Policy](../project-standards/evidence-policy.md) and [glossary](../start-here/glossary.md) without inventing new labels. Keep page-specific assumptions explicit; shared editorial guidance may use the include in `includes/decision-guidance.md`.
