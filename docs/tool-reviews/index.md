# Tool Reviews

These pages are **worked examples** of the project's [tool evaluation framework](../contributing/tool-evaluation-framework.md). They are not an awesome list and not endorsements. Each one applies the [tool review template](../contributing/tool-template.md) to a single, defensible representative tool from one PET family, so you can see how the framework turns "this tool exists" into "this tool fits (or does not fit) a concrete architecture, threat model, and benchmark."

## How to read these

Every review answers the same six questions the framework asks:

- **What does this help build?** A pattern or architecture, not a vague PET category.
- **What protected asset does it cover?** Inputs, updates, prompts, embeddings, outputs, logs, or weights.
- **What adversary is in scope?** Honest-but-curious, malicious, colluding, platform, inference, or side-channel.
- **What evidence supports the claim?** Documentation, a proof, a benchmark, a deployment, or an audit.
- **What breaks in production?** Setup, keys, logs, latency, upgrades, debugging.
- **What benchmark should be run first?** A review should produce a first measurement, not a vibe.

Each review ends with a fit label (strong / promising / narrow / poor / unknown), an evidence level, a first benchmark to run, operational risks, when *not* to use the tool, and a verdict (recommend / watch / reject for the stated use case).

## Evidence levels

Reviews are dated and labelled with the strongest evidence the reviewer could stand behind:

| Level | Meaning |
| --- | --- |
| Deployment-backed | Named, maturity-labelled production deployments support the claim. |
| Literature-backed | A specification, security proof, or peer-reviewed paper supports the claim. |
| Expert judgment | A reasoned conclusion drawn from documentation and design, without independent measurement. |
| Needs evidence | The claim is plausible but unverified here; treat numbers as uncertain. |

Versions, performance numbers, and "latest release" facts drift. Where a fact could not be confirmed as of the review date, it is labelled **Needs evidence** rather than guessed.

## The sample reviews

One representative per PET family:

| PET family | Tool | Review | Pair with |
| --- | --- | --- | --- |
| Federated learning (FL) | Flower (`flwr`) | [flower-fl.md](flower-fl.md) | [FL + secure aggregation](../pet-architectures/fl-secure-aggregation.md) |
| Differential privacy (DP) | OpenDP | [opendp.md](opendp.md) | [FL + differential privacy](../pet-architectures/fl-differential-privacy.md) |
| Homomorphic encryption (HE) | Microsoft SEAL | [microsoft-seal.md](microsoft-seal.md) | [HE private inference API](../pet-architectures/he-private-inference-api.md) |
| Confidential computing (TEE) | AWS Nitro Enclaves | [confidential-computing-platform.md](confidential-computing-platform.md) | [Confidential RAG](../pet-architectures/confidential-rag.md) |

## Contributing a review

Want to add one? Read the [tool evaluation framework](../contributing/tool-evaluation-framework.md) first to confirm the tool earns a page (it must help a reader decide on a concrete architecture, threat model, or benchmark), then copy the [tool review template](../contributing/tool-template.md) and fill in every field. A review that lists features without saying when *not* to use the tool is not finished.

## See Also

- [Tool evaluation framework](../contributing/tool-evaluation-framework.md) for the review rubric.
- [Benchmark scorecards](../benchmarks/scorecards.md) for the first measurement after a review.
- [Claim register](../project-standards/claim-register.md) for claims that need stronger evidence.
