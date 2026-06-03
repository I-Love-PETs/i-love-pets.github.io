# Federated Learning

Federated learning is useful when raw data cannot centralize, but it is often oversold as privacy by default. These problems focus on making FL measurable, safer, and easier to operate.

## Realistic Cross-Silo Non-IID Benchmarks

| Field | Card |
| --- | --- |
| Problem | How do we benchmark FL on realistic cross-silo non-IID data? |
| The itch | Many FL papers use convenient partitions that do not look like hospitals, banks, or agencies with different populations, label practices, missingness, and infrastructure. |
| Why it matters | Teams choose FL based on average accuracy, then discover that smaller or unusual sites get worse models. |
| Current workaround | Simulate non-IID splits from centralized datasets or report one global metric. |
| Why the workaround is insufficient | It hides per-site failure, operational dropouts, label mismatch, and governance constraints. |
| What good progress would look like | A benchmark suite with site-level metrics, realistic heterogeneity, dropout patterns, and documented data-generation assumptions. |
| Difficulty | Medium |
| Good for | ML researcher, benchmark maintainer, privacy engineer |
| Related PETs | FL, secure aggregation, DP |
| Possible first contribution | Reproduce three FL baselines on a public dataset with hospital-like partitions and report per-site utility, fairness, and communication cost. |

## Poisoned Updates Without Inspecting Private Data

| Field | Card |
| --- | --- |
| Problem | How can FL systems detect poisoned updates without inspecting private data or raw client updates? |
| The itch | Secure aggregation and privacy controls reduce coordinator visibility exactly when debugging and abuse detection need visibility. |
| Why it matters | Malicious or compromised participants can degrade a shared model or insert backdoors. |
| Current workaround | Inspect updates in less-private settings, use simple norm clipping, or rely on participant vetting. |
| Why the workaround is insufficient | It conflicts with privacy goals and misses adaptive attacks. |
| What good progress would look like | Robust aggregation and anomaly signals that work with secure aggregation constraints and report false-positive cost. |
| Difficulty | Hard |
| Good for | ML researcher, systems builder, privacy engineer |
| Related PETs | FL, secure aggregation, DP, TEEs |
| Possible first contribution | Build a small secure-aggregation-compatible poisoning benchmark with norm, sign, and backdoor attacks plus documented detection limits. |

## Low-Infrastructure FL For Small Organizations

| Field | Card |
| --- | --- |
| Problem | How can small organizations participate in FL without dedicated infrastructure teams? |
| The itch | Cross-silo FL assumes participants can run training jobs, manage keys, monitor rounds, and recover from failure. Many clinics, schools, nonprofits, and smaller banks cannot. |
| Why it matters | FL can exclude exactly the organizations whose data would improve representativeness. |
| Current workaround | Limit participation to large sites or centralize data after all. |
| Why the workaround is insufficient | It reduces diversity and makes privacy-preserving collaboration a privilege of large institutions. |
| What good progress would look like | A minimal participant appliance or managed workflow with clear security boundaries, upgrade paths, and failure recovery. |
| Difficulty | Medium |
| Good for | Systems builder, privacy engineer, ML engineer |
| Related PETs | FL, secure aggregation, TEEs |
| Possible first contribution | Prototype a containerized FL participant with reproducible setup, health checks, local data validation, and round-level audit logs. |

## Honest Claim Templates For FL

| Field | Card |
| --- | --- |
| Problem | How should teams state FL privacy claims without implying that FL alone protects training data? |
| The itch | Product pages often say "data never leaves your site" and stop there, while gradients, metrics, and model releases can leak. |
| Why it matters | Buyers, regulators, and internal reviewers make decisions from incomplete claims. |
| Current workaround | Add broad caveats in legal or security review documents. |
| Why the workaround is insufficient | Caveats are not tied to architecture choices, threat models, or measurable controls. |
| What good progress would look like | A claim template that maps FL architecture choices to allowed and disallowed privacy statements. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, policy researcher, technical writer |
| Related PETs | FL, secure aggregation, DP |
| Possible first contribution | Compare ten FL descriptions and rewrite them with explicit protected artifacts, adversaries, and residual risks. |
