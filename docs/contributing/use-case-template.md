# Use Case Template

Use this template when the page starts from a domain need, not from a PET.

```markdown
# Use Case

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

## Failure Modes

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
