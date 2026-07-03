# Inference Attacks

Inference attacks use outputs, models, embeddings, statistics, or auxiliary data to learn sensitive facts.

## Examples

- Reconstruction attacks from gradients or statistics
- Attribute inference from released aggregates
- Embedding inversion from vector search systems
- Model extraction and prompt leakage

## Why PETs Still Need Output Review

Protecting inputs during computation does not guarantee that the released output is safe.

The output review should match the artifact. A trained model needs memorization
and membership tests. A statistics release needs small-cell and differencing
checks. A RAG answer needs authorization-aware retrieval tests and quote leakage
review. A synthetic dataset needs nearest-neighbor, rare-record, and downstream
misuse checks.

## PET Implications

Use DP, thresholds, output review, query limits, model auditing, and release documentation.

## Practical Tests

| Artifact | First tests |
| --- | --- |
| Aggregate statistics | Minimum cohort size, differencing across releases, attribute inference on small groups |
| Trained model | Membership inference, canary extraction, subgroup utility, overfitting gap |
| Embeddings or vector index | Nearest-neighbor exposure, embedding inversion probes, tenant isolation |
| Synthetic data | Record similarity, rare category preservation, memorization probes, downstream task drift |
| RAG answers | Permission bypass attempts, sensitive quote rate, prompt/log retention review |
