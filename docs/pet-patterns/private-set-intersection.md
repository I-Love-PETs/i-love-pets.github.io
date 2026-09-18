---
description: "Private Set Intersection: protected assets, adversaries, allowed outputs, leakage, assumptions, non-goals, and checks for a concrete design review."
---

# Private Set Intersection

## Decision framing

| Field | Scope |
| --- | --- |
| Protected asset | Nonmatching identifiers held by each party. |
| Adversary | Other protocol parties within the selected honest-but-curious or malicious security model and collusion bound. |
| Allowed output | An agreed intersection, intersection count, or downstream aggregate to named recipients; these are different protocol choices. See [allowed output](../start-here/glossary.md#allowed-output). |
| Leakage surface | Set sizes, the permitted overlap, repeated queries, identifier handling, and protocol metadata. See [leakage](../start-here/glossary.md#leakage). |
| Assumptions | The protocol matches the adversary model; identifiers are normalized consistently; query and output policies constrain probing. |
| Non-goals | Hiding the agreed intersection from its recipients, proving that inputs are legitimate, or preventing downstream profiling. |

--8<-- "decision-guidance.md"

## Problem

Two or more parties need to learn which records overlap without revealing nonmatching records.

## When To Use

Use PSI for cohort matching, fraud signals, contact discovery, and measurement joins.

## When Not To Use

Avoid PSI if revealing the intersection is too sensitive or repeated matching enables profiling.

## Typical Architecture

Parties encode records, run a PSI protocol, and reveal the intersection or aggregate statistics over the intersection.

## Threat Model

Commonly honest-but-curious parties. Malicious variants are needed when parties may submit malformed inputs.

## Privacy Properties

Nonmatching elements are hidden under protocol assumptions. The intersection and its size may still leak sensitive information.

## Does not protect

- Sensitive facts in the permitted overlap or count.
- Probing with legitimate-looking but unauthorized identifiers.
- Repeated-query inference or misuse of the match set.

## Tools And Building Blocks

OPRFs, ECDH PSI, circuit PSI, [MPC](../start-here/glossary.md#mpc) for post-intersection computation, and output policies.

<span id="common-failure-modes"></span>

## Failure modes

Identifier normalization leakage, frequency leakage, small intersections, replayed queries, and unclear deletion policies.

## Open Research Problems

Better PSI developer experience, malicious-secure protocols at production scale, and safer post-PSI analytics.

## Related Pages

- [MPC analytics](../pet-architectures/mpc-analytics-pipeline.md)
- [Clean rooms](../start-here/glossary.md#clean-room)
- [Advertising use cases](../use-cases/advertising.md)
- [Collusion](../threat-models/collusion.md)
