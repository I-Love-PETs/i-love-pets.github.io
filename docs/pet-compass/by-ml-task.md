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

## Federated Analytics

Use **federated analytics** when the output is a metric, report, or aggregate rather than a trained model.

This is often the right starting point for healthcare quality metrics, cross-bank risk statistics, and platform measurement. Add DP or minimum thresholds when outputs could reveal small cohorts.

Avoid it when the computation requires rich joint features across parties. That may push you toward MPC or a controlled clean-room workflow.

## Private Inference

Use **HE** when the model provider must not see client inputs and the workload is narrow enough for encrypted computation.

Use **TEE-based confidential inference** when:

- the model is too complex for practical HE;
- latency matters;
- hardware trust and remote attestation are acceptable;
- plaintext exists only inside the confidential runtime.

Avoid both if the output itself is sensitive and no output policy exists. The prediction can leak attributes even when inputs are protected.

## Private RAG

Private RAG is mostly an authorization and leakage-control problem with PET support.

Use confidential RAG when prompts, retrieved snippets, embeddings, or model execution cross trust boundaries. TEEs can reduce runtime exposure, but the design also needs retrieval policy, provenance, log controls, and answer review.

Failure mode: the system faithfully protects the prompt from the cloud operator while retrieving documents the user should never have seen.

## Private LLM Fine-Tuning

Choose based on where training data can live:

| Data constraint | PET direction | Caveat |
| --- | --- | --- |
| Data stays inside organizations | FL | Updates can leak; local training must be reliable |
| Formal privacy for records is required | DP-SGD or DP adapters | Utility and compute may be painful |
| Training can run in a confidential environment | TEEs | Requires attestation and side-channel assumptions |
| Only redacted examples can be used | Redaction plus evaluation | Redaction is not a formal privacy guarantee |

Measure memorization directly. A private fine-tuning story is weak if nobody tests whether prompts can extract training examples.

## Synthetic Data For ML

Use synthetic data for prototyping, QA, education, and some downstream modeling when raw data release is too risky.

Use **DP synthetic data** for public or broad releases that need a formal privacy claim. Non-DP synthetic data may still be useful, but it should be labeled as risk-reduced data, not anonymous data.

Measure:

- downstream task performance;
- rare subgroup utility;
- nearest-neighbor similarity to training records;
- membership inference risk;
- privacy budget if DP is used.

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
