# Federated Analytics

## Problem

Multiple parties need aggregate metrics, but raw event or user data should stay local.

## When To Use

Use this pattern for counts, rates, sketches, cohort metrics, and measurement where the final answer is an aggregate.

## When Not To Use

Do not use it when individual-level outputs are required or when small cohorts make the aggregate itself identifying.

## Typical Architecture

Local clients or silos compute partial metrics. A coordinator aggregates partials through secure aggregation, MPC, or a governed clean-room workflow.

## Threat Model

Usually honest-but-curious coordinator and participants, with optional protection against collusion depending on aggregation design.

## Privacy Properties

Raw data remains local. Individual partials may be hidden with secure aggregation. Differential privacy can limit output leakage.

## Tools And Building Blocks

Secure aggregation, MPC, thresholding, DP mechanisms, audit logs, and query governance.

## Common Failure Modes

Small-cell leakage, repeated-query differencing, malicious local reports, weak participant authentication, and unclear output policies.

## Open Research Problems

Usable privacy accounting for repeated federated measurements, robust aggregation under malicious clients, and benchmark suites for output leakage.

## Related Pages

PET Compass, threat models, benchmarks, deployments.
