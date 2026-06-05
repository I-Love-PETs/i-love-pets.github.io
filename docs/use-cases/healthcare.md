# Healthcare

Healthcare PET decisions must account for patient confidentiality, clinical utility, institutional governance, rare cohorts, and uneven data quality.

## Scenario Playbook

| Scenario | Primary PET | Supporting PETs | Why | What can go wrong | What to measure |
| --- | --- | --- | --- | --- | --- |
| Hospitals train a shared model without pooling records | Cross-silo FL | Secure aggregation, DP, robust aggregation | Raw patient data can remain local while sites contribute to a shared model | Update leakage, poisoning, non-IID data, weak local operations | Per-site utility, subgroup performance, round size, dropout rate, memorization risk |
| Hospitals compute quality metrics | Federated analytics | DP, thresholds, output review | Metrics can be computed locally and aggregated | Small cohorts reveal patients or underperforming sites | Minimum cohort sizes, metric consistency, repeated-query risk |
| Researchers identify eligible patients across institutions | PSI or clean room | Audit logs, consent/purpose controls, DP counts | Matching can avoid broad list sharing | The match itself may be sensitive | Match precision/recall, allowed output, query frequency |
| A public research dataset is needed | DP synthetic data | Memorization tests, utility benchmarks | A data-like artifact can support exploration without raw release | Rare records copied or utility destroyed | Nearest-neighbor risk, membership inference, downstream task utility |

## Use This When

- Raw records cannot centralize across institutions.
- The output has a clear clinical or research purpose.
- Participating sites can validate data definitions and local performance.
- The team can review small cohorts, rare diseases, and site-specific leakage.

## Avoid This When

- The model will be trusted clinically without local validation.
- The PET is being used to bypass consent, governance, or data-use limits.
- The cohort is so small that any aggregate or match reveals sensitive facts.
- Sites cannot run, monitor, or audit the local component.

## Recommended Starting Stack

For multi-hospital model training, start with **cross-silo FL + secure aggregation**, then add **DP** only after testing utility at a defensible privacy budget.

For healthcare metrics, start with **federated analytics + thresholds**, then add **DP** for public or repeated releases.

## Failure Modes

- A global model works for large hospitals and fails at smaller sites.
- Secure aggregation hides poisoned or broken updates.
- Synthetic data preserves rare patient traces.
- Quality metrics leak performance for tiny departments.
- Logs and dashboards expose information the PET protected in transit.

## Evaluation Checklist

- What is the privacy unit: patient, encounter, provider, hospital, or site?
- Are rare cohorts suppressed, grouped, or protected with DP?
- Does evaluation report per-site and subgroup performance?
- Are clinical workflow and liability reviewed?
- Are logs, model outputs, and dashboards included in the threat model?

## Related Pages

- [Cross-silo federated learning](../pet-patterns/cross-silo-federated-learning.md)
- [Federated analytics](../pet-patterns/federated-analytics.md)
- [Healthcare deployments](../deployments/healthcare.md)
