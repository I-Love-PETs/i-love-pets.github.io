# Decision Tree

This page gives a first candidate, not a final architecture. It is intentionally text-first so the decision path remains readable on phones, laptops, and printed reviews.

## Start With The Allowed Output

Most privacy failures happen after a PET successfully protects inputs. Begin with the output you are allowed to reveal.

| Allowed output | Start with | Add when needed | Watch for |
| --- | --- | --- | --- |
| A trained model | Federated learning if raw training data cannot centralize | Secure aggregation, DP, robust aggregation | Update leakage, poisoning, non-IID data, model memorization |
| Aggregate metrics | Federated analytics, MPC, or a clean room | DP, thresholds, output review | Small-cell leakage, repeated queries, inconsistent metric definitions |
| A match set | Private set intersection | DP counts, clean-room controls, audit logs | The intersection itself may be sensitive |
| An inference result | TEE confidential inference or HE | Attestation, model compression, output controls | Latency, unsupported operators, side channels, prediction leakage |
| A data-like release | DP synthetic data when a formal release claim is needed | Memorization tests, utility benchmarks | Synthetic data copying real records or losing useful signal |

## Decision Ladders

### If the output is a model

| Question | If yes | If no |
| --- | --- | --- |
| Can raw training data centralize safely? | Centralized training with minimization, access control, and release review | Cross-silo federated learning |
| Should the coordinator see individual updates? | Treat updates as sensitive and audit access | Add secure aggregation |
| Is formal record-level privacy required? | Add differential privacy and budget accounting | Still test memorization and inference risk |
| Can participants run local training reliably? | Continue to FL architecture review | Consider governed centralization, a clean room, or a narrower analytics task |

Primary recommendation: **FL + secure aggregation + optional DP** when data cannot centralize and the output is a model.

### If the output is an aggregate metric

| Question | If yes | If no |
| --- | --- | --- |
| Can one operator be trusted to run the computation? | Clean room or governed analytics | MPC or federated analytics |
| Could small cells reveal people, sites, or businesses? | Add DP, thresholds, grouping, and output review | Still track repeated queries |
| Do parties define the metric the same way? | Continue | Fix schema and semantics before choosing a PET |

Primary recommendation: **federated analytics** for simple distributed metrics; **MPC** when no single operator should see intermediate values.

### If the output is a match set

| Question | If yes | If no |
| --- | --- | --- |
| Is revealing the intersection allowed? | Private set intersection | Do not release the match set |
| Is only the count needed? | PSI with count-only output or MPC | Restrict match use and audit downstream actions |
| Can parties repeat queries freely? | Add query limits and review | Continue |

Primary recommendation: **PSI** when parties may learn the agreed overlap. If the overlap is sensitive, use a stricter output policy or a different computation.

### If the output is an inference result

| Question | If yes | If no |
| --- | --- | --- |
| Is hardware trust acceptable? | TEE confidential inference | Homomorphic encryption or local inference |
| Does the model fit HE constraints? | Benchmark HE end to end | Redesign the model, use a TEE, or run locally |
| Can the output reveal sensitive facts? | Add output controls, rate limits, and review | Continue |
| Can clients verify attestation? | Continue with TEE design | Do not rely on confidential inference claims |

Primary recommendation: **TEE first for broad model support** when hardware trust is acceptable; **HE only after model-fit and latency benchmarking**.

### If the output is a data-like artifact

| Question | If yes | If no |
| --- | --- | --- |
| Is a formal release claim required? | DP synthetic data | Synthetic data with explicit residual-risk labeling |
| Is downstream utility measurable? | Benchmark the intended tasks | Do not release as a useful substitute |
| Does the generator memorize rare records? | Stop, tune, or use a stricter release path | Continue with release review |

Primary recommendation: **DP synthetic data** for broad release claims. Non-DP synthetic data may still be useful, but it should not be described as anonymous.

## When The Recommendation Changes

| First answer | Change recommendation when... | Consider instead |
| --- | --- | --- |
| Federated learning | Participants cannot run local training or the task is only aggregate measurement | Federated analytics, MPC, clean room |
| Secure aggregation | You need to inspect individual updates for debugging or poisoning defense | Robust aggregation, trusted review, staged rollout |
| Differential privacy | Utility collapses at a defensible budget | Narrower release, larger cohorts, fewer queries, governance controls |
| MPC | Parties cannot maintain protocol operations or collusion assumptions are unrealistic | Clean room, TEE, centralized governed processing |
| HE | Latency, ciphertext size, or unsupported operators break the workload | TEE confidential inference, client-side inference, model redesign |
| TEE | Hardware trust, attestation, or side-channel assumptions are unacceptable | HE, MPC, local execution, governance-only design |
| PSI | Revealing the match set is not allowed | MPC for downstream aggregate, DP counts, no-release workflow |
| Synthetic data | Memorization risk is high or downstream utility is poor | DP query access, restricted release, task-specific benchmark data |

## Worked Example: Hospitals Training A Model

Path through the ladders:

1. Output is a model.
2. Raw training data cannot centralize.
3. Start with cross-silo FL.
4. Coordinator should not inspect hospital updates, so add secure aggregation.
5. Patient-level contribution should be bounded, so evaluate DP.

Recommended shortlist: **FL + secure aggregation + optional DP**, with robust aggregation and per-site evaluation.

What can go wrong:

- FL updates leak information if secure aggregation or DP assumptions fail.
- DP utility may be unacceptable for rare conditions.
- Non-IID data can produce a model that works for large hospitals and fails at small ones.
- Poisoned updates are harder to detect when update visibility is reduced.

Measure before launch: per-site performance, subgroup performance, privacy budget, minimum participants per round, dropout behavior, poisoning resilience, and operational cost.

## Worked Example: Private Inference

Path through the ladders:

1. Output is an inference result.
2. The service should not see plaintext inputs.
3. Hardware trust is acceptable only if customers can verify attestation.
4. If the model is large or latency-sensitive, start with TEE confidential inference.
5. If hardware trust is unacceptable and the model is HE-friendly, benchmark HE.

Recommended shortlist: **TEE first for broad model support; HE only after model-fit benchmarking**.

What can go wrong:

- The output reveals the sensitive attribute the input protection was meant to hide.
- Attestation is not integrated into the client workflow.
- HE operator constraints force a model that is not useful.
- Logs capture plaintext prompts or decrypted outputs.

## Follow The Decision

- Differential privacy: [PET taxonomy](../start-here/pet-taxonomy.md#differential-privacy), [DP synthetic data release](../pet-patterns/dp-synthetic-data-release.md), [DP research problems](../fix-my-itch/differential-privacy.md)
- Federated learning: [Cross-silo federated learning](../pet-patterns/cross-silo-federated-learning.md), [FL secure aggregation](../pet-architectures/fl-secure-aggregation.md), [FL research problems](../fix-my-itch/federated-learning.md)
- MPC: [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md), [MPC research problems](../fix-my-itch/mpc.md), [Collusion](../threat-models/collusion.md)
- Homomorphic encryption: [Private inference](../pet-patterns/private-inference.md), [HE private inference API](../pet-architectures/he-private-inference-api.md), [HE research problems](../fix-my-itch/homomorphic-encryption.md)
- TEEs: [Confidential inference](../pet-patterns/confidential-inference.md), [Confidential RAG](../pet-architectures/confidential-rag.md), [Side channels](../threat-models/side-channels.md)
- Synthetic data: [DP synthetic data release](../pet-patterns/dp-synthetic-data-release.md), [Synthetic data release pipeline](../pet-architectures/synthetic-data-release-pipeline.md), [Synthetic data research problems](../fix-my-itch/synthetic-data.md)
