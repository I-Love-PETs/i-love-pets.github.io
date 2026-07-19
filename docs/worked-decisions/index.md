# Worked Decisions

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: Worked reasoning examples, not benchmarked deployments. Every illustrative figure is labeled with its evidence level and must be re-validated against your own workload before any production decision.

A shortlist tells you which PETs are plausible. It does not tell you how to *reason* from a messy real situation to a defensible architecture. These worked decisions do that. Each one walks a privacy or platform engineer from the data, parties, and constraints all the way to a concrete PET stack — and, just as importantly, shows the options that were **rejected and why**.

If the [PET Compass](../pet-compass/index.md) is the map and [Choose a PET](../pet-compass/choose-a-pet.md) is the legend, this section is a set of completed routes. Read one near your problem, then redo the reasoning with your own numbers.

## How To Read A Worked Decision

Every page follows the same seven-part structure. The order is deliberate: it forces reasoning *before* technology selection, and it refuses to stop at "we picked a PET."

| Section | What it answers | Why it is here |
| --- | --- | --- |
| 1. Decision context | What data, which parties, which constraints, what does success look like? | A PET choice is only valid relative to a concrete situation and a defined "good outcome." |
| 2. Candidate PETs | What is the realistic shortlist? | Narrows the field to options worth serious analysis. |
| 3. Rejected options | What did we *not* choose, and why? | The rejections carry most of the engineering judgment. A recommendation without rejections is marketing. |
| 4. Final recommendation | What is the concrete PET stack? | PETs compose; a single technology is rarely the whole answer. |
| 5. Threat model | Who is the adversary, where are the trust boundaries, what is **not** protected? | Names the residual risk explicitly so nobody mistakes the design for a guarantee. |
| 6. What to measure | How will we know privacy, utility, cost, latency, and complexity are acceptable? | Turns the recommendation into something falsifiable. |
| 7. What would change the decision | Which tripwires flip the recommendation? | A good decision states the conditions under which it becomes the wrong decision. |

!!! warning "Read the rejections"
    The most common failure mode in PET selection is adopting the most impressive-sounding technology and discovering the constraint it violates only in production. The "Rejected options" section exists to surface those constraints early. Do not skip it.

## Evidence Honesty

This site distinguishes how strongly a claim is supported. Worked decisions are, by nature, mostly reasoning rather than measurement, so most numbers here are **Expert judgment** or **Needs evidence**. We never relabel a guess as "Measured."

| Evidence level | Meaning in a worked decision |
| --- | --- |
| Measured | A number observed directly on the target workload. Rare in this section. |
| Deployment-backed | Supported by a real production deployment of a comparable system. |
| Literature-backed | Supported by published research or vendor benchmarks on a comparable task. |
| Expert judgment | A directional estimate from practitioner reasoning, dated and owned. |
| Needs evidence | A claim we believe matters but have not yet substantiated. Flagged on purpose. |

When you adapt one of these decisions, your first job is to upgrade the evidence level of the figures that actually drive your choice.

## The Six Worked Decisions

| Decision | Core tension | Where it usually lands |
| --- | --- | --- |
| [Hospital model training](hospital-model-training.md) | Train across hospitals that cannot pool patient records | Cross-silo federated learning + secure aggregation, DP only if patient-level participation must be bounded |
| [Cross-bank fraud detection](cross-bank-fraud-detection.md) | Banks want shared fraud signal without sharing customers or transactions | PSI for entity overlap + MPC on the joint computation, DP on any published metric |
| [Private RAG for enterprise docs](private-rag-enterprise-docs.md) | Answer questions over confidential documents without leaking them | Confidential RAG: access-controlled retrieval + TEE inference + output and log governance |
| [Synthetic dataset release](synthetic-dataset-release.md) | Publish a usable stand-in for a sensitive dataset | DP synthetic data with memorization tests, or query access if a release is not truly required |
| [Private model inference](private-model-inference.md) | Serve a model without seeing client inputs | TEE confidential inference for general models; HE only for narrow, latency-tolerant scoring |
| [Public-sector statistics release](public-sector-statistics-release.md) | Publish population statistics without re-identifying residents | Centralized DP with a documented privacy unit and budget, plus small-cell suppression |

## Choose The Closest Worked Decision

| If your case sounds like... | Start with... | Adjust first |
| --- | --- | --- |
| Several regulated organizations want a shared model | [Hospital model training](hospital-model-training.md) | Participant reliability, per-site utility, and poisoning risk |
| Multiple firms need a joint signal or overlap | [Cross-bank fraud detection](cross-bank-fraud-detection.md) | Entity resolution, allowed output, and adversarial incentives |
| Sensitive documents feed an assistant | [Private RAG for enterprise docs](private-rag-enterprise-docs.md) | Authorization, logging, and answer leakage |
| A dataset needs broad external use | [Synthetic dataset release](synthetic-dataset-release.md) | Whether users truly need row-shaped data |
| A service should not see inference inputs | [Private model inference](private-model-inference.md) | Latency, model operators, key ownership, and output leakage |
| A public body publishes statistics | [Public-sector statistics release](public-sector-statistics-release.md) | Legitimacy, accessibility, and small-cell policy |

## Before You Commit

Borrowing the project's standing rule: a worked decision is a starting point, not an architecture sign-off. Before you build, collect for *your* workload:

- A written threat model naming the adversary, the protected asset, collusion assumptions, and the allowed output. See [Threat Models](../threat-models/index.md).
- A workload benchmark for privacy, utility, latency, cost, and operational effort. See [Benchmark Scorecards](../benchmarks/scorecards.md).
- A reversal condition: the one metric or risk that would make you choose a different PET.

If you cannot fill those in, you do not yet have a decision — you have a preference.

## Related Guides

- [PET Compass](../pet-compass/index.md) for shortlisting before a worked decision.
- [PET Architectures](../pet-architectures/index.md) for turning the decision into data flows and trust boundaries.
- [Benchmarks](../benchmarks/index.md) for upgrading expert judgment into evidence.
