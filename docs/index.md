# I ❤️ PETs

A practical field guide to Privacy-Enhancing Technologies.

## This Is Not Another Awesome List

Existing repositories catalog papers and tools. This site is for the moment after
someone asks, "What should we actually build, buy, evaluate, or research?"

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
| Check whether a privacy claim is credible | [Threat Models](threat-models/index.md) | The adversary, the protected asset, and what the PET does not protect |
| Find a useful research problem | [Fix My Itch](fix-my-itch/index.md) | A concrete problem, current workaround, success criteria, and a first contribution |
| Judge whether a deployment claim is meaningful | [Deployments](deployments/index.md) | Deployment maturity, source quality, lessons, and unresolved caveats |

## Opinionated Defaults

- Federated learning does not provide privacy by itself.
- Synthetic data is not automatically safe to release.
- TEEs reduce exposure but add hardware, attestation, and side-channel assumptions.
- Homomorphic encryption protects data during computation but is constrained by latency, operators, and model design.
- MPC can be powerful, but many teams underestimate protocol, identity, and operations work.
- Differential privacy is the clearest formal privacy tool, but the utility cost and budget accounting must be measured.

## Main Sections

- [Start Here](start-here/index.md): shared vocabulary and taxonomy.
- [PET Compass](pet-compass/index.md): decision support by data movement, threat model, and ML task.
- [PET Patterns](pet-patterns/index.md): reusable designs such as federated analytics, private inference, and private RAG.
- [Use Cases](use-cases/index.md): domain constraints in healthcare, finance, advertising, public sector, and AI.
- [Benchmarks](benchmarks/index.md): how to measure privacy, utility, cost, latency, scalability, and developer effort.
- [Contributing](contributing/index.md): quality bar for improving the guide.
