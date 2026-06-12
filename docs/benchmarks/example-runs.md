# Example Benchmark Runs

These are worked examples of the [scorecard templates](scorecards.md) applied to concrete workloads.
Each example fills in the shared reporting template from `scorecards.md` and adds illustrative figures, explicit tradeoffs, what to measure, and known failure modes.

!!! warning "Evidence levels"
    Figures marked **Illustrative** are plausible ranges constructed from public literature and expert judgment as of 2026-06-10. They are NOT measured results from a specific deployment. Where a figure is grounded in a specific published study it is marked **Literature-backed**. Nothing on this page should be treated as a measured production benchmark without independent replication.

---

## 1. Private RAG — Confidential / Role-Gated Retrieval-Augmented Generation

### Workload Description

A legal or HR team runs a RAG system over a document corpus that is partitioned by access tier (public, internal, restricted, confidential). Users submit natural-language queries. The retriever must return only documents the user is authorised to see; the LLM must not leak restricted content into its generated answer even when restricted documents appear in the top-k results.

### Scorecard

| Category | What was measured | Evidence level | Illustrative result |
| --- | --- | --- | --- |
| Privacy claim | Prompt logging, retrieved-snippet exposure, citation leakage, answer leakage | Expert judgment | 0 leaked snippets in 200 adversarial probes when hard-filter applied pre-LLM; soft-filter (LLM instruction) leaked in ~4 % of cases (2026-06-10) |
| Utility | Answer quality (RAGAS faithfulness + answer relevance) by access tier | Expert judgment | Authorised-tier: faithfulness 0.82, relevance 0.79; no degradation vs. unfiltered baseline for same-tier queries (2026-06-10) |
| Cost | p50 / p95 / p99 end-to-end latency; cloud cost per 1 000 queries | Expert judgment | Hard-filter adds ~40 ms p50 overhead vs. unfiltered; TEE-based confidential retrieval adds ~200–400 ms p50 (2026-06-10) |
| Robustness | Prompt injection inside authorised documents; stale-permission cache; deleted-document residual | Expert judgment | Injection success rate drops from ~30 % (no defence) to < 2 % with structured output parsing + input sanitisation (2026-06-10) |
| Operations | Policy debugging trace; incident-response drill (answer sourced from restricted doc) | Expert judgment | Teams without traceable policy decisions took 3–5× longer to reproduce an unsafe-answer incident (2026-06-10) |

### Tradeoffs

| Axis | Hard permission filter (pre-LLM) | Soft filter (LLM instruction) |
| --- | --- | --- |
| Privacy | Strong — restricted docs never enter context | Weak — restricted docs may appear in context |
| Utility | May reduce recall for legitimate queries near tier boundaries | Higher recall, risk of leakage |
| Latency | +30–50 ms for ACL lookup | Negligible |
| Complexity | Requires ACL service integration | Simpler to implement, harder to audit |

### What to Measure

- Leakage rate: fraction of adversarial probes where restricted content appears verbatim or paraphrastically in the answer.
- Citation policy: confirm the system does not cite documents whose *existence* is sensitive.
- Authorised-recall degradation: RAGAS or similar on authorised-only test set.
- Latency breakdown: ACL lookup, retrieval, LLM inference, total p50/p95/p99.
- Log review burden: time for a human reviewer to reconstruct a suspicious answer.

### Failure Modes

- **Soft-filter bypass**: An LLM told "do not reveal restricted content" will comply in most cases but fails on adversarially crafted authorised documents that contain injection payloads.
- **Stale ACL cache**: Permissions revoked in the source system are still honoured by a cached retriever, allowing access to documents the user should no longer see.
- **Citation side-channel**: Even when answer text is clean, a citation list can reveal that a restricted document exists and is relevant.
- **Embedding leakage**: In shared-index architectures, an attacker with repeated query access can reconstruct approximate document embeddings and infer content.

---

## 2. HE vs TEE Private Inference — Side-by-Side on a Tabular Classification Task

### Workload Description

A bank scores loan applications using a gradient-boosted tree model. The applicant's financial features are sensitive. The model is proprietary. Neither party should see the other's input or model weights. Both Homomorphic Encryption (HE) and a Trusted Execution Environment (TEE) are evaluated on the same task.

### Scorecard

| Category | HE approach | TEE approach | Evidence level |
| --- | --- | --- | --- |
| Privacy claim — client inputs | Client inputs are encrypted under client key; server never sees plaintext | Client inputs are plaintext inside TEE; platform operator cannot observe if attestation holds | Expert judgment |
| Privacy claim — model weights | Model weights evaluated in HE ciphertext domain; client cannot extract them | Weights loaded inside TEE; no hardware-level extraction (assuming no microarchitectural side channel) | Expert judgment |
| Utility — accuracy vs. plaintext | GBDT accuracy drops ~0 % if model is adapted to HE-friendly operators; severe degradation if not (2026-06-10, Expert judgment) | Accuracy identical to plaintext baseline — TEE executes unmodified model (2026-06-10, Expert judgment) |
| Cost — latency (100-feature record) | ~2–30 s per record depending on GBDT depth and HE scheme (CKKS/BFV) (2026-06-10, Expert judgment) | ~5–50 ms per record; TEE overhead ~10–30 % vs. vanilla CPU (2026-06-10, Expert judgment) |
| Cost — throughput | Low; HE is compute-intensive on server | High; TEE supports batch scoring at near-native speed |
| Cost — operational | HE library integration; key management; parameter tuning | TEE platform selection; attestation infrastructure; hardware procurement / cloud availability |
| Robustness — repeated-query leakage | HE is stateless per query; no membership signal from computation itself | Microarchitectural side channels (cache timing) are a known risk on co-hosted TEEs |
| Operations | Complex: HE parameters must match model structure; debugging is opaque | Moderate: standard MLOps pipelines work inside TEE; attestation adds a new failure path |

### Tradeoffs

| | HE | TEE |
| --- | --- | --- |
| Hardware trust required | None | Yes (Intel TDX, AMD SEV, ARM CCA or equivalent) |
| Model compatibility | Must redesign for supported operators | Any model |
| Latency | Seconds to minutes | Milliseconds |
| Cryptographic guarantee | Unconditional under scheme assumptions | Conditional on hardware + microcode integrity |
| Side-channel resistance | Strong (computation on ciphertext) | Needs careful mitigation |

**Decision rule (from [Scorecards](scorecards.md)):** Use HE when the model is shallow and fits HE-supported operators and latency is acceptable. Use TEE when model flexibility matters and hardware trust is acceptable. For this GBDT workload with a latency SLA under 100 ms, TEE is the practical choice as of 2026-06-10.

### What to Measure

- Accuracy delta vs. plaintext baseline on held-out test set.
- p50 / p95 / p99 latency for single-record and batch (100, 1 000, 10 000 records).
- Ciphertext size (HE) or memory footprint inside TEE enclave.
- Attestation verification time (TEE).
- Key management failure scenarios: what does the client see if attestation fails?

### Failure Modes

- **HE parameter mismatch**: choosing CKKS noise budget or polynomial degree incorrectly produces silently wrong scores rather than errors.
- **TEE attestation not verified by client**: clients that skip attestation verification get no confidentiality guarantee despite using a TEE stack.
- **Model extraction via repeated HE queries**: theoretically bounded but practically feasible for simple models if the adversary can submit arbitrary ciphertexts.
- **Enclave memory limits**: large GBDT models may exceed enclave memory, forcing swapping that exposes data to the host OS.

---

## 3. Federated Learning Benchmark — Cross-Silo, Medical Imaging

### Workload Description

Six hospital sites collaboratively train a chest X-ray classification model (binary: abnormality present / absent). Each site holds 500–4 000 labelled images. Data never leaves each hospital. The coordinator is an honest-but-curious cloud service. Differential privacy (DP) with Gaussian noise is applied to model updates.

### Scorecard

| Category | What was measured | Evidence level | Illustrative result |
| --- | --- | --- | --- |
| Privacy claim | Gradient leakage (DLG attack); membership inference on final model; DP accounting | Expert judgment | DLG attack reconstructed no recognisable images after secure aggregation + DP (δ=10⁻⁵, ε tracked per round); membership inference AUC 0.53 (near random) (2026-06-10) |
| Utility — global | AUROC on held-out global test set | Expert judgment | FL + DP: 0.86 AUROC; centralised baseline: 0.89 AUROC; gap narrows with more rounds (2026-06-10) |
| Utility — per-site | AUROC on each site's own test set | Expert judgment | Largest site (4 000 images): 0.88; smallest site (500 images): 0.79; local-only smallest-site: 0.71 (2026-06-10) |
| Utility — subgroup | Demographic subgroup parity gap | Needs evidence | Not measured in this run — flagged as gap |
| Cost | Rounds to convergence; communication per round; local GPU time | Expert judgment | 40 rounds to convergence; ~120 MB per round (FP32 ResNet-50 gradients); ~45 min local training per round per site (2026-06-10) |
| Robustness | Non-IID label skew; one site dropout; one poisoned update (label flip) | Expert judgment | Dropout of one mid-size site: +2 rounds to convergence; Byzantine-robust aggregation (Krum) neutralised single poisoned update (2026-06-10) |
| Operations | Participant onboarding time; monitoring dashboard | Expert judgment | Onboarding a new site required ~8 hours of data-engineering effort; training-code provenance logged per round (2026-06-10) |

### Tradeoffs

| Axis | With DP (ε ≈ 8 per training run) | Without DP |
| --- | --- | --- |
| Privacy formal guarantee | Yes — bounded per-record contribution | No formal bound |
| Utility (AUROC) | ~0.86 | ~0.88 (Expert judgment) |
| Compute overhead | +5–10 % for noise injection | None |
| Auditability | DP budget must be tracked and communicated | No budget to track |

### What to Measure

- DP accounting: per-round ε, total ε, δ, composition method (RDP, zCDP, or other).
- Global and per-site metrics with confidence intervals, not just the mean.
- Membership inference AUC on final model — a near-random AUC is necessary but not sufficient evidence of protection.
- Communication cost: bytes sent and received per site per round.
- Dropout recovery: how many additional rounds when one site is unavailable?
- Subgroup performance across demographic groups represented in the data.

### Failure Modes

- **DP noise destroys small-site utility**: sites with fewer than ~200 records may see catastrophic utility loss at privacy budgets that are acceptable for larger sites.
- **Non-IID drift**: heavy label imbalance across sites causes the global model to underperform every individual site's local model — a signal to reconsider the FL architecture.
- **Round poisoning at scale**: a single Byzantine-robust aggregation method neutralises one poisoned update but may fail against coordinated multi-site attacks.
- **Privacy budget burn-out**: without careful accounting, DP budget is exhausted before the model converges, forcing a choice between continuing without DP or stopping early.
- **Subgroup erasure**: rare demographic subgroups present only at one small site can be effectively erased from the global model without any privacy attack occurring.

---

## 4. Synthetic Data Release Review — DP Synthetic Tabular Data for Research

### Workload Description

A national statistics office releases a DP synthetic version of a household income survey (n = 50 000 records, 22 variables including age, income band, region, employment status). The intended downstream use is economic research: regression analysis and cross-tabulations. The release must pass internal review before public posting.

### Scorecard

| Category | What was measured | Evidence level | Illustrative result |
| --- | --- | --- | --- |
| Privacy claim | Nearest-neighbour distance ratio (NNDR); membership inference; DP accounting | Expert judgment | NNDR median 0.94 (synthetic records not close to real records); membership inference AUC 0.51; DP: ε = 3, δ = 10⁻⁶, Gaussian mechanism, zCDP composition (2026-06-10) |
| Privacy claim — rare records | Rare-region subgroup (n < 50 in real data) memorisation probe | Expert judgment | No rare record reproduced verbatim; two rare combinations appeared in synthetic data but with plausible frequency distortion (2026-06-10) |
| Utility — regression | Coefficients and standard errors for income ~ age + employment + region OLS | Expert judgment | Coefficient estimates within 8 % of real-data estimates; standard errors inflated ~15 % (synthetic variance is higher) (2026-06-10) |
| Utility — cross-tabulations | Chi-squared statistics for key categorical pairs | Expert judgment | 18 / 20 cross-tabulations within acceptable range; 2 involving rare regions showed > 20 % relative error (flagged) (2026-06-10) |
| Utility — rare subgroup | Income distribution for smallest region | Expert judgment | Distribution shape preserved; cell counts distorted by DP noise — not suitable for precise rare-group analysis (2026-06-10) |
| Cost | Generation compute; parameter tuning iterations; privacy review | Expert judgment | ~4 hours training on A100; 6 tuning iterations; ~3 days reviewer time for release card (2026-06-10) |
| Robustness | Distribution shift if real data updated; misuse outside intended tasks | Expert judgment | Longitudinal use (year-over-year comparison) explicitly flagged as out-of-scope in release card (2026-06-10) |
| Operations | Release card completeness; residual-risk statement | Expert judgment | Release card covers: DP parameters, memorisation tests run, utility results, intended uses, prohibited uses, contact for questions (2026-06-10) |

### Release Gate Check

Following the gate from [Scorecards](scorecards.md): this release states whether DP was applied (yes, ε = 3), what memorisation tests were run (NNDR + membership inference), what utility was measured (regression coefficients + cross-tabs), and what residual risk remains (rare-region cells). Gate passed with the two flagged cross-tabulations noted as known limits.

### Tradeoffs

| ε (privacy budget) | Utility (regression R²) | Rare-group fidelity | Evidence level |
| --- | --- | --- | --- |
| ε = 1 | ~0.61 (Expert judgment, 2026-06-10) | Very poor | Expert judgment |
| ε = 3 | ~0.74 (Expert judgment, 2026-06-10) | Poor for cells < 50 | Expert judgment |
| ε = 10 | ~0.81 (Expert judgment, 2026-06-10) | Moderate | Expert judgment |
| No DP (governance only) | ~0.83 | Good | Expert judgment |

### What to Measure

- NNDR and distribution overlap (e.g. Total Variation Distance per marginal).
- Membership inference AUC — report both mean and worst-case across 5 attack seeds.
- Task-level utility for every stated intended use, not just aggregate statistics.
- Rare-subgroup utility separately: a synthetic dataset that is excellent overall can be useless or misleading for minority subgroups.
- DP composition method and budget: report ε, δ, mechanism, and composition theorem used.

### Failure Modes

- **Releasing without a release card**: researchers misuse the synthetic data for tasks it was not designed for (e.g. individual-level inference from a dataset synthesised for aggregate analysis).
- **Overfitting to training data**: generative model memorises rare records, defeating DP if the noise level was insufficient for the tail of the distribution.
- **ε inflation through multiple releases**: releasing updated versions of the same synthetic dataset without tracking cumulative composition.
- **Utility-privacy miscommunication**: a release that is DP-sound but has 30 % error on the key research variable is used uncritically because the DP label signals "private AND useful."

---

## 5. MPC / Federated Analytics — Cross-Org Ad Attribution

### Workload Description

Two ad platforms and a retailer compute a joint conversion-rate metric (ad impressions → purchases) without revealing individual user records or platform-specific impression logs to each other. They use a two-party MPC protocol (secret sharing) with a semi-honest coordinator. The output is an aggregate conversion count, segmented by campaign and week.

### Scorecard

| Category | What was measured | Evidence level | Illustrative result |
| --- | --- | --- | --- |
| Privacy claim — input hiding | No party learns another party's raw impression or purchase records | Expert judgment | Verified by protocol audit; semi-honest threat model with no collusion assumed (2026-06-10) |
| Privacy claim — output leakage | Small-cell suppression for cells with fewer than k records | Expert judgment | k = 50 applied; 3 of 24 campaign-week cells suppressed (2026-06-10) |
| Privacy claim — differencing | Repeated queries with slightly shifted time windows | Expert judgment | No output-differential analysis run — flagged as gap (2026-06-10) |
| Utility — metric accuracy | Conversion count vs. trusted centralised baseline (synthetic validation) | Expert judgment | Within 0.5 % of baseline for unsuppressed cells; suppressed cells represent ~8 % of total conversions (2026-06-10) |
| Utility — decision impact | Campaign budget reallocation decisions made using MPC output vs. centralised | Expert judgment | Decision outcomes identical in 11 / 12 test scenarios; 1 borderline scenario affected by cell suppression (2026-06-10) |
| Cost | End-to-end query time; coordinator effort; schema negotiation | Expert judgment | ~18 min for a weekly batch query over 3 parties; schema negotiation required ~6 hours at setup; ongoing governance ~2 hours per query cycle (2026-06-10) |
| Robustness | One party unavailable; malformed input record; schema drift | Expert judgment | Protocol halts cleanly if a party is unavailable — no partial result leaked; malformed records rejected at ingestion; schema drift requires manual reconciliation (2026-06-10) |
| Operations | Query governance log; allowed-output schema; incident path | Expert judgment | Every query logged with requesting party, timestamp, output schema, suppression count; incident path defined but untested (2026-06-10) |

### Tradeoffs

| Axis | MPC (secret sharing, semi-honest) | Trusted third party | Governance-only data sharing |
| --- | --- | --- | --- |
| Input confidentiality | Cryptographic (semi-honest) | Contractual | Contractual |
| Setup complexity | High — schema alignment, protocol integration | Moderate | Low |
| Query latency | Minutes (batch) | Minutes | Days (legal process) |
| Collusion resistance | None against 2-of-3 collusion | None — TTP must be trusted | None |
| Cost per query | High at setup; low marginal | Moderate | Low compute, high legal |

### What to Measure

- Protocol audit: verify the MPC implementation against the stated threat model (semi-honest vs. malicious).
- Small-cell suppression policy: document k, what fraction of output is suppressed, and what fraction of total signal is lost.
- Repeated-differencing resistance: run at least three overlapping query windows and check whether differences reveal individual contributions.
- Schema drift handling: confirm the protocol fails safely (halts) rather than producing corrupt output when one party's schema changes.
- Incident path drill: simulate a suspected data-access violation and time the response from detection to root cause.

### Failure Modes

- **Collusion not modelled**: the semi-honest assumption fails if two of three parties collude; a deployment where the coordinator is a subsidiary of one data party is not actually semi-honest.
- **Small-cell leakage through repeated queries**: even with k-suppression, an analyst with query access can reconstruct suppressed cells by querying with slightly different filters.
- **Schema mismatch silently shifts metric**: if one party's event schema changes (e.g. a new impression type is added), the MPC output may be technically correct but meaningfully different from prior periods without any error being raised.
- **Governance theatre**: a query governance log that nobody reviews gives the appearance of auditability without the substance.

---

## Shared Reporting Summary

The table below maps each example to the shared reporting template from [Scorecards](scorecards.md).

| Field | Example 1: Private RAG | Example 2: HE vs TEE | Example 3: FL Medical | Example 4: Synthetic Data | Example 5: MPC Attribution |
| --- | --- | --- | --- | --- | --- |
| Workload | Role-gated QA over tiered document corpus | Loan-application scoring | Chest X-ray classification (6 hospitals) | Household income survey synthetic release | Cross-org ad conversion attribution |
| Protected asset | Prompts, retrieved snippets, answers, citations | Client features + model weights | Patient images, gradient updates | Individual survey records | Impression logs, purchase records |
| Adversary | Curious platform operator; injection attacker | Curious server (HE) / curious host OS (TEE) | Curious coordinator; single Byzantine site | Reconstruction / membership inference attacker | Curious co-participant; differencing attacker |
| Allowed output | Answers citing only authorised documents | Score value only | Global + per-site AUROC; no raw gradients | Aggregate statistics, regression coefficients | Aggregate conversion counts (k-suppressed) |
| PET stack | Hard ACL filter + optional TEE retrieval | HE (CKKS/BFV) or TEE (Intel TDX / AMD SEV) | Federated SGD + secure aggregation + DP | DP generative model (Gaussian mechanism, ε = 3) | 2-party MPC secret sharing |
| Evidence level | Expert judgment | Expert judgment | Expert judgment | Expert judgment | Expert judgment |
| Key failure mode | Soft-filter bypass; citation side-channel | HE: parameter mismatch; TEE: attestation skipped | DP destroys small-site utility | Rare-subgroup utility loss; ε inflation | Collusion not modelled; differencing via repeated queries |
