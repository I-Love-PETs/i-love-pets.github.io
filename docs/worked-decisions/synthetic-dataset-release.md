# Worked Decision: Releasing a Synthetic Version of a Sensitive Dataset

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Figures are illustrative and labeled. Validate utility, memorization, and membership-inference risk on the actual generator and data before any release.

A team holds a sensitive tabular dataset — say, customer records or patient-derived data — and wants to publish a synthetic stand-in so researchers, vendors, or other teams can build and test without touching real records. The dangerous assumption is "synthetic means safe." It does not. A generator can memorize rare records, reproduce identifying outliers, and leak sensitive correlations. The decision is really about *what privacy claim the release needs to make* and *what it costs in utility*.

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | A sensitive structured dataset with common patterns plus a long tail of rare, potentially identifying records. |
| Parties | The data owner (releaser), downstream consumers (researchers, vendors, internal teams), the individuals represented in the data, and reviewers/regulators who may scrutinize the release. |
| Constraints | Once published, a release cannot be recalled. Consumers want fidelity high enough to be useful. The owner may need to make a *formal* statement about individual privacy. Rare records and small subgroups are where re-identification risk concentrates. |
| What success looks like | A released artifact useful enough for the intended downstream tasks, with a clear and honest privacy statement, demonstrated resistance to memorization and membership inference, and documented residual risk — especially for rare subgroups. |

!!! note "Decide if you even need a release"
    A static synthetic release is the highest-commitment option because it is irrevocable. If consumers only need statistics or model outputs, a *query interface* with DP is often safer and cheaper than publishing a dataset. Start by asking whether a release is genuinely required.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| DP synthetic data | A generator trained under differential privacy gives a formal individual-privacy claim for the release. The main route when the release needs a defensible guarantee. See [DP Synthetic Data Release](../pet-patterns/dp-synthetic-data-release.md). |
| Memorization / similarity testing | Nearest-neighbor and duplication tests to catch the generator copying training records. Essential evaluation regardless of generator. |
| Membership-inference evaluation | Quantifies whether an attacker can tell if a record was in the training set. Turns "we think it's safe" into a measured risk. |
| Utility benchmarking | Downstream task performance and distributional fidelity tests, so the release is known to be useful, not just safe. |
| DP query access (alternative to release) | If a dataset is not strictly required, a DP query interface answers statistics without publishing records at all. |

## 3. Rejected Options

| Rejected option | Why rejected |
| --- | --- |
| **Non-DP generative model, released as "synthetic = safe"** | The headline trap. Standard generators can and do memorize rare records and reproduce outliers verbatim, and offer no formal individual-privacy bound. Releasing without a privacy evaluation is how "synthetic" data leaks real people. Rejected as unsafe by default. |
| **Classic de-identification / k-anonymity on the real data** | Removing identifiers and generalizing fields is well known to be vulnerable to linkage attacks, and it degrades utility while still shipping real (if masked) records. For a public-style release this is weaker than DP synthetic data. Rejected as insufficient. |
| **DP with an arbitrarily tight budget chosen for optics** | DP is on the recommendation, but a budget picked to *sound* strong, without checking utility, typically produces a synthetic dataset that is useless — destroying the reason to release it. Rejected as a *reflex*; the budget must be chosen against measured utility. |
| **Releasing high-fidelity individual-level data broadly** | If consumers truly need high-fidelity individual records, no synthetic method will both preserve that fidelity and protect individuals; the honest move is *restricted sharing* under contract, not a public synthetic release. Rejected for broad release; redirected to controlled access. |
| **Skipping memorization/membership testing to ship faster** | Without these tests, the privacy statement is unfalsifiable. A release you cannot evaluate is a release you cannot defend. Rejected — testing is non-negotiable. |

## 4. Final Recommendation

Choose by the claim the release must support:

- **If the release needs a formal individual-privacy claim:** train a **DP synthetic data generator**, then *gate the release on evaluation*:
  1. **Choose the privacy unit and budget deliberately** (typically per-individual), and tune the budget against **measured downstream utility** — not against optics.
  2. Run **memorization / nearest-neighbor tests** to confirm the generator is not copying records.
  3. Run a **membership-inference evaluation** to quantify residual risk.
  4. Run **utility benchmarks** on the intended downstream tasks, including rare-subgroup behavior.
  5. Publish with an **honest residual-risk statement** and the privacy parameters.
- **If consumers only need statistics or model outputs:** prefer a **DP query interface** over a static release — it is revocable, rate-limitable, and avoids shipping a dataset at all.
- **If high-fidelity individual records are genuinely required:** abandon public release; use **restricted, contractual sharing** with access controls and audit.

See [Synthetic Data Release Pipeline](../pet-architectures/synthetic-data-release-pipeline.md).

!!! tip "Tune the budget to utility, then state it"
    The right DP budget is the one that meets your utility bar with the strongest guarantee achievable — discovered by measurement, not chosen for the press release. Then publish the actual parameters so reviewers can judge them.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | An attacker who downloads the release and tries to re-identify individuals, confirm membership, or recover rare records; an over-trusting consumer who treats "synthetic" as "risk-free." |
| Trust boundaries | After release, there is no boundary — the artifact is public (or broadly shared) and permanent. All protection must be baked in *before* publication. |
| What this design protects | With DP, the formal influence of any single individual on the released generator is bounded. Memorization and membership tests provide empirical evidence that rare records are not reproduced and membership is hard to infer. |
| What is **not** protected | DP bounds individual influence but does **not** guarantee zero utility loss, nor does it protect sensitive *population-level correlations* that may themselves be sensitive to disclose. Rare subgroups remain the highest-risk region even under DP. A non-DP generator protects *nothing* formally. Over-trust by downstream users is a human risk no algorithm removes. See [Membership Inference](../threat-models/membership-inference.md). |

!!! warning "Synthetic is not a privacy guarantee"
    "It's synthetic" describes how the data was generated, not how private it is. Only a privacy mechanism (DP) plus evaluation (memorization, membership inference) supports a defensible claim. State the residual risk explicitly; do not let "synthetic" do the work that evidence should.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Privacy (formal) | DP privacy budget and the privacy unit it protects | Needs evidence — must be set and reported per release |
| Memorization | Nearest-neighbor similarity between synthetic and training records; verbatim duplication rate | Needs evidence — the first test that catches copying |
| Membership inference | Attacker success rate at distinguishing training members | Needs evidence — turns belief into a number |
| Utility | Downstream task performance vs. real data; distributional fidelity | Expert judgment (2026-06-10): expect noticeable utility loss under meaningful DP; quantify it |
| Rare-subgroup behavior | Utility and risk specifically for small/rare subgroups | Needs evidence — risk and utility both concentrate here |
| Cost / effort | Generator training cost; evaluation effort; review/governance burden | Expert judgment (2026-06-10): evaluation and review often exceed generation cost |
| Residual-risk clarity | Whether the release documents what it does *not* protect | Expert judgment (2026-06-10): a release without a residual-risk statement is incomplete |

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| Consumers only need aggregate statistics | Replace the release with a **DP query interface** — revocable and lower-risk. |
| Required fidelity is incompatible with any acceptable DP budget | Stop trying to release publicly; move to **restricted contractual sharing** of real data under access controls. |
| Memorization or membership tests fail | Do **not** release. Re-train with a tighter budget or different generator and re-test until evidence supports the claim. |
| Population-level correlations are themselves sensitive | DP on individuals will not cover this; add disclosure review and possibly suppress or coarsen those relationships. |
| A regulator demands a specific formal guarantee | DP becomes mandatory with a documented budget and accounting; design to that requirement from the start. |
| Utility under DP is acceptable but reviewers distrust "synthetic" | Lead with the **evidence package** (budget, memorization, membership results) rather than the word "synthetic." |

!!! note "The honest summary"
    A synthetic release is irrevocable, so the privacy work happens before publication, not after. DP provides the formal claim; memorization and membership testing provide the evidence; an honest residual-risk statement provides the integrity. If any of the three is missing, do not ship.
