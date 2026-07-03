# By ML Task

ML task matters because PETs constrain different parts of the pipeline: data collection, training, inference, evaluation, logging, and release.

## Task Matrix

| ML task | Primary PET | Supporting PETs | What to measure | Do not claim |
| --- | --- | --- | --- | --- |
| Cross-silo model training | Federated learning | Secure aggregation, DP, robust aggregation | Per-site utility, update leakage, poisoning resilience, round size | Privacy from FL alone |
| Federated analytics | Federated analytics or MPC | DP, thresholds, output review | Small-cell leakage, latency, analyst workflow, cost | That aggregates are automatically safe |
| Private inference | HE or TEE confidential inference | Compression, quantization, attestation, key management | Latency, accuracy, supported operators, output leakage | That input privacy protects prediction privacy |
| Private RAG | Confidential RAG | TEEs, access control, redaction, audit logs | Retrieval authorization, answer leakage, prompt/log retention | That a protected runtime fixes bad permissions |
| Private LLM fine-tuning | DP-SGD, FL, TEEs depending on data location | Secure aggregation, memorization audits, redaction | Utility, privacy budget, memorization, compute cost | That fine-tuning is safe because data stays local |
| Synthetic data generation | DP synthetic data if release is public | Memorization tests, downstream utility tests | Membership inference, nearest-neighbor similarity, task utility | That synthetic means anonymous |
| Privacy-preserving evaluation | Clean room, TEE, MPC, DP metrics | Output review, test-set minimization | Label leakage, benchmark contamination, metric sensitivity | That evaluation outputs cannot leak |

## Cross-Silo Training

Use **federated learning** when several organizations want a shared model and raw data cannot centralize.

Add:

- **secure aggregation** when the coordinator should not inspect individual updates;
- **DP** when the model release must bound individual or record contribution;
- **robust aggregation** when participants may be malicious or compromised;
- **per-site evaluation** because non-IID data can hide failures.

Avoid FL when the real problem is governance, not data movement. A negotiated data-sharing agreement plus centralized training may be simpler, cheaper, and easier to audit.

| Field | Guidance |
| --- | --- |
| Recommended PET | Cross-silo FL + secure aggregation; add DP when record-level contribution bounds are required. |
| Alternative PETs | Governed centralization, clean room training, MPC/federated analytics for non-training tasks. |
| Why | Training data stays local while the collaboration produces a shared model. |
| Tradeoffs | Distributed operations, non-IID evaluation, harder debugging, possible DP utility loss. |
| Failure modes | Update leakage, poisoning, small rounds, memorization, poor utility for smaller sites. |
| Operational considerations | Participant onboarding, local validation, secure aggregation thresholds, per-site metrics, rollback. |

## Federated Analytics

Use **federated analytics** when the output is a metric, report, or aggregate rather than a trained model.

This is often the right starting point for healthcare quality metrics, cross-bank risk statistics, and platform measurement. Add DP or minimum thresholds when outputs could reveal small cohorts.

Avoid it when the computation requires rich joint features across parties. That may push you toward MPC or a controlled clean-room workflow.

| Field | Guidance |
| --- | --- |
| Recommended PET | Federated analytics for simple distributed metrics; MPC when intermediate values must stay hidden. |
| Alternative PETs | Clean room for governed analyst workflows; DP query system for repeated statistical releases. |
| Why | The output is an aggregate, not a model, and raw records do not need to centralize. |
| Tradeoffs | Lower ML complexity, but output policy and metric alignment dominate. |
| Failure modes | Small-cell leakage, repeated-query differencing, inconsistent definitions, collusion. |
| Operational considerations | Schema alignment, minimum thresholds, query review, evidence labels, analyst audit trail. |

## Private Inference

Use **HE** when the model provider must not see client inputs and the workload is narrow enough for encrypted computation.

Use **TEE-based confidential inference** when:

- the model is too complex for practical HE;
- latency matters;
- hardware trust and remote attestation are acceptable;
- plaintext exists only inside the confidential runtime.

Avoid both if the output itself is sensitive and no output policy exists. The prediction can leak attributes even when inputs are protected.

| Field | Guidance |
| --- | --- |
| Recommended PET | HE for narrow no-plaintext-input requirements; TEE confidential inference for complex or latency-sensitive models. |
| Alternative PETs | Client-side inference, standard hosted inference with governance, MPC for multi-party scoring. |
| Why | The sensitive artifact is the inference input, model interaction, or runtime plaintext. |
| Tradeoffs | HE has strong input confidentiality but limited model fit; TEEs are practical but add hardware trust. |
| Failure modes | Unsupported operators, attestation gaps, plaintext logs, prediction leakage, key mishandling. |
| Operational considerations | Key ownership, attestation verification, model update process, p95 latency, output controls. |

## Private RAG

Private RAG is mostly an authorization and leakage-control problem with PET support.

Use confidential RAG when prompts, retrieved snippets, embeddings, or model execution cross trust boundaries. TEEs can reduce runtime exposure, but the design also needs retrieval policy, provenance, log controls, and answer review.

Failure mode: the system faithfully protects the prompt from the cloud operator while retrieving documents the user should never have seen.

| Field | Guidance |
| --- | --- |
| Recommended PET | Confidential RAG with authorization-aware retrieval, log minimization, and output review. |
| Alternative PETs | Ordinary RAG inside a trusted boundary; segmented retrieval; redaction-first workflow. |
| Why | The sensitive artifacts are prompts, retrieved snippets, embeddings, logs, and generated answers. |
| Tradeoffs | Runtime protection helps, but permissions and answer behavior carry much of the risk. |
| Failure modes | Overbroad retrieval, answer quotation of restricted content, sensitive logs, unverifiable attestation. |
| Operational considerations | Access-control tests, provenance, retention, support access, incident response, evaluation prompts. |

## Private LLM Fine-Tuning

Choose based on where training data can live:

| Data constraint | PET direction | Caveat |
| --- | --- | --- |
| Data stays inside organizations | FL | Updates can leak; local training must be reliable |
| Formal privacy for records is required | DP-SGD or DP adapters | Utility and compute may be painful |
| Training can run in a confidential environment | TEEs | Requires attestation and side-channel assumptions |
| Only redacted examples can be used | Redaction plus evaluation | Redaction is not a formal privacy guarantee |

Measure memorization directly. A private fine-tuning story is weak if nobody tests whether prompts can extract training examples.

| Field | Guidance |
| --- | --- |
| Recommended PET | DP-SGD/DP adapters, FL, or TEEs depending on where training data may live. |
| Alternative PETs | Retrieval-only design, redaction plus evaluation, smaller task-specific model, no fine-tuning. |
| Why | Training can memorize examples, and the privacy goal may involve records, organizations, or prompts. |
| Tradeoffs | DP can reduce quality; FL adds operations; TEEs add trust assumptions; redaction is not formal privacy. |
| Failure modes | Training-example extraction, weak budget accounting, local data leakage, model overfitting. |
| Operational considerations | Memorization audit, privacy budget, data retention, model release policy, rollback criteria. |

## Synthetic Data For ML

Use synthetic data for prototyping, QA, education, and some downstream modeling when raw data release is too risky.

Use **DP synthetic data** for public or broad releases that need a formal privacy claim. Non-DP synthetic data may still be useful, but it should be labeled as risk-reduced data, not anonymous data.

Measure:

- downstream task performance;
- rare subgroup utility;
- nearest-neighbor similarity to training records;
- membership inference risk;
- privacy budget if DP is used.

| Field | Guidance |
| --- | --- |
| Recommended PET | DP synthetic data for public release; non-DP synthetic data only for clearly scoped internal use. |
| Alternative PETs | DP query access, restricted enclave, benchmark-specific generated data. |
| Why | Users need a data-like artifact, but the release itself can be attacked. |
| Tradeoffs | Public release flexibility versus rare-case utility and privacy-budget cost. |
| Failure modes | Memorization, misleading correlations, poor downstream utility, overbroad reuse. |
| Operational considerations | Release review, data cards, nearest-neighbor tests, downstream benchmarks, usage limits. |

## Worked Example: Model Provider Private Inference

A model provider wants to sell risk scoring without seeing customer inputs.

First shortlist:

- HE if the model can be simplified to supported operations and latency remains acceptable.
- TEE confidential inference if the model is complex or low latency is required.
- Client-side inference if the model is small enough and IP exposure is acceptable.

Recommendation changes when:

- the customer also needs the provider not to learn outputs;
- the model architecture cannot be made HE-friendly;
- attestation cannot be integrated into the customer's workflow;
- the input sensitivity is low enough that standard hosted inference plus contractual controls is sufficient.

## Checklist

- Which pipeline stage contains the sensitive data?
- Does the PET protect training data, inference inputs, retrieved context, evaluation labels, logs, or outputs?
- Is the model architecture compatible with the PET?
- What utility loss is acceptable?
- What attack will be tested before launch?
- What operational metric would cause rollback?
