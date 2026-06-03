# Synthetic Data

Synthetic data can be useful for testing, education, prototyping, and some modeling workflows. It is not automatically anonymous, safe, or useful.

## Memorization Detection

| Field | Card |
| --- | --- |
| Problem | How do we detect memorization in synthetic data? |
| The itch | Generators can copy rare records, outliers, or sensitive combinations while still producing data that looks synthetic. |
| Why it matters | A public release can expose people, companies, or sensitive events. |
| Current workaround | Run nearest-neighbor checks, spot-check samples, or rely on the generator type. |
| Why the workaround is insufficient | Simple checks miss semantic copying, rare subgroup leakage, and adaptive attackers. |
| What good progress would look like | A practical memorization test suite with multiple attacks, subgroup analysis, and release-review thresholds. |
| Difficulty | Medium |
| Good for | Privacy engineer, ML researcher, benchmark maintainer |
| Related PETs | Synthetic data, DP |
| Possible first contribution | Evaluate three memorization tests on a public dataset with injected rare records and report which tests catch them. |

## Downstream Utility Measurement

| Field | Card |
| --- | --- |
| Problem | How do we measure whether synthetic data is useful for downstream tasks? |
| The itch | Teams report distribution similarity, but users care whether the synthetic data supports specific analysis, testing, or model training. |
| Why it matters | Low-utility synthetic data wastes time and can mislead product, policy, or science decisions. |
| Current workaround | Compare summary statistics or train one model on synthetic data. |
| Why the workaround is insufficient | It misses task-specific utility, rare groups, causal structure, and failure under shift. |
| What good progress would look like | Utility evaluations tied to intended use, with explicit tasks, unacceptable failures, and subgroup reporting. |
| Difficulty | Good first research problem |
| Good for | ML researcher, benchmark maintainer, domain expert |
| Related PETs | Synthetic data, DP synthetic data |
| Possible first contribution | Build a task card for one synthetic dataset release that defines allowed uses and three utility tests. |

## Residual Privacy Risk Communication

| Field | Card |
| --- | --- |
| Problem | How do we communicate residual privacy risk to non-experts? |
| The itch | "Synthetic" sounds safe, while "DP synthetic" sounds formally safe even when utility and parameters matter. |
| Why it matters | Data users, legal teams, and executives may overtrust releases. |
| Current workaround | Add generic caveats in documentation. |
| Why the workaround is insufficient | It does not say what attacks were tested, what failed, or what users must not do. |
| What good progress would look like | A synthetic-data release card that states privacy method, tests, residual risks, intended uses, and prohibited uses. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, policy researcher, technical writer |
| Related PETs | Synthetic data, DP |
| Possible first contribution | Rewrite an example synthetic-data release note with explicit privacy tests, utility limits, and misuse warnings. |

## DP Synthetic Data Under Utility Pressure

| Field | Card |
| --- | --- |
| Problem | How can teams avoid weakening DP synthetic data claims when utility is poor? |
| The itch | When DP noise hurts utility, teams may tune, rerun, or release supplemental information until the privacy story becomes unclear. |
| Why it matters | Composition and selection effects can quietly invalidate the intended guarantee. |
| Current workaround | Choose a more permissive budget or release non-DP helper artifacts. |
| Why the workaround is insufficient | It hides the privacy cost of iteration and auxiliary releases. |
| What good progress would look like | A release workflow that tracks privacy budget, tuning decisions, auxiliary outputs, and final utility. |
| Difficulty | Medium |
| Good for | Privacy engineer, ML researcher |
| Related PETs | DP, synthetic data |
| Possible first contribution | Document a DP synthetic-data tuning loop and account for every release decision, including failed candidates. |
