# Start Here

Privacy-enhancing technologies are not interchangeable. They protect different parts of a system, assume different adversaries, and create different tradeoffs.

Use this section to build a working vocabulary before choosing a PET.

## The Short Version

| PET | Best fit | Watch out for | Go deeper |
| --- | --- | --- | --- |
| Federated learning | Training across data silos without centralizing raw data | Gradients and model updates can still leak information | [Cross-silo FL](../pet-patterns/cross-silo-federated-learning.md) |
| Differential privacy | Limiting what can be learned about one person or record from an output | Utility loss and accounting complexity | [DP taxonomy](pet-taxonomy.md#differential-privacy) |
| Secure multiparty computation | Joint computation across parties that do not reveal inputs | Cost, coordination, and protocol complexity | [MPC analytics](../pet-architectures/mpc-analytics-pipeline.md) |
| Homomorphic encryption | Computing on encrypted data | High cost and narrow workload fit | [Private inference](../pet-patterns/private-inference.md) |
| Trusted execution environments | Isolating computation in hardware-protected runtimes | Hardware trust, side channels, and attestation usability | [Confidential RAG](../pet-architectures/confidential-rag.md) |
| Private set intersection | Finding overlap between datasets without exposing nonmatches | Output leakage and repeated-query risk | [PSI pattern](../pet-patterns/private-set-intersection.md) |
| Synthetic data | Sharing generated data instead of raw data | Memorization, weak privacy claims, and utility drift | [Synthetic release pipeline](../pet-architectures/synthetic-data-release-pipeline.md) |
| Data clean rooms | Controlled collaboration over governed datasets | Governance does not automatically equal cryptographic privacy | [Deployments](../deployments/index.md) |
| Zero-knowledge proofs | Proving a statement without revealing the witness | Circuit cost and proving-system expertise | [Glossary](glossary.md) |

## How To Read This Guide

Start with the problem, not the PET. Ask:

- Who owns the data?
- What output is needed?
- Who must not learn what?
- What adversary is in scope?
- What latency, cost, and accuracy constraints are acceptable?

Then use [PET Compass](../pet-compass/index.md) to choose candidates and [PET Patterns](../pet-patterns/index.md) to design a system.

## Common Wrong Assumptions

| Assumption | Better framing |
| --- | --- |
| "Data stayed local, so it is private." | Updates, metrics, models, logs, and outputs can still leak. |
| "Synthetic data is anonymous." | Synthetic data can memorize or reproduce rare records unless tested and governed. |
| "A TEE means the whole system is confidential." | Attestation, side channels, logs, code, and outputs still matter. |
| "HE is the strongest choice, so use it." | HE is useful only when the workload fits its operator, latency, and cost constraints. |
| "DP is just adding noise." | DP requires a privacy unit, sensitivity, mechanism, accounting, and release policy. |
| "A clean room is a PET guarantee." | Clean rooms are governed workflows; privacy depends on controls and outputs. |

## First Decision Path

| If your problem is... | Start with... |
| --- | --- |
| Choosing a PET | [Choose a PET](../pet-compass/choose-a-pet.md) |
| Explaining terms | [Glossary](glossary.md) |
| Comparing PET families | [PET taxonomy](pet-taxonomy.md) |
| Designing a system | [PET architectures](../pet-architectures/index.md) |
| Finding failure modes | [Threat models](../threat-models/index.md) |
| Measuring a candidate | [Benchmarks](../benchmarks/index.md) |
