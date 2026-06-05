# AI

AI systems introduce privacy risk through training examples, prompts, embeddings, retrieved context, evaluation data, model outputs, logs, and model weights.

## Scenario Playbook

| Scenario | Primary PET | Supporting PETs | Why | What can go wrong | What to measure |
| --- | --- | --- | --- | --- | --- |
| Enterprise private RAG over sensitive documents | Confidential RAG | TEEs, access control, redaction, log controls | Prompts and retrieved context cross trust boundaries | Bad permissions leak documents, logs store snippets, answers reveal restricted facts | Unauthorized retrieval rate, prompt/log retention, answer leakage |
| Private inference for model API users | TEE confidential inference or HE | Attestation, model compression, output controls | Inputs should not be exposed to the provider | HE latency explodes, attestation is ignored, outputs leak | p95 latency, supported operators, attestation coverage |
| Fine-tuning on sensitive examples | DP fine-tuning, FL, or TEE training | Redaction, secure aggregation, memorization tests | Model needs private domain behavior | Model memorizes examples, DP utility collapses, checkpoints leak | Extraction tests, privacy budget, utility, artifact access |
| Privacy-preserving model evaluation | Clean room or TEE | DP metrics, output review | Evaluation labels or prompts are sensitive | Metrics reveal test data, logs leak prompts | Metric sensitivity, benchmark contamination, access control |

## Use This When

- The sensitive artifact is named: prompts, documents, embeddings, labels, examples, logs, weights, or outputs.
- The model behavior can be evaluated for leakage.
- Access control and output policy are part of the design.
- Latency and utility have been benchmarked under the PET constraints.

## Avoid This When

- A PET protects runtime computation but permissions are wrong.
- The team has no plan to test memorization or extraction.
- Logs and experiment trackers are outside the privacy boundary.
- The output will reveal the sensitive fact anyway.
- A cheaper pattern such as RAG or prompting avoids fine-tuning sensitive data.

## Recommended Starting Stack

For private RAG, start with **access control + retrieval policy + log minimization**; add **TEEs** when runtime exposure crosses a trust boundary.

For private inference, start with **TEE confidential inference** when hardware trust is acceptable and model support matters. Use **HE** only after operator and latency benchmarking.

## Failure Modes

- Retrieved context violates document permissions.
- Prompt injection causes policy bypass.
- Fine-tuned models emit training examples.
- Embeddings or logs retain deleted content.
- Evaluation metrics expose sensitive labels or prompts.
- Users overtrust "private AI" claims without a threat model.

## Evaluation Checklist

- Which AI artifact is protected?
- Who can see prompts, retrieved context, logs, and outputs?
- Are memorization, extraction, and membership inference tested?
- Can users verify attestation if TEEs are used?
- Do outputs include provenance and policy checks?
- Is the model release path controlled?

## Related Pages

- [Federated RAG](../pet-patterns/federated-rag.md)
- [Private inference](../pet-patterns/private-inference.md)
- [Private LLM fine-tuning](../pet-patterns/private-llm-finetuning.md)
