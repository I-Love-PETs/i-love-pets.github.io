# Choose a PET

!!! info "Review status"
    Last reviewed: 2026-06-03
    Evidence level: Expert judgment
    Snapshot scope: Practical shortlisting guidance. Validate cost, maturity, and utility against the target workload before production decisions.

The right PET is usually the one that matches the **output you are allowed to reveal**, not the one with the strongest-sounding privacy claim.

Use this page to create a shortlist. Then write the threat model, benchmark the workload, and decide what evidence would change your mind.

## Fast Shortlist

| Situation | Primary PET | Supporting PETs | Avoid this trap |
| --- | --- | --- | --- |
| Several organizations need a shared model and data cannot centralize | Federated learning | Secure aggregation, DP, robust aggregation, TEEs for orchestration | Claiming privacy from FL alone |
| Several organizations need an aggregate metric | Federated analytics or MPC | DP, thresholding, clean-room governance | Publishing small-cell outputs that reveal people or businesses |
| Parties need to find overlap without revealing nonmatches | PSI | DP on downstream counts, clean-room logging, legal controls | Treating the intersection itself as nonsensitive |
| A service must run inference without seeing client inputs | HE or TEE confidential inference | Model compression, attestation, output controls | Choosing HE before checking operator support and latency |
| A team wants to publish data-like artifacts | DP synthetic data when a formal release claim is needed | Memorization tests, utility benchmarks, release review | Calling synthetic data safe because it is synthetic |
| Sensitive documents must support RAG | Confidential RAG with tight access control | TEEs, redaction, audit logs, retrieval policy, output review | Hiding the runtime while leaking through retrieval or answers |

## Tradeoff Scoring

Scores are directional: 1 is weak or expensive, 5 is strong or easy. Change the score when your workload evidence disagrees.

| PET | Input confidentiality | Output privacy | Utility retention | Latency/cost | Operational ease | Best first question |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Federated learning | 3 | 1 | 4 | 3 | 2 | Can every participant run trustworthy local training? |
| Secure aggregation | 4 | 1 | 4 | 3 | 2 | How many participants are needed per round? |
| Differential privacy | 2 | 5 | 2-4 | 4 | 3 | What privacy unit and budget are defensible? |
| MPC | 5 | 2 | 4 | 2 | 1 | Who are the parties and what collusion is allowed? |
| Homomorphic encryption | 5 | 2 | 3 | 1 | 2 | Is the computation narrow enough for HE? |
| TEEs | 4 | 2 | 4 | 4 | 3 | Is hardware trust and attestation acceptable? |
| PSI | 5 for nonmatches | 2 | 5 | 4 | 3 | Is revealing the match set allowed? |
| Synthetic data | 1-4 | 2-5 | 2-4 | 3 | 3 | How will you test memorization and downstream utility? |
| Clean room | 2-4 | 2 | 4 | 3 | 3 | Is the main problem governance rather than cryptography? |

## Scenario Recommendations

### Hospitals want to train a model without sharing data

| Recommendation | Guidance |
| --- | --- |
| Primary PET | Cross-silo federated learning |
| Supporting PETs | Secure aggregation, DP if patient-level participation must be bounded, robust aggregation, audit logging |
| Why | Hospitals can keep raw records local while contributing to a shared model. |
| What can go wrong | FL updates can leak information; small rounds can expose a hospital; poisoned updates can degrade the model; heterogeneous data can make the global model worse for smaller sites. |
| What to measure | Per-site utility, subgroup performance, round size, dropout rate, update leakage risk, privacy budget if DP is used, cost of local operations. |
| When it changes | Use centralized training with governance if data sharing is legally and operationally acceptable. Use MPC or TEEs if the task is analytics rather than training. |

### Banks want to detect fraud across institutions

| Recommendation | Guidance |
| --- | --- |
| Primary PET | Federated analytics or MPC, depending on whether the computation is simple or joint and sensitive |
| Supporting PETs | PSI for entity overlap, DP for published metrics, clean-room workflows for auditability |
| Why | Fraud signals often require cross-institution evidence, but raw transaction data and customer lists are highly sensitive. |
| What can go wrong | The overlap set may reveal investigations; collusion assumptions may be unrealistic; thresholds can be too low; latency may miss operational fraud windows. |
| What to measure | Detection lift, false positives, time-to-decision, smallest released cohort, collusion assumptions, analyst workflow fit. |
| When it changes | Use PSI first if the main task is entity matching. Use FL if the goal is a shared fraud model rather than a specific joint computation. |

### An enterprise wants private RAG over sensitive documents

| Recommendation | Guidance |
| --- | --- |
| Primary PET | Confidential RAG with strong access control |
| Supporting PETs | TEEs, remote attestation, redaction, query minimization, output policy, log controls |
| Why | The main exposure is not only model inference; it is retrieval context, prompts, logs, generated answers, and overbroad authorization. |
| What can go wrong | The system retrieves documents the user should not see, logs sensitive prompts, produces answers that quote restricted content, or relies on attestation nobody verifies. |
| What to measure | Retrieval precision, authorization failures, prompt/log retention, answer leakage rate, attestation coverage, incident response path. |
| When it changes | Use ordinary RAG with governance if all users and systems are in one trusted boundary. Use HE only for narrow inference, not full RAG pipelines. |

### A company wants to release a synthetic dataset

| Recommendation | Guidance |
| --- | --- |
| Primary PET | DP synthetic data when the release needs a formal privacy claim |
| Supporting PETs | Memorization tests, utility benchmarks, record-level risk review, release governance |
| Why | Synthetic data can still memorize rare records or leak sensitive correlations; DP is the main route to a formal individual privacy statement. |
| What can go wrong | Utility evaporates under DP; non-DP generators copy training examples; users overtrust the release; documentation hides residual risk. |
| What to measure | Downstream task utility, nearest-neighbor similarity, membership inference risk, privacy budget, rare subgroup behavior. |
| When it changes | Use query access with DP if users only need statistics. Use restricted sharing if high-fidelity individual-level data is required. |

### Two organizations want to find overlapping users

| Recommendation | Guidance |
| --- | --- |
| Primary PET | Private set intersection |
| Supporting PETs | DP on aggregate counts, contractual controls for use of matches, clean-room audit logs |
| Why | PSI can hide nonmatching records while revealing agreed overlap. |
| What can go wrong | The match itself may be sensitive; one party can use repeated queries to learn more; weak identifiers create false matches; downstream use can violate expectations. |
| What to measure | Match precision, match recall, allowed output, repeated-query controls, minimum cohort size, identifier hygiene. |
| When it changes | Use a clean room if governance and workflow controls matter more than cryptographic nonmatch privacy. Use MPC if the overlap is only one step in a richer joint computation. |

### A model provider wants private inference

| Recommendation | Guidance |
| --- | --- |
| Primary PET | HE for narrow models and strict no-plaintext-input requirements; TEEs when model complexity and latency matter more |
| Supporting PETs | Model compression, quantization, attestation, key management, output review |
| Why | HE keeps inputs encrypted during computation, while TEEs can support broader workloads under hardware trust assumptions. |
| What can go wrong | HE latency is unacceptable; model layers are unsupported; TEE attestation is not checked; outputs leak sensitive attributes; keys are mishandled. |
| What to measure | End-to-end latency, ciphertext size, accuracy loss, supported operators, attestation verification, output leakage. |
| When it changes | Use client-side inference if the model can run locally. Use standard hosted inference if the input is not sensitive enough to justify PET overhead. |

## Anti-Patterns

- Choosing FL because data cannot move, when the real blocker is governance, liability, or incentives.
- Adding DP after launch without defining the privacy unit, budget owner, and accounting process.
- Using HE as a default for modern ML without checking model architecture, operator support, batching, and latency.
- Treating a TEE as a magic secure box while ignoring attestation, supply chain, logs, side channels, and output leakage.
- Releasing synthetic data without a privacy evaluation and a clear statement of residual risk.
- Publishing aggregate outputs without minimum thresholds or review for small-group leakage.

## Evidence Needed Before Committing

- A written threat model naming the adversary, protected asset, collusion assumptions, and allowed output.
- A workload benchmark for privacy, utility, latency, cost, and operational effort.
- A failure-mode review: poisoning, inference attacks, side channels, logging, keys, and output leakage.
- A reversal condition: the metric or risk that would make you choose another PET.
