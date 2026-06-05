# Finance

Finance PET decisions are shaped by adversarial behavior, regulatory obligations, customer confidentiality, commercial sensitivity, and the need for auditable decisions.

## Scenario Playbook

| Scenario | Primary PET | Supporting PETs | Why | What can go wrong | What to measure |
| --- | --- | --- | --- | --- | --- |
| Banks detect fraud across institutions | MPC or federated analytics | PSI, DP thresholds, clean-room audit | Fraud patterns cross institutional boundaries | Collusion assumptions fail, false positives rise, latency misses fraud windows | Detection lift, false positives, latency, smallest released cohort |
| Institutions find overlapping risky entities | PSI | Output limits, audit logs, DP counts | Nonmatches can remain hidden | The intersection can reveal investigations | Match precision, repeat-query controls, allowed use |
| Banks train a shared fraud model | Cross-silo FL | Secure aggregation, robust aggregation, DP | Raw transaction data stays local | Poisoned updates, entity-resolution mismatch, unfair outcomes | Per-bank utility, drift, poisoning resilience, update leakage |
| Risk teams compare portfolio metrics | Federated analytics or clean room | DP, thresholds, governance | Peer benchmarks can be computed without raw portfolio sharing | Aggregates reveal business strategy | Cohort sizes, query history, commercial sensitivity |

## Use This When

- The collaboration has a specific fraud, AML, risk, or compliance output.
- Parties can agree on entity resolution and permitted use.
- Auditability matters as much as computation.
- Malicious or strategic behavior is part of the threat model.

## Avoid This When

- The parties cannot agree on output policy or downstream use.
- Low latency is required but the PET has not been benchmarked.
- The design assumes all participants behave honestly.
- Entity resolution is unsolved but treated as a minor preprocessing step.

## Recommended Starting Stack

For cross-bank fraud signals, start with **PSI for overlap** or **MPC/federated analytics for joint metrics**. Move to **FL** only when the real output is a shared model.

## Failure Modes

- A party uses repeated PSI queries to learn another party's customer base.
- An aggregate reveals a bank's exposure or investigation focus.
- A malicious participant poisons a shared model.
- False positives harm customers and create compliance risk.
- Vendor case studies overstate production maturity.

## Evaluation Checklist

- Are parties honest-but-curious, malicious, or strategically adversarial?
- Is the match set itself sensitive?
- What outputs are analysts allowed to act on?
- Can the system explain false positives and disputed decisions?
- Are query limits, logs, and abuse monitoring in place?

## Related Pages

- [Private set intersection](../pet-patterns/private-set-intersection.md)
- [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md)
- [Finance deployments](../deployments/finance.md)
