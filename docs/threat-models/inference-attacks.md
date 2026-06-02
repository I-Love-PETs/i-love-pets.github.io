# Inference Attacks

Inference attacks use outputs, models, embeddings, statistics, or auxiliary data to learn sensitive facts.

## Examples

- Reconstruction attacks from gradients or statistics
- Attribute inference from released aggregates
- Embedding inversion from vector search systems
- Model extraction and prompt leakage

## Why PETs Still Need Output Review

Protecting inputs during computation does not guarantee that the released output is safe.

## PET Implications

Use DP, thresholds, output review, query limits, model auditing, and release documentation.
