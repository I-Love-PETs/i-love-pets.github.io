# Pattern Template

Use this template for reusable PET patterns such as private inference, federated analytics, or DP synthetic data release.

```markdown
# Pattern Name

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

## Motivating Example

Name the actors, data, output, and constraint.

## Problem

What recurring design problem does this pattern solve?

## When To Use

- Use this when...

## When Not To Use

- Avoid this when...

## Architecture

Describe the main actors, data flow, control points, and trust boundaries.

## Threat Model

Who is the adversary? What can they see or change? What output is allowed?

## Privacy Properties

What does the pattern protect, and under which assumptions?

## Does not protect

Name output leakage, governance gaps, side channels, poisoning, or other limits.

## Tools And Building Blocks

List building blocks only when you explain their role.

## Operational Complexity

What makes this hard to run?

## Cost Drivers

What drives latency, compute, engineering effort, or review cost?

## Failure modes

- This breaks when...

## Evaluation Checklist

- What should be measured before launch?

## Open Research Problems

Name concrete open problems, not broad research areas.

## Related Pages

Link only to pages that help the reader decide or implement.
```

## Review Checklist

- Does it say when NOT to use the pattern?
- Does it state a threat model?
- Does it explain failure modes?
- Does it avoid pretending the PET solves everything?
- Does it include evaluation criteria?

Use the [Evidence Policy](../project-standards/evidence-policy.md) and [glossary](../start-here/glossary.md) without inventing new labels. Keep page-specific assumptions explicit; shared editorial guidance may use the include in `includes/decision-guidance.md`.
