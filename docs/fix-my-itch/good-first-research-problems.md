# Good First Research Problems

Good first PET research problems should produce a reusable artifact: a checklist, benchmark, reproduction, small tool, failure-case catalog, or measurement report.

## Rewrite PET Claims With Threat Models

| Field | Card |
| --- | --- |
| Problem | Can common PET marketing claims be rewritten as precise threat-model statements? |
| The itch | Readers see phrases like "privacy-preserving AI" without knowing what is protected or from whom. |
| Why it matters | Bad claims lead to bad procurement, weak reviews, and overtrust. |
| Current workaround | Experts mentally translate claims during review. |
| Why the workaround is insufficient | The translation is not reusable and non-experts do not see it. |
| What good progress would look like | A public set of before/after claim rewrites with protected assets, adversaries, assumptions, and residual risks. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, policy researcher, technical writer |
| Related PETs | All PETs |
| Possible first contribution | Rewrite ten PET claims from public materials and publish a scoring rubric. |

## Small-Cohort Aggregate Leakage Catalog

| Field | Card |
| --- | --- |
| Problem | What aggregate outputs leak sensitive facts when cohorts are small? |
| The itch | Teams often assume aggregates are safe until a rare group, hospital, advertiser, or region is isolated. |
| Why it matters | Small-cohort leakage affects healthcare, public statistics, advertising, and fraud analysis. |
| Current workaround | Use rough minimum thresholds. |
| Why the workaround is insufficient | Thresholds are often arbitrary and do not explain residual leakage. |
| What good progress would look like | A catalog of small-cohort leakage examples with mitigations such as grouping, suppression, DP, and output review. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, benchmark maintainer, policy researcher |
| Related PETs | DP, federated analytics, clean rooms, MPC |
| Possible first contribution | Build five synthetic examples where aggregates reveal an individual or organization and test common thresholds. |

## PET Setup Friction Diary

| Field | Card |
| --- | --- |
| Problem | Where do developers get stuck when trying PET tools for the first time? |
| The itch | Tooling pain is often discussed anecdotally rather than measured. |
| Why it matters | Adoption fails when setup, docs, and examples are too hard for the target user. |
| Current workaround | Maintainers wait for bug reports or support tickets. |
| Why the workaround is insufficient | It captures only users who persist long enough to complain. |
| What good progress would look like | A reproducible setup diary that records time, errors, missing docs, security assumptions, and first successful run. |
| Difficulty | Good first research problem |
| Good for | Systems builder, benchmark maintainer, technical writer |
| Related PETs | MPC, HE, FL, TEEs |
| Possible first contribution | Try one PET tool from a clean environment and publish a timed friction report with suggested fixes. |

## Privacy Test For A Toy RAG System

| Field | Card |
| --- | --- |
| Problem | What simple tests catch privacy leaks in a toy RAG system? |
| The itch | RAG demos often check answer quality but not unauthorized retrieval, prompt logging, or answer leakage. |
| Why it matters | Private RAG is a common enterprise pitch and an easy place to leak sensitive documents. |
| Current workaround | Manual review of prompts and outputs. |
| Why the workaround is insufficient | It is not repeatable and misses regressions. |
| What good progress would look like | A small test harness with role-based documents, adversarial prompts, expected-deny cases, and log checks. |
| Difficulty | Good first research problem |
| Good for | Systems builder, privacy engineer, benchmark maintainer |
| Related PETs | TEEs, confidential RAG, access control |
| Possible first contribution | Create a 20-document RAG fixture with three roles and tests for unauthorized snippet exposure. |
