# PET Patterns

Patterns are reusable designs, not recipes. Each one states when to use it, when not to use it, what can still go wrong, and which research problems remain open.

## Pattern Selection

| Problem | Pattern | Closest architecture | Related research |
| --- | --- | --- | --- |
| Aggregate measurement without centralizing raw data | [Federated analytics](federated-analytics.md) | [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md) | [Benchmarks needed](../fix-my-itch/benchmarks-needed.md) |
| Cross-organization model training | [Cross-silo federated learning](cross-silo-federated-learning.md) | [FL + secure aggregation](../pet-architectures/fl-secure-aggregation.md) | [FL research problems](../fix-my-itch/federated-learning.md) |
| Safer data-like release | [DP synthetic data release](dp-synthetic-data-release.md) | [Synthetic data release pipeline](../pet-architectures/synthetic-data-release-pipeline.md) | [Synthetic data research](../fix-my-itch/synthetic-data.md) |
| Dataset overlap | [Private set intersection](private-set-intersection.md) | [MPC analytics pipeline](../pet-architectures/mpc-analytics-pipeline.md) | [MPC research](../fix-my-itch/mpc.md) |
| Model inference over protected inputs | [Private inference](private-inference.md) | [HE private inference API](../pet-architectures/he-private-inference-api.md) | [HE research](../fix-my-itch/homomorphic-encryption.md) |
| General-purpose protected inference | [Confidential inference](confidential-inference.md) | [Confidential RAG](../pet-architectures/confidential-rag.md) | [TEE research](../fix-my-itch/tees.md) |
| Retrieval across sensitive corpora | [Federated RAG](federated-rag.md) | [Confidential RAG](../pet-architectures/confidential-rag.md) | [PET composition](../fix-my-itch/pet-composition.md) |
| Fine-tuning on sensitive data | [Private LLM fine-tuning](private-llm-finetuning.md) | [FL + differential privacy](../pet-architectures/fl-differential-privacy.md) | [DP research](../fix-my-itch/differential-privacy.md) |

## Use A Pattern When

- the use case is clear enough to name the allowed output;
- the trust boundary is still being shaped;
- you need a reusable design vocabulary before drawing a concrete architecture.

Move to [PET Architectures](../pet-architectures/index.md) when you need actors,
logs, keys, deployment notes, and evaluation checks.
