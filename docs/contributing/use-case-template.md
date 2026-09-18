# Use Case Template

Use this template when the page starts from a domain need, not from a PET.

```markdown
# Use Case

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

## Decision Context

Who is choosing, and what decision must they make?

## Actors And Data

Name data owners, processors, users, auditors, and affected people. Describe sensitive data and allowed outputs.

## Candidate PETs

| PET | Use this when... | Avoid this when... | Main caveat |
| --- | --- | --- | --- |

## Threat Model

Who is the adversary? What can they observe, change, or infer?

## Recommended Starting Point

State the primary PET and supporting PETs for the most common version of the use case.

## When The Recommendation Changes

What constraints would make another PET better?

## Tradeoffs

Compare privacy, utility, cost, latency, governance, and maturity.

## Does not protect

Name remaining output leakage, excluded adversaries, and controls outside this design.

## Failure modes

What can go wrong even if the PET works?

## Evaluation Checklist

What must be measured or reviewed?

## Practical Next Step

Give one small next action: benchmark, threat-model workshop, data-flow diagram, or prototype.
```

## Review Checklist

- Does the page start from the use-case decision rather than a favorite PET?
- Are candidate PETs compared honestly?
- Does it include when the recommendation changes?
- Are output leakage and governance risks included?
- Is there a practical next step?

Use the [Evidence Policy](../project-standards/evidence-policy.md) and [glossary](../start-here/glossary.md) without inventing new labels. Keep page-specific assumptions explicit; shared editorial guidance may use the include in `includes/decision-guidance.md`.
