# I ❤️ PETs

A practical field guide to Privacy-Enhancing Technologies.

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

## This Is Not Another Awesome List

Existing repositories catalog papers and tools. This site is for the moment after
someone asks, "What should we actually build, buy, evaluate, or research?"

The guide is intentionally biased toward engineering review. A useful answer here
names the protected asset, the adversary, the allowed output, the operational
assumptions, and the measurement that would falsify the design. If a PET choice
cannot survive those questions, the right next step is not a bigger diagram; it is
a narrower claim.

I ❤️ PETs focuses on:

- choosing the right PET for a constraint, not a buzzword;
- drawing architectures with explicit trust boundaries;
- spotting privacy claims that are missing a threat model;
- turning vague "future work" into concrete research problems;
- learning from deployments without pretending every pilot is production.

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

- Federated learning does not provide privacy by itself.
- Synthetic data is not automatically safe to release.
- TEEs reduce exposure but add hardware, attestation, and side-channel assumptions.
- Homomorphic encryption protects data during computation but is constrained by latency, operators, and model design.
- MPC can be powerful, but many teams underestimate protocol, identity, and operations work.
- Differential privacy is the clearest formal privacy tool, but the utility cost and budget accounting must be measured.

## A Review Checklist For Any Page

When you use a page as input to a design review, leave with answers to these
questions:

| Question | Why it matters |
| --- | --- |
| What is the allowed output? | Most PET failures come from revealing too much after a private computation. |
| Who is the adversary? | A design for a curious coordinator can fail immediately against a malicious participant. |
| What assumption would break the claim? | Thresholds, attestation, local security, and budget accounting are often the real control plane. |
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
