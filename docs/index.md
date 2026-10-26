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

## Find Your Path

<div class="grid cards" markdown>

- :material-compass-outline: **I need to choose a PET**

    ---

    You have a real system and a privacy constraint. Start with the guided chooser.

    [:octicons-arrow-right-24: Choose a PET](pet-compass/choose-a-pet.md)

- :material-vector-square: **I need to design an architecture**

    ---

    You know your PET candidate and need actors, data flows, and trust boundaries.

    [:octicons-arrow-right-24: PET Architectures](pet-architectures/index.md)

- :material-magnify: **I need to evaluate a claim**

    ---

    A vendor or paper makes a privacy claim. Check it against the evidence policy and the claim register.

    [:octicons-arrow-right-24: Evidence Policy](project-standards/evidence-policy.md) &nbsp;·&nbsp; [Claim Register](project-standards/claim-register.md)

- :material-flask-outline: **I need a research problem**

    ---

    You want a concrete open problem with success criteria and a first contribution.

    [:octicons-arrow-right-24: Fix My Itch](fix-my-itch/index.md)

- :material-database-search-outline: **I need evidence from deployments**

    ---

    You want deployment maturity, source quality, and lessons from real production use.

    [:octicons-arrow-right-24: Deployments](deployments/index.md)

- :material-clipboard-check-outline: **I need a worked decision**

    ---

    You want to see a PET choice made under realistic constraints before you copy the pattern.

    [:octicons-arrow-right-24: Worked Decisions](worked-decisions/index.md)

- :material-tools: **I need to evaluate a PET tool**

    ---

    You want to know whether a library or platform fits a threat model, architecture, and first benchmark.

    [:octicons-arrow-right-24: Tool Reviews](tool-reviews/index.md)

</div>

Not sure where to start? Read the [guided reader paths](start-here/reader-paths.md).

## Fast Routing

| You have... | Go to... | Then check... |
| --- | --- | --- |
| A concrete use case but no PET shortlist | [Use Cases](use-cases/index.md) | [PET Compass](pet-compass/index.md) |
| A PET candidate but no design | [PET Architectures](pet-architectures/index.md) | [Threat Models](threat-models/index.md) |
| A vendor/tool claim | [Tool Reviews](tool-reviews/index.md) | [Evidence Policy](project-standards/evidence-policy.md) |
| A proposed deployment claim | [Deployments](deployments/index.md) | [Claim Register](project-standards/claim-register.md) |
| A research or contribution idea | [Fix My Itch](fix-my-itch/index.md) | [Contributing](contributing/index.md) |

## What makes this guide useful

Each design connects an allowed output to the people who may observe it, the
assumptions needed to protect inputs, and the ways the system can still fail.
Recommendations include reasons to change course. Deployment and benchmark
pages distinguish sourced evidence from illustrative examples using one
[Evidence Policy](project-standards/evidence-policy.md).

You can use a page to prepare a design review, choose a first benchmark, or find
a concrete research problem. Coverage is selective; [v1.0 readiness](project-standards/version-history.md#v10-definition-of-done)
means a consistent decision framework and publishing baseline, not complete PET coverage.

## How To Use This Site

Use the site as a field guide, not a textbook.

| If you need to... | Start with... | You should leave with... |
| --- | --- | --- |
| Pick a PET for a real system | [PET Compass](pet-compass/index.md) | A primary candidate, likely supporting PETs, and reasons to reject the wrong options |
| Explain how a PET design works | [PET Architectures](pet-architectures/index.md) | Actors, data flows, trust boundaries, assumptions, and failure modes |
| Compare recurring designs | [PET Patterns](pet-patterns/index.md) | When to use a pattern, when not to use it, and what to measure |
| See a decision worked through end to end | [Worked Decisions](worked-decisions/index.md) | A recommended PET stack, what can go wrong, what to measure, and when the choice changes |
| Check whether a privacy claim is credible | [Threat Models](threat-models/index.md) | The adversary, the protected asset, and what the PET does not protect |
| Evaluate a tool or platform | [Tool Reviews](tool-reviews/index.md) | Fit, evidence level, operational risks, first benchmark, and when not to use it |
| Exercise a benchmark scorecard | [Benchmark Example Runs](benchmarks/example-runs.md) | A hypothetical workload, scorecard fields, failure modes, and measurement plan |
| Find a useful research problem | [Fix My Itch](fix-my-itch/index.md) | A concrete problem, current workaround, success criteria, and a first contribution |
| Judge whether a deployment claim is meaningful | [Deployments](deployments/index.md) | Deployment maturity, source quality, lessons, and unresolved caveats |

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
