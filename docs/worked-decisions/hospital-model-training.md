# Worked Decision: Training a Diagnostic Model Across Hospitals

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
| Secure aggregation | Hides individual site updates from the coordinator; the server sees only the aggregate. Directly addresses "a single site's update leaks its data." |
| Differential privacy (DP) | Adds a formal bound on how much any single patient (or site) influences the model. The route to a formal individual-privacy claim. |
| Robust aggregation | Limits damage from a faulty or poisoned site update. Relevant because a multi-org setting has weak control over each participant. |
| TEEs for orchestration | Run the aggregation server inside attested hardware to harden the coordinator. A supporting option, not the core. |

## 3. Rejected Options

This is the section that carries the judgment. Each rejection names the constraint the option violates.

| Rejected option | Why rejected |
| --- | --- |
| **Centralized training on pooled data** | The cleanest engineering path and the strongest utility — and forbidden by the stated constraint that raw records cannot move. If pooling were legally and operationally acceptable, it would likely win; here it is off the table. Rejected on legal/constraint grounds, not technical ones. |
| **Plain FL with no secure aggregation or DP** | FL alone is not a privacy guarantee. Per-round updates can leak training data, and with only five sites a single site's contribution is often distinguishable. Claiming privacy "because it is federated" is the canonical anti-pattern. Rejected as insufficient. |
| **MPC for the full training computation** | General MPC over deep-model training across five parties is operationally heavy and slow, and training is iterative (many rounds), multiplying the cost. MPC shines for bounded joint computations, not whole training loops. Rejected on cost/complexity. |
| **Homomorphic encryption for training** | HE over full model training is currently impractical for non-trivial architectures: operator support and latency do not hold up across many iterations. Rejected on feasibility. |
| **DP applied aggressively from day one** | DP is on the *recommendation*, but applying a tight budget before knowing the utility cost is a trap. With heterogeneous, smaller-site data, an over-tight budget can destroy per-site utility, especially for rare subgroups. We include DP but stage it — measure first, then bound. Rejected as a *default*, retained as a *deliberate* control. |

## 4. Final Recommendation

A staged stack, simplest first:

1. **Cross-silo federated learning** as the backbone. Raw records stay local; sites exchange model updates.
2. **Secure aggregation** so the coordinator sees only the summed update, never any single site's contribution. This closes the "single-site update leaks data" gap that plain FL leaves open.
3. **Robust aggregation** to bound the influence of a faulty or adversarial site update.
4. **Differential privacy — staged.** First train without DP and measure per-site and subgroup utility to establish a ceiling. Then introduce a defensible privacy unit (patient-level participation is usually the right unit here) and tune the budget against that ceiling. Adopt DP for the production model only once the utility cost is known and accepted by the review boards.
5. **TEE for the aggregation server** if the coordinator is not fully trusted, to harden orchestration with attestation.

For the canonical composition, see [FL + Secure Aggregation](../pet-architectures/fl-secure-aggregation.md) and [FL + Differential Privacy](../pet-architectures/fl-differential-privacy.md).

!!! tip "Sequencing matters"
    Stand up FL + secure aggregation + robust aggregation first and prove it trains. Layer DP only after you can quantify what it costs in utility. Adding DP blindly is how teams ship a model that is private and useless.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | Honest-but-curious coordinator (wants to infer a site's data from updates); a compromised or faulty participating site; an external attacker probing the final model. |
| Trust boundaries | Each hospital trusts its own infrastructure. The coordinator is *semi-trusted* — secure aggregation removes the need to trust it with individual updates. The final model is a release artifact crossing into clinician hands. |
| What this design protects | Raw patient records never leave a site. Individual site updates are hidden from the coordinator via secure aggregation. With DP enabled, the marginal influence of any single patient on the model is formally bounded. |
| What is **not** protected | Without DP, the *trained model itself* can still leak via membership-inference or reconstruction attacks. Secure aggregation hides per-site updates but not what the converged model memorizes. A malicious-majority collusion among sites breaks the aggregation assumptions. Side channels on the coordinator (timing, logs) are out of scope unless the TEE and logging controls are in place. See [Membership Inference](../threat-models/membership-inference.md) and [Collusion](../threat-models/collusion.md). |

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
| A review board demands a formal individual-privacy guarantee | DP becomes mandatory rather than staged; accept the utility cost and design around it from the start. |
| Strong evidence of poisoning risk among participants | Elevate robust aggregation and add participant attestation; consider restricting the consortium. |

!!! note "The honest summary"
    FL + secure aggregation gives you joint training without moving records. It does **not**, by itself, give you a formal individual-privacy guarantee — only DP does, and only at a measured utility cost. Decide which claim you actually need before you build.
