# Federated Analytics

## Motivating Example

A network of hospitals wants to measure readmission rates and treatment outcomes without sending patient records to a central database. The useful output is a set of aggregate metrics, not a trained model.

## Problem

Multiple parties need shared statistics while keeping raw data local or inside controlled environments. The hard part is not computing an average; it is controlling small-cell leakage, inconsistent definitions, repeated queries, and who can see the output.

## When To Use

- The output is an aggregate, report, metric, or dashboard.
- Raw records cannot centralize, or centralization would create avoidable risk.
- Participants can run local queries or submit protected aggregates.
- The collaboration can define minimum cohort sizes, query limits, and output review.

## When Not To Use

- Do not use federated analytics if the real need is a trained model. Use FL or centralized training.
- Do not use it if outputs can identify small groups and nobody will suppress, group, or noise them.
- Do not use it when parties disagree on metric definitions; fix semantics first.
- Do not claim privacy because raw data stayed local. Aggregate outputs can still leak.

## Architecture

1. Coordinator publishes a query specification, data schema, and release policy.
2. Participants validate the query against local policy and run it locally.
3. Local results are returned directly, via secure aggregation, through MPC, or inside a clean room.
4. The coordinator applies thresholds, DP noise if needed, and output review.
5. Released metrics include provenance, cohort sizes, and caveats.

## Threat Model

| Actor | Concern |
| --- | --- |
| Coordinator | May infer sensitive information from small results or repeated queries |
| Participant | May submit incorrect, stale, or adversarial data |
| Other participants | May learn commercially or clinically sensitive facts from outputs |
| External attacker | May compromise credentials, logs, or dashboards |

## Privacy Properties

- Raw records can remain local.
- Secure aggregation or MPC can hide individual participant contributions from the coordinator.
- DP can bound the contribution of a privacy unit to released outputs.
- Thresholds and output review reduce small-cell disclosure.

## What This Does Not Protect Against

- Bad metric definitions.
- Leakage through tiny cohorts or repeated queries.
- A final output that intentionally reveals the sensitive fact.
- Compromised local systems.
- Collusion beyond the stated protocol assumptions.

## Tools And Building Blocks

- Local query runners with schema validation.
- Secure aggregation for participant-level contribution hiding.
- MPC for joint computations without one trusted operator.
- Clean rooms for governed workflows and auditability.
- DP mechanisms, minimum thresholds, and output review.

## Operational Complexity

Medium. The computation may be simple, but the program needs participant onboarding, schema alignment, query approval, output policy, audit logs, and release governance.

## Cost Drivers

- Number of participants and query frequency.
- Local data engineering and schema harmonization.
- Secure aggregation or MPC overhead.
- Review cost for sensitive outputs.
- DP utility loss and accounting.

## Failure Modes

- Small-cell results reveal a patient group, branch, or business line.
- Participants compute the same metric differently.
- Repeated queries reconstruct sensitive values.
- Dashboards or logs expose raw local results.
- Governance approves more output than the privacy design can justify.

## Evaluation Checklist

- Are privacy units and allowed outputs defined?
- Are minimum cohort sizes enforced?
- Are repeated queries tracked?
- Are local schemas and metric definitions tested?
- Does the output review include small groups and rare events?
- Is the coordinator allowed to see participant-level results?

## Open Research Problems

- Benchmarks for federated analytics on realistic small cohorts.
- Query planners that predict leakage before running a query.
- Usable DP accounting for repeated organizational analytics.
- Robustness checks for incorrect or adversarial participant results.

## Related Pages

- [By data movement](../pet-compass/by-data-movement.md)
- [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md)
- [Differential privacy problems](../fix-my-itch/differential-privacy.md)
