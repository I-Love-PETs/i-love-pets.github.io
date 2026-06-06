# Use Cases

Use cases translate PET choices into domain constraints. The same PET can be wise in one domain and irresponsible in another.

Use these pages when you know the domain problem but do not yet know which PET stack is defensible.

## Playbook Map

| Domain | Common decision | Strong starting point | Watch first |
| --- | --- | --- | --- |
| [Healthcare](healthcare.md) | Multi-site research, quality metrics, cohort matching | FL, federated analytics, PSI, DP synthetic data | Rare cohorts, clinical utility, local validation |
| [Finance](finance.md) | Fraud, AML, risk, and compliance collaboration | PSI, MPC, federated analytics, FL | Adversarial participants, entity resolution, output misuse |
| [Advertising](advertising.md) | Measurement, attribution, audience overlap | Clean rooms, PSI, DP, attribution APIs | Small segments, repeated queries, platform incentives |
| [Public Sector](public-sector.md) | Official statistics, cross-agency analytics, public-interest releases | DP, MPC, clean rooms, synthetic data | Legitimacy, accessibility, utility disputes |
| [AI](ai.md) | Private RAG, inference, fine-tuning, evaluation | TEEs, HE, DP, FL, access controls | Memorization, prompt/log leakage, output leakage |

## How To Use A Playbook

1. Pick the scenario closest to your real decision.
2. Check the recommended PET stack and the "when not to use it" section.
3. Write down what the output is allowed to reveal.
4. Measure the listed privacy, utility, cost, and operational metrics.
5. Move to [PET Compass](../pet-compass/index.md) or [PET Patterns](../pet-patterns/index.md) for deeper design guidance.

## Cross-Domain Warning Signs

- The PET protects inputs but the output reveals the sensitive fact.
- The domain problem is governance, incentives, or legal authority rather than computation.
- The benchmark uses clean data but the deployment has missingness, drift, or inconsistent definitions.
- The privacy claim ignores logs, prompts, model weights, embeddings, or repeated queries.
- The proposal says "privacy-preserving" without naming an adversary.
