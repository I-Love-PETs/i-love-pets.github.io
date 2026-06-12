# OpenDP

> Worked example applying the [tool evaluation framework](../contributing/tool-evaluation-framework.md) and [tool review template](../contributing/tool-template.md). Reviewed 2026-06-10. Not an endorsement.

## Evaluation Summary

| Field | Answer |
| --- | --- |
| What it helps build | A [DP synthetic data release](../pet-patterns/dp-synthetic-data-release.md) or, more directly, differentially private statistics and aggregate releases with formal, tracked privacy loss |
| PET family | DP (low-level library with a verified core and privacy accounting) |
| Best fit | Releasing aggregate statistics from a sensitive tabular dataset with a defensible, end-to-end `epsilon`/`delta` budget |
| Fit label | Strong fit (for rigorous DP statistics); narrow fit as a turnkey product |
| Evidence level | Literature-backed (programming-framework paper + per-mechanism proofs); Deployment-backed for adoption |

## What It Helps Build

OpenDP is a modular library of differentially private algorithms with a Rust core and Python and R bindings on that same core. You assemble a DP release by chaining **transformations** (deterministic data operations, e.g. a bounded sum) with **measurements** (randomised, DP-introducing operations, e.g. Laplace or Gaussian noise), and the library computes the resulting privacy loss for you via **privacy maps** ([OpenDP docs](https://docs.opendp.org/en/stable/index.html), [programming framework](https://docs.opendp.org/en/stable/api/user-guide/programming-framework/index.html)).

It is the engine under a [DP synthetic data release](../pet-patterns/dp-synthetic-data-release.md) or a [synthetic data release pipeline](../pet-architectures/synthetic-data-release-pipeline.md), and the natural tool for the DP work in [federated analytics](../pet-patterns/federated-analytics.md) where you need a defensible accountant rather than hand-rolled noise.

## Protected Assets

The protected asset is the **presence or absence of any one individual's record** in the input dataset, and by extension any per-individual attribute. DP's guarantee is about **outputs**: the released statistics are calibrated so that an attacker cannot tell whether a given person was in the dataset. OpenDP protects the *release*, not the storage or transport of the raw data — those remain your responsibility.

## Threat Model Support

- **In scope**: an adversary who sees the released output (and may have arbitrary auxiliary knowledge) trying to perform [membership inference](../threat-models/membership-inference.md) or reconstruction. This is the canonical DP threat model and is exactly what OpenDP's privacy maps bound.
- **Local-DP support**: OpenDP includes randomized-response mechanisms for the local model, where individuals randomise their own data before it ever reaches a collector ([measurements reference](https://docs.opendp.org/en/stable/api/user-guide/measurements/index.html)).
- **Explicitly out of scope**: anyone with access to the *raw* data, the correctness of your sensitivity bounds (if you declare wrong bounds, the guarantee is void), and side channels. OpenDP hardened one such channel by requiring an opt-in "honest-but-curious" flag before arbitrary post-processors can be built, precisely because a malicious post-processor (e.g. one reading the system clock) could leak via timing ([0.12 release notes](https://opendp.org/2024/12/20/announcing-opendp-library-0-12/)).

## Best Fit

Use OpenDP when:

- you must release statistics or a synthetic dataset from sensitive records and need a **formal, end-to-end privacy budget** you can defend to a regulator or DPO;
- you want privacy accounting handled by a vetted library (privacy maps, composition, RDP / zCDP / approximate-DP measures) rather than hand-derived;
- you value a security-reviewed Rust core with the same logic exposed to Python and R;
- you can express your release as a chain of transformations and measurements.

## When Not To Use

Avoid, or budget heavily, when:

- you want a turnkey "add DP to my SQL/ML" product. OpenDP is deliberately **low-level**; the maintainers themselves point to higher-level tools such as SmartNoise SDK (which is built on OpenDP) for SQL-style interfaces;
- your team cannot reason about sensitivity bounds, clipping, and `epsilon` budgets — misdeclared bounds silently break the guarantee;
- your privacy concern is about data *in transit or at rest*, not about what a released output leaks (use encryption / access control / a [TEE](confidential-computing-platform.md));
- you need high-dimensional DP deep learning specifically — a gradient-perturbation library like Opacus may fit that workload more directly (note this as a comparison to evaluate, not a settled verdict).

## Privacy Claims

OpenDP claims **provable differential privacy** for releases assembled from its vetted components, with the privacy loss computed by the library. The claim is credible because: (1) the architecture is grounded in a published programming framework; (2) mechanisms ship with proofs and a stated independent-review process; and (3) the project reports having performed well in independent security audits ([Why OpenDP](https://docs.opendp.org/en/stable/index.html)). The claim is *conditional* on correct sensitivity declarations and on staying within vetted ("non-`contrib`") components.

## Benchmarks Or Evidence

- **Formal evidence** (Literature-backed): the programming-framework paper plus per-mechanism proofs; a documented algorithm-review process; reported independent security audits.
- **Adoption** (Deployment-backed): named users include the UN High Commissioner for Refugees (synthetic microdata exploration), the Swiss Federal Statistical Office (income-statistics prototyping; the Lomas platform), Oblivious/Antigranular, OpenMined/PySyft pilots, and multiple research groups ([Who is using OpenDP](https://docs.opendp.org/en/stable/index.html)). MIT-licensed.
- **Maturity caveat** (honest): the project self-labels as a **work in progress** ("repostatus: WIP") and warns that, like all software, it has known and unknown issues you must evaluate for privacy-critical use ([README / repo status](https://github.com/opendp/opendp/)). Latest release as of this review is v0.14.2 (2026-03-11).
- **Utility for your release** (Needs evidence): the noise-vs-utility tradeoff for *your* statistics at *your* `epsilon` is not a published constant; it must be measured.

## First Benchmark To Run

Per the framework's DP row: **privacy accounting and a utility curve for a specific release.**

1. Pick one concrete release (e.g. grouped counts or a mean over a sensitive column).
2. Build it with `enable_features("contrib")` only where unavoidable, declaring explicit bounds/sensitivity; chain a transformation (e.g. `make_sum`) with a measurement (`make_laplace`/`make_gaussian`).
3. Sweep `epsilon` (and `delta` if using approximate-DP) and plot a **utility curve**: accuracy/confidence-interval width vs privacy spent, using OpenDP's accuracy helpers.
4. For releases with sensitive grouping keys, exercise the thresholded mechanisms (`make_laplace_threshold`) and confirm rare categories are suppressed.
5. Record the *total* budget under composition — the number you would actually have to defend.

## Operational Notes

- **Setup**: `pip install opendp` (or R-universe / crates.io). The Rust core gives memory/thread safety; Python and R share it for consistency.
- **Accounting discipline**: measurements do not carry a fixed privacy loss; you specify noise scale and the privacy *map* reports the loss. Tracking and summing the budget across all releases is an operational responsibility, not an afterthought.
- **`contrib` gating**: unvetted components require an explicit opt-in flag. Treat any `contrib` use as "not yet proof-backed" in your risk register.
- **Upgrades / churn**: frequent releases and breaking changes (privacy-measure renames, ordering changes) mean you should pin versions and re-test accounting on upgrade.
- **Post-processing**: building custom post-processors now requires the honest-but-curious opt-in — do not bypass it casually.

## Failure Modes

- Declaring loose or wrong sensitivity bounds, which voids the guarantee while still "running fine."
- Forgetting composition: many small releases sum to a large real `epsilon`.
- Treating a `contrib` (unvetted) mechanism as if it were proof-backed.
- Confusing DP on a *release* with protection of the *raw* dataset, which OpenDP does not provide.
- Reading too much into adoption: that UNHCR or a statistics office *used* OpenDP does not mean your `epsilon` is appropriate.

## Review Verdict

**Recommend for rigorous DP statistics; flag as low-level.** OpenDP is a defensible representative of the DP family for this guide: it is grounded in a published framework, ships proofs, reports audits, and has credible institutional adoption. The honest caveats are its self-declared WIP status and its deliberately low-level interface — for SQL/ML-style ergonomics, evaluate a higher-level layer built on it (e.g. SmartNoise SDK). Recommend it where you need a defensible budget and have the expertise to declare correct bounds; otherwise watch.

## Related Pages

- Pattern: [DP Synthetic Data Release](../pet-patterns/dp-synthetic-data-release.md)
- Architecture: [Synthetic Data Release Pipeline](../pet-architectures/synthetic-data-release-pipeline.md)
- Pattern: [Federated Analytics](../pet-patterns/federated-analytics.md)
- Threat model: [Membership Inference](../threat-models/membership-inference.md)
- Itch: [Differential Privacy](../fix-my-itch/differential-privacy.md)
