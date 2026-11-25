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

<span id="when-not-to-use"></span>

## Do not use PSI when

- **The match identities themselves are sensitive.** For example, if two services may learn how many users overlap but neither may learn who, choose a protocol that returns only the count. Check whether small counts still reveal membership.
- **Participants can submit arbitrary identifiers or retry against changing cohorts.** A correct protocol can still answer an unauthorized membership question. Tie input eligibility to an approved source, bound set size, and restrict and audit repeated queries.
- **The only permitted output is a downstream statistic.** Compute the statistic over the join inside the protected computation so the recipient never gets the intermediate match set. See the [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md).

## Typical Architecture

Parties encode records, run a PSI protocol, and reveal the intersection or aggregate statistics over the intersection.

## Threat Model

Use a malicious-secure variant if parties may deviate from the protocol. Input authorization is a separate control: a valid protocol input can still be fabricated or unauthorized.

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
