# Choose a PET

!!! info "Review status"
    Last reviewed: 2026-06-10
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

*(Evidence: Expert judgment, 2026-06-10 — scores are editorial estimates across representative workloads; no single benchmark covers all PETs on a common task. Treat as a starting shortlist, not a precise ranking.)*

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
| Recommended PET | Cross-silo federated learning with secure aggregation. |
| Alternative PETs | Governed centralization if sharing is permitted; MPC or federated analytics if the task is a statistic rather than a model; TEEs if training can run inside an accepted confidential boundary. |
| Why | Hospitals can keep raw records local while contributing to a shared model, and secure aggregation reduces coordinator visibility into site updates. |
| Tradeoffs | FL adds local operations, non-IID evaluation, round orchestration, and harder debugging. DP may be needed for patient-level contribution bounds, but it can reduce utility for rare conditions. |
| Failure modes | FL updates can leak information; small rounds can expose a site; poisoned updates can degrade the model; heterogeneous data can make the global model worse for smaller hospitals. |
| Operational considerations | Define minimum participants per round, participant authentication, local training versioning, secure-aggregation recovery, per-site metrics, audit logs, and rollback criteria. |
| What to measure | Per-site utility, subgroup performance, round size, dropout rate, update leakage risk, privacy budget if DP is used, poisoning resilience, cost of local operations. |

*(Evidence: Literature-backed, 2026-06-10 — gradient leakage from FL updates is well-documented; see Zhu et al., "Deep Leakage from Gradients", NeurIPS 2019 (https://papers.nips.cc/paper/2019/hash/60a6c4002cc7b29142def8871531281a-Abstract.html) and Geiping et al., "Inverting Gradients", NeurIPS 2020. The claim that "data stays local" is accurate for raw data but not for derived information; the "What can go wrong" row above captures the residual risk.)*

### Banks want to detect fraud across institutions

| Recommendation | Guidance |
| --- | --- |
| Recommended PET | PSI for permitted overlap, MPC for richer joint features, or federated analytics for simple distributed metrics. |
| Alternative PETs | Cross-silo FL if the durable output is a shared fraud model; clean room if governance, auditability, and analyst workflow are the main blockers. |
| Why | Fraud signals often require cross-institution evidence, but raw transaction data, watchlists, and customer identifiers are highly sensitive. |
| Tradeoffs | PSI is narrow but practical; MPC supports richer computation at higher coordination cost; FL optimizes a model but may not answer the immediate investigation question. |
| Failure modes | The overlap set may reveal investigations; collusion assumptions may be unrealistic; thresholds can be too low; latency may miss operational fraud windows; entity resolution can create false matches. |
| Operational considerations | Agree on identifier hygiene, allowed uses of matches, minimum cohorts, query repetition limits, analyst access, evidence retention, and dispute handling. |
| What to measure | Detection lift, false positives, time-to-decision, smallest released cohort, collusion assumptions, analyst workflow fit, fairness impact. |

### An enterprise wants private RAG over sensitive documents

| Recommendation | Guidance |
| --- | --- |
| Recommended PET | Confidential RAG with authorization-aware retrieval and strong access control. |
| Alternative PETs | Ordinary RAG with governance if all components are inside one trusted boundary; segmented search or redaction workflow if the problem is document permissions; HE only for narrow inference steps, not full RAG. |
| Why | The main exposure is not only model inference; it is retrieval context, prompts, embeddings, logs, generated answers, and overbroad authorization. |
| Tradeoffs | TEEs can reduce runtime exposure but add attestation, hardware trust, deployment complexity, and side-channel assumptions. Retrieval policy still carries most of the privacy load. |
| Failure modes | The system retrieves documents the user should not see, logs sensitive prompts, quotes restricted content in answers, or relies on attestation nobody verifies. |
| Operational considerations | Test per-document authorization, provenance, prompt/log retention, enclave image updates, attestation verification, support access, and incident response. |
| What to measure | Retrieval precision, authorization failures, prompt/log retention, answer leakage rate, attestation coverage, incident response path. |

*(Evidence: Needs evidence, 2026-06-10 — no public benchmark covers the full leakage surface of private RAG (retrieval, prompt, log, output). The "What can go wrong" guidance is expert judgment based on known attack surfaces; a measured evaluation for each channel is an open backlog item.)*

### A company wants to release a synthetic dataset

| Recommendation | Guidance |
| --- | --- |
| Recommended PET | DP synthetic data when the release needs a formal privacy claim. |
| Alternative PETs | DP query access if users only need statistics; restricted sharing if high-fidelity individual-level data is required; non-DP synthetic data for internal QA with explicit residual-risk labeling. |
| Why | Synthetic data can still memorize rare records or leak sensitive correlations; DP is the main route to a formal individual privacy statement. |
| Tradeoffs | Stronger privacy budgets often reduce rare-pattern fidelity; high-utility synthetic data may preserve too much; broad releases require documentation users can understand. |
| Failure modes | Utility evaporates under DP; non-DP generators copy training examples; users overtrust the release; documentation hides residual risk. |
| Operational considerations | Define privacy unit, budget owner, release review, memorization tests, utility benchmarks, versioning, and downstream-use warnings. |
| What to measure | Downstream task utility, nearest-neighbor similarity, membership inference risk, privacy budget, rare subgroup behavior. |

*(Evidence: Literature-backed, 2026-06-10 — membership inference risk from synthetic generators is documented; see Jordon et al., "Synthetic Data — what, why and how?", Royal Statistical Society 2022 (https://doi.org/10.48550/arXiv.2205.03257) and Carlini et al., "Extracting Training Data from Large Language Models", USENIX Security 2021. The claim that non-DP generators can copy training examples is Needs evidence for any specific generator; test before releasing.)*

### Two organizations want to find overlapping users

| Recommendation | Guidance |
| --- | --- |
| Recommended PET | Private set intersection. |
| Alternative PETs | MPC if overlap is only one input to a richer joint computation; clean room if governance and workflow controls matter more than cryptographic nonmatch privacy. |
| Why | PSI can hide nonmatching records while revealing an agreed match set or count. |
| Tradeoffs | PSI is targeted and efficient, but it does not decide whether revealing the intersection is acceptable. Count-only outputs are safer but less useful. |
| Failure modes | The match itself may be sensitive; one party can use repeated queries to learn more; weak identifiers create false matches; downstream use can violate expectations. |
| Operational considerations | Define output type, repeated-query controls, match-use policy, identifier normalization, minimum cohorts, and audit logs. |
| What to measure | Match precision, match recall, allowed output, repeated-query controls, minimum cohort size, identifier hygiene. |

### A model provider wants private inference

| Recommendation | Guidance |
| --- | --- |
| Recommended PET | HE for narrow models and strict no-plaintext-input requirements; TEEs when model complexity and latency matter more. |
| Alternative PETs | Client-side inference if the model can run locally; standard hosted inference with contractual and security controls if the input sensitivity does not justify PET overhead. |
| Why | HE keeps inputs encrypted during computation, while TEEs can support broader workloads under hardware trust assumptions. |
| Tradeoffs | HE has operator, model-design, ciphertext-size, and latency constraints. TEEs are faster and broader but require hardware trust, attestation, and side-channel review. |
| Failure modes | HE latency is unacceptable; model layers are unsupported; TEE attestation is not checked; outputs leak sensitive attributes; keys are mishandled; logs capture plaintext. |
| Operational considerations | Own key lifecycle, attestation verification, model update workflow, p95 latency benchmark, output policy, and support/debugging boundaries. |
| What to measure | End-to-end latency, ciphertext size, accuracy loss, supported operators, attestation verification, output leakage. |

*(Evidence: Expert judgment, 2026-06-10 — the latency and operator-support constraints on HE are widely noted in literature (e.g., Boura et al., "TFHE: Fast Fully Homomorphic Encryption Over the Torus", JoC 2020) but no single cross-workload benchmark for HE vs. TEE vs. client-side inference is publicly available. Needs evidence for specific model families.)*

## Anti-Patterns

- Choosing FL because data cannot move, when the real blocker is governance, liability, or incentives.
- Adding DP after launch without defining the privacy unit, budget owner, and accounting process.
- Using HE as a default for modern ML without checking model architecture, operator support, batching, and latency. *(Evidence: Expert judgment, 2026-06-10 — HE operator support for transformer-style layers remains limited; treat as Needs evidence for any specific architecture until benchmarked.)*
- Treating a TEE as a magic secure box while ignoring attestation, supply chain, logs, side channels, and output leakage. *(Evidence: Literature-backed, 2026-06-10 — TEE side-channel attacks are well-documented; see Van Bulck et al., "Foreshadow", USENIX Security 2018 (https://foreshadowattack.eu/) and Intel Product Security Advisory INTEL-SA-00161.)*
- Releasing synthetic data without a privacy evaluation and a clear statement of residual risk.
- Publishing aggregate outputs without minimum thresholds or review for small-group leakage.

## Evidence Needed Before Committing

- A written threat model naming the adversary, protected asset, collusion assumptions, and allowed output.
- A workload benchmark for privacy, utility, latency, cost, and operational effort.
- A failure-mode review: poisoning, inference attacks, side channels, logging, keys, and output leakage.
- A reversal condition: the metric or risk that would make you choose another PET.
