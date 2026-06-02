# Private Set Intersection

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

## Tools And Building Blocks

OPRFs, ECDH PSI, circuit PSI, MPC for post-intersection computation, and output policies.

## Common Failure Modes

Identifier normalization leakage, frequency leakage, small intersections, replayed queries, and unclear deletion policies.

## Open Research Problems

Better PSI developer experience, malicious-secure protocols at production scale, and safer post-PSI analytics.

## Related Pages

MPC, clean rooms, advertising use cases, collusion.
