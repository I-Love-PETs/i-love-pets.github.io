# Benchmark Scorecards

These scorecards are starting templates. A good benchmark should make a team more willing to reject the wrong PET, not only more confident in the chosen one.

## Private RAG Scorecard

| Category | What to measure | Good evidence looks like |
| --- | --- | --- |
| Privacy claim | Prompts, retrieved snippets, embeddings, logs, citations, and answers | Tests for unauthorized retrieval, prompt logging, answer leakage, and citation leakage |
| Utility | Answer quality under access constraints | Accuracy and citation quality by role, with denied-access cases |
| Cost | Retrieval latency, confidential runtime overhead, review time | p50/p95/p99 latency, cloud cost, log-review burden |
| Robustness | Prompt injection, stale permissions, deleted documents | Attack fixtures and regression tests |
| Operations | Policy debugging, provenance, incident response | Traceable policy decisions and reproducible unsafe-answer reports |

### Minimum Test Set

- User asks for a document they are not authorized to see.
- Retrieved context includes a restricted document with a tempting answer.
- Prompt injection appears inside an otherwise authorized document.
- Logs are inspected for prompts, snippets, and generated answers.
- Citation policy is tested when the document existence is itself sensitive.

## Private Inference Scorecard

| Category | What to measure | Good evidence looks like |
| --- | --- | --- |
| Privacy claim | Client input exposure to model provider and platform operator | HE parameter review or TEE attestation verification |
| Utility | Accuracy after quantization, approximation, or model redesign | Comparison with plaintext baseline |
| Cost | End-to-end latency, ciphertext size, throughput, cloud cost | p50/p95/p99 including encryption, transfer, and decryption |
| Robustness | Repeated-query leakage, model extraction, key mishandling | Abuse tests and key-management review |
| Operations | Client SDK integration and failure behavior | Clear behavior when attestation, keys, or decryption fail |

### Decision Rule

Use **HE** only when the model fits supported operators and latency is acceptable. Use **TEE confidential inference** when model flexibility matters and hardware trust is acceptable.

## Cross-Silo FL Scorecard

| Category | What to measure | Good evidence looks like |
| --- | --- | --- |
| Privacy claim | Update leakage, model memorization, participant privacy | Gradient leakage tests, membership inference, DP accounting if used |
| Utility | Global, per-site, and subgroup performance | Site-level metrics and confidence intervals |
| Cost | Rounds, communication, local compute, participant support | Round time, bandwidth, dropout recovery, operator effort |
| Robustness | Non-IID data, poisoned updates, site dropouts | Stress tests with skewed silos and malicious updates |
| Operations | Local setup, versioning, monitoring, rollback | Participant onboarding diary and training-code provenance |

### Minimum Test Set

- One large site and several small sites.
- Label skew and missing-feature skew.
- Participant dropout mid-round.
- Poisoned or low-quality update.
- Final-model memorization probe.

## Synthetic Data Release Scorecard

| Category | What to measure | Good evidence looks like |
| --- | --- | --- |
| Privacy claim | Memorization, membership inference, rare-record leakage | Nearest-neighbor tests, attack baselines, DP accounting if used |
| Utility | Intended downstream tasks | Task-level utility, rare subgroup utility, known failure cases |
| Cost | Generation, tuning, privacy review, documentation | Compute plus reviewer time and release iterations |
| Robustness | Overfitting, distribution shift, misuse outside intended task | Stress tests and prohibited-use documentation |
| Operations | Release governance and residual-risk communication | Release card with intended uses, limits, and privacy tests |

### Release Gate

Do not release synthetic data broadly unless the page states whether it is DP, what memorization tests were run, what utility was measured, and what residual risk remains.

## Federated Analytics / MPC Analytics Scorecard

| Category | What to measure | Good evidence looks like |
| --- | --- | --- |
| Privacy claim | Input hiding, participant contribution hiding, output leakage | Collusion assumptions, small-cell tests, repeated-query review |
| Utility | Metric accuracy and decision impact | Comparison with trusted baseline or known aggregate |
| Cost | Parties, rounds, bandwidth, query approval, review time | End-to-end query time and operational effort |
| Robustness | Missing parties, malformed inputs, schema mismatch | Failure drills and validation checks |
| Operations | Query governance, auditability, policy enforcement | Query logs, allowed-output schemas, incident path |

### Minimum Test Set

- Tiny cohort query.
- Repeated differencing query.
- One participant unavailable.
- Malformed or stale participant data.
- Output that is technically aggregate but commercially or personally sensitive.

## Shared Reporting Template

| Field | Fill this in |
| --- | --- |
| Workload | What decision or workflow is being benchmarked? |
| Protected asset | Inputs, updates, prompts, embeddings, outputs, logs, model weights, or another artifact |
| Adversary | Curious coordinator, malicious participant, platform operator, inference attacker, external attacker |
| Allowed output | What the system is allowed to reveal |
| PET stack | PETs, supporting controls, and parameters |
| Baselines | Plaintext, centralized, governance-only, or alternative PET designs |
| Results | Privacy, utility, latency, throughput, cost, robustness, operations |
| Evidence and source quality | Measured / deployment-backed / literature-backed / expert judgment / needs evidence, plus source-quality label |
| Failure cases | What broke or became unacceptable |
| Reversal condition | What result would make you choose another PET |
