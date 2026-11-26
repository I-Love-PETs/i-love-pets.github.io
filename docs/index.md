---
description: "Choose privacy-enhancing technologies by allowed output, adversary, assumptions, leakage, and failure modes. A practical guide for engineers and architects."
---

# I ❤️ PETs

A practical field guide to Privacy-Enhancing Technologies for privacy engineers,
platform engineers, and architects deciding what to build and what to test.

**Start with what the system is allowed to reveal.** Then name the adversary,
assumptions, leakage surfaces, and failure modes. The guide connects those choices
to reusable patterns, concrete architectures, worked decisions, and evidence you
can inspect.

<div class="home-actions" markdown>

[Choose a PET](pet-compass/choose-a-pet.md){ .md-button .md-button--primary }
[Explore patterns](pet-patterns/index.md){ .md-button }
[Worked decisions](worked-decisions/index.md){ .md-button }
[Open problems](fix-my-itch/index.md){ .md-button }

</div>

New to PETs? [Start here](start-here/index.md) introduces the terms and the six-field decision framing.

<span id="find-your-path"></span>
<span id="fast-routing"></span>
<span id="what-makes-this-guide-useful"></span>
<span id="how-to-use-this-site"></span>

## When to rule out a PET

- **Skip plain federated learning if the coordinator must not see site updates.** Keeping records local still leaves updates visible. Check the trust boundary in the [hospital training decision](worked-decisions/hospital-model-training.md).
- **Skip identity-revealing PSI if participants may learn only a count.** The match list is itself a disclosure. Compare the outputs in [Private Set Intersection](pet-patterns/private-set-intersection.md#do-not-use-psi-when).
- **Skip a TEE if you cannot establish who can access the hardware.** Valid attestation depends on the platform's threat assumptions. See the [private inference decision](worked-decisions/private-model-inference.md).

Use the [reader paths](start-here/reader-paths.md) for a guided walkthrough, or check the
[Evidence Policy](project-standards/evidence-policy.md) before relying on a claim.

## Opinionated Defaults

These are starting points for review. The evidence supports the scoped properties
below; it does not establish a universal PET ranking.

- **Review FL updates as sensitive data.** Published gradient-reconstruction attacks show why keeping raw records local is insufficient. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. [Zhu et al., Deep Leakage from Gradients](https://arxiv.org/abs/1906.08935), 2019; the demonstrated attacks do not imply every training setup is equally vulnerable.)*
- **Evaluate synthetic releases before sharing them.** Generated records can retain disclosure risk. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. [Giomi et al.](https://arxiv.org/abs/2211.10459), 2022, evaluates singling-out, linkability, and inference risks; attack tests are not a proof that no leakage remains.)*
- **Review the selected TEE and its attestation workflow.** Hardware isolation has platform-specific limits. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. [Foreshadow](https://foreshadowattack.eu/), 2018, demonstrated attacks on Intel SGX; assess the current platform and mitigations separately.)*
- **Check HE parameters and benchmark the actual model.** HE security relies on scheme and parameter choices. *(Evidence: Literature-backed. Source quality: Primary / official. [HE Security Standard](https://homomorphicencryption.org/standard/), 2018. Latency, operator fit, and accuracy for your model remain Needs evidence until measured.)*
- **Budget for MPC participant operations.** Identity, availability, and collusion assumptions are part of the design review. *(Evidence: Expert judgment. Source quality: Unsourced / illustrative. Reviewed 2026-09-18. Coordination work motivates this default; a measured workload and operating plan can change it.)*
- **Use DP when the release needs a quantified contribution guarantee.** Define adjacency, privacy unit, parameters, and accounting first. *(Evidence: Literature-backed. Source quality: Primary / official. [NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final), 2025. Utility and parameter acceptability still need workload-specific evaluation.)*

## A Review Checklist For Any Page

When you use a page as input to a design review, leave with answers to these
questions:

| Question | Why it matters |
| --- | --- |
| What is the allowed output? | A protected computation can still reveal sensitive information through its allowed output. |
| Who is the adversary? | A design for a curious coordinator can fail immediately against a malicious participant. |
| What assumption would break the claim? | Thresholds, attestation, local security, and budget accounting determine where the claim holds. |
| What is the first benchmark? | Utility, latency, cost, and privacy evidence should be measured before procurement or launch. |
| What would make us switch PETs? | A reversible decision is easier to govern than a technology commitment. |

## Main Sections

- [Start Here](start-here/index.md): shared vocabulary and taxonomy.
- [PET Compass](pet-compass/index.md): decision support by data movement, threat model, and ML task.
- [Worked Decisions](worked-decisions/index.md): end-to-end PET choices for common scenarios.
- [PET Patterns](pet-patterns/index.md): reusable designs such as federated analytics, private inference, and private RAG.
- [Use Cases](use-cases/index.md): domain constraints in healthcare, finance, advertising, public sector, and AI.
- [Benchmarks](benchmarks/index.md): how to measure privacy, utility, cost, latency, scalability, and developer effort.
- [Tool Reviews](tool-reviews/index.md): tool evaluations tied to concrete architectures, threat models, and first benchmarks.
- [Contributing](contributing/index.md): quality bar for improving the guide.

## Related Starting Points

- [Reader Paths](start-here/reader-paths.md) for ordered reading sequences.
- [Worked Decisions](worked-decisions/index.md) for examples of complete PET choices.
- [Benchmark Scorecards](benchmarks/scorecards.md) for turning a recommendation into evidence.
