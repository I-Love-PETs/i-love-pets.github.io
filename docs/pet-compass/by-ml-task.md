# By ML Task

## Cross-Silo Training

Start with cross-silo federated learning. Add secure aggregation if individual updates should be hidden from the coordinator. Add differential privacy if training participation or records require formal privacy protection.

## Personalization

Use federated learning when personalization data should remain local. Watch for fairness, drift, update leakage, and per-client overfitting.

## Private Inference

Use HE when plaintext inputs must be hidden from the model service and latency budgets can tolerate cryptographic cost. Use TEE-based confidential inference when performance and model flexibility matter.

## RAG

Use confidential RAG when retrieval context, embeddings, prompts, or generated answers cross trust boundaries. Consider TEEs, access controls, query logging, and output review.

## Fine-Tuning

Use private LLM fine-tuning patterns when training data is sensitive. Consider DP-SGD, secure aggregation, TEEs, redaction, and memorization auditing.

## Evaluation

Use privacy-aware evaluation when benchmark prompts, traces, labels, or user data are sensitive. Clean rooms, TEEs, or MPC may help, but output leakage remains central.
