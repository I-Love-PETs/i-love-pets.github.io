# Architecture Template

Use this template when the page explains a concrete system shape rather than a general pattern.

```markdown
# Architecture Name

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

## What This Does Not Protect Against

Name output leakage, compromised endpoints, side channels, weak governance, or bad data quality.

## Deployment Notes

What must be configured, monitored, rotated, audited, or reviewed?

## Tradeoffs

State privacy, utility, cost, latency, and operational tradeoffs.

## Failure Modes

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
