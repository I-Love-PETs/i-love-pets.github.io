# Pattern Template

Use this template for reusable PET patterns such as private inference, federated analytics, or DP synthetic data release.

```markdown
# Pattern Name

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

## What This Does Not Protect Against

Name output leakage, governance gaps, side channels, poisoning, or other limits.

## Tools And Building Blocks

List building blocks only when you explain their role.

## Operational Complexity

What makes this hard to run?

## Cost Drivers

What drives latency, compute, engineering effort, or review cost?

## Failure Modes

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
