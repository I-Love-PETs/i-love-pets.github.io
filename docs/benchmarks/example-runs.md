# Benchmark Exercises

These five exercises show how to fill in the [benchmark scorecards](scorecards.md) for a specific workload. Each one identifies the controls to compare, what to measure, and failure modes to investigate. They report no measured results.

<span id="how-to-read-the-values"></span>

## How to report a result

Start each untested metric at **Needs evidence**. For a **Measured** result, record the workload, data shape, hardware, software versions, date, and who ran it. When citing a **Literature-backed** result, explain where its assumptions differ from your workload. Use the [Evidence Policy](../project-standards/evidence-policy.md) to label the source.

---

## 1. Private RAG — Confidential / Role-Gated Retrieval-Augmented Generation

### Workload Description

A legal or HR team runs a RAG system over a document corpus that is partitioned by access tier (public, internal, restricted, confidential). Users submit natural-language queries. The retriever must return only documents the user is authorised to see; the LLM must not leak restricted content into its generated answer even when restricted documents appear in the top-k results.

### Scorecard

| Category | What to measure | Evidence level |
| --- | --- | --- |
| Privacy claim | Prompt logging, retrieved-snippet exposure, citation leakage, answer leakage | Needs evidence |
| Utility | Answer quality (RAGAS faithfulness + answer relevance) by access tier | Needs evidence |
| Cost | p50 / p95 / p99 end-to-end latency; cloud cost per 1 000 queries | Needs evidence |
| Robustness | Prompt injection inside authorised documents; stale-permission cache; deleted-document residual | Needs evidence |
| Operations | Policy debugging trace; incident-response drill (answer sourced from restricted doc) | Needs evidence |

### Tradeoffs

| Axis | Hard permission filter (pre-LLM) | Soft filter (LLM instruction) |
| --- | --- | --- |
| Privacy boundary | The permission check runs before context assembly | Restricted documents can reach the model |
| Utility | Measure recall on documents the user may read | Including unauthorized hits can make apparent recall misleading |
| Latency | Include the authorization lookup in the timing | Measure the cost of the remaining checks |
| Complexity | Requires ACL service integration | Simpler to implement, harder to audit |

### What to Measure

- Leakage rate: fraction of adversarial probes where restricted content appears verbatim or paraphrastically in the answer.
- Citation policy: confirm the system does not cite documents whose *existence* is sensitive.
- Authorised-recall degradation: RAGAS or similar on authorised-only test set.
- Latency breakdown: ACL lookup, retrieval, LLM inference, total p50/p95/p99.
- Log review burden: time for a human reviewer to reconstruct a suspicious answer.

### Failure Modes

- **Soft-filter bypass**: An LLM told "do not reveal restricted content" can still disclose restricted content. Keep unauthorized documents out of the prompt and test how the system handles untrusted documents.
- **Stale ACL cache**: Permissions revoked in the source system are still honoured by a cached retriever, allowing access to documents the user should no longer see.
- **Citation side-channel**: Even when answer text is clean, a citation list can reveal that a restricted document exists and is relevant.
- **Embedding leakage**: In shared-index architectures, an attacker with repeated query access can reconstruct approximate document embeddings and infer content.

---

## 2. HE vs TEE Private Inference — Side-by-Side on a Tabular Classification Task

### Workload Description

A bank scores loan applications using a gradient-boosted tree model. The applicant's financial features are sensitive. The model is proprietary. Neither party should see the other's input or model weights. Both Homomorphic Encryption (HE) and a Trusted Execution Environment (TEE) are evaluated on the same task.

### Scorecard

| Category | HE approach | TEE approach |
| --- | --- | --- |
| Client inputs | Verify ciphertext handling, parameters, and who controls decryption | Verify the channel to the approved workload, then assess host and physical access |
| Model weights | Check whether the protocol hides model details from the decrypting client and what the scores reveal | Keep weights in the runtime and test what repeated scores reveal |
| Accuracy | Compare the adapted model and ciphertext computation with plaintext | Compare the exact workload and image used in the TEE with plaintext |
| Cost | Measure latency, throughput, ciphertext size, and key-management effort | Measure the same workload, including attestation and memory pressure |
| Operations | Test key rotation, rejected requests, and decryption failures | Test failed attestation, upgrades, key release, and what the host can see |

### Tradeoffs

The HE confidentiality claim depends on computational assumptions, parameters, and implementation. It does not establish circuit privacy or side-channel resistance. A TEE's claim depends on the hardware, software, and attestation boundary. Compare both on the same workload before deciding whether either fits the latency target. See [Private Inference](../pet-patterns/private-inference.md) and [Side Channels](../threat-models/side-channels.md).

### What to Measure

- Accuracy delta vs. plaintext baseline on held-out test set.
- p50 / p95 / p99 latency for single-record and batch (100, 1 000, 10 000 records).
- Ciphertext size (HE) or memory footprint inside TEE enclave.
- Attestation verification time (TEE).
- Key management failure scenarios: what does the client see if attestation fails?

### Failure Modes

- **HE parameter mismatch**: choosing CKKS noise budget or polynomial degree incorrectly produces silently wrong scores rather than errors.
- **TEE attestation not verified by client**: if clients skip verification, they cannot establish that they are sending data to the approved workload.
- **Model extraction via repeated HE queries**: encrypted inputs do not limit what a client can infer from repeated predictions.
- **Enclave memory limits**: measure the performance cost of memory pressure. Check how the chosen platform protects paging and whether guest swap, logs, or crash dumps leave the protected boundary. The presence of paging alone does not establish plaintext exposure.

---

## 3. Federated Learning Benchmark — Cross-Silo, Medical Imaging

### Workload Description

Six hospital sites collaboratively train a chest X-ray classification model (binary: abnormality present / absent). Each site holds 500–4 000 labelled images. Raw images stay at each hospital. The coordinator follows the protocol but can inspect what it receives. Compare plain FL with secure aggregation and a trusted DP operator that applies noise before releasing aggregates to the coordinator.

### Scorecard

| Category | What to measure | Evidence level |
| --- | --- | --- |
| Privacy claim | Check what the protocol reveals and report membership inference at low false-positive rates. Specify adjacency, clipping, sampling, and total DP accounting. | Needs evidence |
| Utility — global | AUROC on held-out global test set | Needs evidence |
| Utility — per-site | AUROC on each site's own test set | Needs evidence |
| Utility — subgroup | Demographic subgroup parity gap | Needs evidence |
| Cost | Rounds to convergence; communication per round; local GPU time | Needs evidence |
| Robustness | Non-IID label skew; one site dropout; one poisoned update (label flip) | Needs evidence |
| Operations | Participant onboarding time; monitoring dashboard | Needs evidence |

### Tradeoffs

Specify the protected unit before choosing the mechanism. Clipping whole site updates can bound site contributions under the matching adjacency and accountant. Patient-level privacy needs a patient-level bound, including any visits across sites. See [FL + Differential Privacy](../pet-architectures/fl-differential-privacy.md).

For the baseline, use secure summation. If evaluating a defense such as Krum that needs separate updates, use a distinct test arm with an explicit trust boundary or a protocol that computes the robust function without exposing its inputs.

### What to Measure

- DP accounting: per-round ε, total ε, δ, composition method (RDP, zCDP, or other).
- Global and per-site metrics with confidence intervals, not just the mean.
- Membership inference on the final model. Report true-positive rate at low false-positive rates with uncertainty, following [Carlini et al. (IEEE S&P 2022)](https://arxiv.org/abs/2112.03570).
- Communication cost: bytes sent and received per site per round.
- Dropout recovery: how many additional rounds when one site is unavailable?
- Subgroup performance across demographic groups represented in the data.

### Failure Modes

- **DP noise destroys small-site utility**: check whether utility drops on smaller sites and report uncertainty with the site metrics.
- **Non-IID drift**: heavy label imbalance across sites causes the global model to underperform every individual site's local model — a signal to reconsider the FL architecture.
- **Round poisoning at scale**: an update can affect the aggregate and downstream model. Test the defense under its stated number of adversarial sites and report when it fails.
- **Privacy budget burn-out**: without careful accounting, DP budget is exhausted before the model converges, stop or use a pre-approved budget plan. Continuing without the mechanism can invalidate the release claim.
- **Subgroup erasure**: rare demographic subgroups present only at one small site can be effectively erased from the global model without any privacy attack occurring.

---

## 4. Synthetic Data Release Review — DP Synthetic Tabular Data for Research

### Workload Description

A national statistics office releases a DP synthetic version of a household income survey (n = 50 000 records, 22 variables including age, income band, region, employment status). The intended downstream use is economic research: regression analysis and cross-tabulations. The release must pass internal review before public posting.

### Scorecard

| Category | What to measure | Evidence level |
| --- | --- | --- |
| Privacy claim | Nearest-neighbour distance ratio (NNDR); membership inference; DP accounting | Needs evidence |
| Privacy claim — rare records | Rare-region subgroup (n < 50 in real data) memorisation probe | Needs evidence |
| Utility — regression | Coefficients and standard errors for income ~ age + employment + region OLS | Needs evidence |
| Utility — cross-tabulations | Chi-squared statistics for key categorical pairs | Needs evidence |
| Utility — rare subgroup | Income distribution for smallest region | Needs evidence |
| Cost | Generation compute; parameter tuning iterations; privacy review | Needs evidence |
| Robustness | Distribution shift if real data updated; misuse outside intended tasks | Needs evidence |
| Operations | Release card completeness; residual-risk statement | Needs evidence |

### Release Gate Check

Use the [scorecard release gate](scorecards.md). Require the implemented DP parameters and accounting, similarity and membership test results, downstream utility results, and a statement of residual risk before recording a release decision.

### Tradeoffs

Compare candidate budgets against task-level and subgroup utility. Use public or proxy data for tuning or account for private selection. Report where utility falls below the release requirement.

### What to Measure

- NNDR and distribution overlap (e.g. Total Variation Distance per marginal).
- Membership inference AUC — report both mean and worst-case across 5 attack seeds.
- Task-level utility for every stated intended use, not just aggregate statistics.
- Rare-subgroup utility separately: a synthetic dataset that is excellent overall can be useless or misleading for minority subgroups.
- DP composition method and budget: report ε, δ, mechanism, and composition theorem used.

### Failure Modes

- **Releasing without a release card**: researchers misuse the synthetic data for tasks it was not designed for (e.g. individual-level inference from a dataset synthesised for aggregate analysis).
- **Overfitting to training data**: the mechanism or accounting may be incorrect, or the parameters may give a weak bound. Correctly implemented DP still allows exact matches with some probability. Investigate matches separately and verify the formal guarantee.
- **ε inflation through multiple releases**: releasing updated versions of the same synthetic dataset without tracking cumulative composition.
- **Utility-privacy miscommunication**: users can mistake a valid privacy guarantee for evidence that the data are accurate enough for their task.

---

## 5. MPC / Federated Analytics — Cross-Org Ad Attribution

### Workload Description

One ad platform and one retailer compute a joint conversion metric without revealing raw impression and purchase records to each other. The exercise uses a bilateral MPC protocol chosen to protect against one passive data party. No third party receives private inputs or occupies a compute role. The output is an aggregate conversion count, segmented by campaign and week.

### Scorecard

| Category | What to measure | Evidence level |
| --- | --- | --- |
| Privacy claim — input hiding | No party learns another party's raw impression or purchase records | Needs evidence |
| Privacy claim — output leakage | Small-cell suppression for cells with fewer than k records | Needs evidence |
| Privacy claim — differencing | Repeated queries with slightly shifted time windows | Needs evidence |
| Utility — metric accuracy | Conversion count vs. trusted centralised baseline (synthetic validation) | Needs evidence |
| Utility — decision impact | Campaign budget reallocation decisions made using MPC output vs. centralised | Needs evidence |
| Cost | End-to-end query time; per-party operational effort; schema negotiation | Needs evidence |
| Robustness | One party unavailable; malformed input record; schema drift | Needs evidence |
| Operations | Query governance log; allowed-output schema; incident path | Needs evidence |

### Tradeoffs

| Axis | MPC (secret sharing, semi-honest) | Trusted third party | Governance-only data sharing |
| --- | --- | --- | --- |
| Input confidentiality | Cryptographic (semi-honest) | Contractual | Contractual |
| Setup complexity | High — schema alignment, protocol integration | Moderate | Low |
| Timing | Measure end-to-end batch latency | Include data transfer and approvals | Include data transfer and approvals |
| Trust assumption | One passive party, under the selected protocol and output policy | Third party sees raw inputs | Recipients see whatever the agreement permits |
| Cost per query | High at setup; low marginal | Moderate | Low compute, high legal |

### What to Measure

- Protocol audit: verify the MPC implementation against the stated threat model (semi-honest vs. malicious).
- Small-cell suppression policy: document k, what fraction of output is suppressed, and what fraction of total signal is lost.
- Repeated-differencing resistance: run at least three overlapping query windows and check whether differences reveal individual contributions.
- Schema drift handling: confirm the protocol fails safely (halts) rather than producing corrupt output when one party's schema changes.
- Incident path drill: simulate a suspected data-access violation and time the response from detection to root cause.

### Failure Modes

- **Collusion not modelled**: a protocol that protects against passive parties does not cover deviations. Adding a compute party or a coordinator with access to inputs changes the trust model. Review its view and the tolerated coalitions before adopting that topology.
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
| PET stack | Hard ACL filter + optional TEE retrieval | HE (CKKS/BFV) or TEE (Intel TDX / AMD SEV) | Federated SGD + secure aggregation + DP | DP generative model with a documented privacy unit and budget | Two-party MPC with a documented passive security model |
| Evidence level | Needs evidence | Needs evidence | Needs evidence | Needs evidence | Needs evidence |
| Source quality | Unsourced / illustrative | Unsourced / illustrative | Unsourced / illustrative | Unsourced / illustrative | Unsourced / illustrative |
| Key failure mode | Soft-filter bypass; citation side-channel | HE: parameter mismatch; TEE: attestation skipped | DP destroys small-site utility | Rare-subgroup utility loss; ε inflation | Collusion not modelled; differencing via repeated queries |
