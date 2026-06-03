# Project Standards

I Love PETs is a curated field guide. Its value comes from judgment that readers can inspect, not from collecting every link.

## Quality Bar

Every decision-support page should help a reader answer:

> What should I believe, why should I believe it, what might have changed, and what should I verify before building?

Good pages are practical, dated, scoped, and honest about failure. A page is not ready if it only explains what a PET is.

## Required Page Qualities

| Quality | Standard |
| --- | --- |
| Decision support | The page says when to use, when not to use, and what would change the recommendation. |
| Threat model | The page names adversaries, protected assets, assumptions, and outputs. |
| Failure modes | The page explains how the PET can fail or be misused. |
| Evidence | Claims are sourced, measured, labeled as expert judgment, or placed in the claim register. |
| Specificity | Examples name actors, data, outputs, and operational constraints. |
| Anti-hype | The page does not imply a PET solves governance, security, utility, or output leakage by itself. |

## Minimum Useful Page

Every page should contain at least one of:

- decision table;
- worked example;
- failure mode;
- checklist;
- concrete research problem;
- tradeoff matrix.

## Writing Rules

Prefer:

- "Use this when..."
- "Avoid this when..."
- "This breaks when..."
- "This does not protect against..."
- "A good first experiment would be..."
- "The hidden cost is..."

Avoid:

- generic textbook prose;
- unqualified "privacy-preserving" claims;
- paper dumps;
- tool lists without fit, threat model, or limitations;
- empty sections waiting for future content.

## Review Gate

Before opening a PR, check:

- `mkdocs build` succeeds.
- Navigation still reaches the changed page.
- Internal links point to existing pages and anchors.
- No empty headings remain.
- The page contains at least one concrete decision aid.
- Any deployment or tool claim is sourced or explicitly labeled as uncertain.

## What Counts As Progress

Improving one important page is better than adding five shallow pages. A useful PR makes a reader more capable of choosing, rejecting, evaluating, or debugging a PET.
