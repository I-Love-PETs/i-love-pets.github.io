# Worked Decision: Training a Diagnostic Model Across Hospitals

--8<-- "decision-guidance.md"

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Numbers are illustrative and labeled. Validate per-site utility, leakage risk, and cost on the real cohort before any clinical use.

A consortium of five hospitals wants a shared diagnostic model — say, detecting a condition from imaging plus structured EHR features. Each hospital believes the pooled signal would beat any single-site model, but legal, ethical, and contractual constraints forbid moving raw patient records off-site. The question is not "which PET is most private" but "what is the least complex stack that lets us train jointly and make a defensible privacy statement."

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | Patient-level imaging and structured EHR features at each hospital. Highly sensitive, regulated, non-portable. |
| Parties | Five hospitals (data holders), one coordinating party (consortium or trusted academic center), downstream clinicians as model users. |
| Constraints | Raw records cannot leave each site. Cross-border or cross-org pooling is legally blocked. Sites have uneven data volume and quality. Model must work acceptably for *every* site, not just the largest. |
| What success looks like | A global model that beats each site's local model on held-out data, no raw-record movement, a privacy statement defensible to each hospital's review board, and per-site performance that does not quietly fail smaller hospitals. |

!!! note "The real blocker is data movement, not aggregation math"
    Before reaching for a PET, confirm the blocker is genuinely that raw data cannot move. If the true obstacle is governance, liability, or incentives, a federated architecture adds complexity without solving the actual problem. Here we assume non-portability is real and legally grounded.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| Cross-silo federated learning (FL) | Keeps raw records local; each site trains and shares only model updates. The natural fit when data cannot centralize. See [Cross-Silo Federated Learning](../pet-patterns/cross-silo-federated-learning.md). |
| Secure aggregation | Limits the protocol output to the aggregate under the stated adversary and participation bounds. The aggregate may still reveal information about individual sites. |
| [Differential privacy](../start-here/glossary.md#differential-privacy) (DP) | Adds a formal bound on how much any single patient (or site) influences the model. The route to a formal individual-privacy claim. |
| Robust aggregation | Limits damage from a faulty or poisoned site update. Relevant because a multi-org setting has weak control over each participant. |
| TEEs for orchestration | Run the aggregation server inside attested hardware to harden the coordinator. A supporting option, not the core. |

## 3. Rejected Options

This is the section that carries the judgment. Each rejection names the constraint the option violates.

| Rejected option | Why rejected |
| --- | --- |
| **Centralized training on pooled data** | The cleanest engineering path and the strongest utility — and forbidden by the stated constraint that raw records cannot move. If pooling were legally and operationally acceptable, it would likely win; here it is off the table. Rejected on legal/constraint grounds, not technical ones. |
| **Plain FL with no secure aggregation or DP** | FL alone is not a privacy guarantee. Per-round updates can leak training data, and with only five sites a single site's contribution is often distinguishable. Claiming privacy "because it is federated" is the canonical anti-pattern. Rejected as insufficient. |
| **[MPC](../start-here/glossary.md#mpc) for the full training computation** | General MPC over deep-model training across five parties is operationally heavy and slow, and training is iterative (many rounds), multiplying the cost. MPC shines for bounded joint computations, not whole training loops. Rejected on cost/complexity. |
| **[Homomorphic encryption](../start-here/glossary.md#homomorphic-encryption) for training** | For this iterative imaging model, require evidence on operator support and end-to-end training cost before adopting HE. Simpler models may have different tradeoffs. |
| **Picking a privacy budget after unaccounted private tuning** | Decide the privacy unit and an acceptable budget with the review boards. Use public or proxy data for initial tuning, or include private tuning that affects the release in the privacy accounting. |

## 4. Final Recommendation

A staged stack, simplest first:

1. **Cross-silo federated learning** as the backbone. Raw records stay local; sites exchange model updates.
2. **Secure aggregation** to limit direct access to updates. Use the five-site, four-response example in [FL + Secure Aggregation](../pet-architectures/fl-secure-aggregation.md#assumptions), scoped to a passive coordinator and at most one colluding passive site. The consortium identity authority owns enrollment and credential rotation. See [Bonawitz et al. (CCS 2017), §6.1](https://doi.org/10.1145/3133956.3133982).
3. **A poisoning defense**, if required. A plain sum cannot also run a defense that needs individual updates. Evaluate a compatible protocol or explicitly change who can see the inputs.
4. **Patient-level differential privacy** if the consortium needs a bound on the released model. Bound each patient’s total contribution, including repeat visits and participation at multiple sites. Account for private tuning, validation outputs, and checkpoints that influence or form part of the release. Check subgroup and per-site utility within the approved budget. See [NIST SP 800-226](https://doi.org/10.6028/NIST.SP.800-226).
5. **If the coordinator can deviate**, require actively secure aggregation and verified agreement across sites on the approved round configuration. An attested environment can constrain approved orchestration code if its hardware trust assumptions are acceptable. [Pasquini, Francati, and Ateniese (CCS 2022)](https://arxiv.org/abs/2111.07380) shows why secure summation alone does not address model inconsistency.

For the canonical composition, see [FL + Secure Aggregation](../pet-architectures/fl-secure-aggregation.md) and [FL + Differential Privacy](../pet-architectures/fl-differential-privacy.md).

!!! tip "Sequencing matters"
    Exercise the training and aggregation pipeline on public or simulated data first. Before private training results influence the release, specify who can see intermediate values and how the accountant covers training, tuning, and evaluation.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | For update confidentiality, a passive coordinator and up to one colluding passive site. Analyze active coordinator or site behavior separately. For release privacy, consider downstream users probing the model. |
| Trust boundaries | Each hospital trusts its own infrastructure. The base design trusts the coordinator to follow the protocol. Only the designated DP operator may see the pre-noise aggregate when using central DP. The final model is a release artifact crossing into clinician hands. |
| What this design protects | Raw patient records never leave a site. The aggregation protocol hides individual inputs beyond what the permitted sum and coalition knowledge reveal. The model has a patient-level DP bound only if the contribution limits and release accounting cover each patient. |
| What is **not** protected | Without DP, the *trained model itself* can still leak via membership-inference or reconstruction attacks. Secure aggregation hides per-site updates but not what the converged model memorizes. The passive five-site example makes no claim for active deviation, more than one colluding site, or rounds below threshold. Timing, logs, and inference from the aggregate need their own review. See [Membership Inference](../threat-models/membership-inference.md) and [Collusion](../threat-models/collusion.md). |

!!! warning "Secure aggregation is not differential privacy"
    Secure aggregation protects updates *in transit/aggregation*. It says nothing about what the final model memorizes. If your privacy statement needs to bound individual influence on the released model, you need DP. Do not conflate the two.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Privacy | Privacy budget per patient unit (if DP); membership-inference success rate against the released model | Needs evidence — must be measured on the real model |
| Utility (global) | Global model performance vs. each site's local model on held-out data | Expert judgment (2026-06-10): expect a positive lift for smaller sites; confirm empirically |
| Utility (fairness) | Per-site and per-subgroup performance, especially smallest hospital and rare conditions | Needs evidence — the failure mode hides here |
| Robustness | Model degradation under a simulated poisoned/faulty site update | Needs evidence |
| Cost | Per-round local compute and communication cost; total rounds to convergence | Expert judgment (2026-06-10): communication-bound, not compute-bound, for typical silo counts |
| Latency | Wall-clock per training round including secure aggregation overhead | Needs evidence |
| Complexity | Operational effort to keep five sites synchronized; dropout handling | Expert judgment (2026-06-10): the dominant ongoing cost is coordination, not cryptography |

The subgroup row is the one most teams skip and most regret. A global model that improves the average while quietly degrading the smallest hospital's patients is a failure, not a success.

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| Legal/governance unblocks pooling | Reconsider **centralized training** with strong governance — usually higher utility and far lower operational complexity. |
| The task is analytics, not training (e.g., joint cohort statistics) | Switch to **federated analytics or MPC** for the specific computation rather than full FL. |
| Only two or three sites, and one dominates | FL's benefit shrinks and update-leakage risk per site rises; weigh whether a clean-room or governed sharing arrangement serves better. |
| DP destroys utility for rare subgroups | Re-examine the privacy unit and budget owner; consider whether a non-DP model with strong access governance is the honest trade, and document the residual risk. |
| A review board demands a formal patient-level DP guarantee | Include patient-level DP in the design and acceptance criteria from the start. If utility fails within the approved budget, reconsider the release. |
| Strong evidence of poisoning risk among participants | Elevate robust aggregation and add participant attestation; consider restricting the consortium. |

!!! note "The honest summary"
    Use secure aggregation to limit what the coordinator learns about site updates. Use patient-level DP if the released model needs a bound on each patient’s influence. Review the two guarantees separately.
