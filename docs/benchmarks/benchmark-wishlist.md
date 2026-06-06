# Benchmark Wishlist

These are benchmark projects that would materially improve PET decision support. Each should produce reproducible code, documented assumptions, and negative results.

## Private RAG Evaluation

Measure leakage from prompts, embeddings, retrieval context, generated answers, logs, and provenance.

A useful first benchmark: a role-based document corpus with expected-deny cases and prompt-injection fixtures.

## Federated Learning Under Realistic Non-IID Data

Benchmark utility, privacy, communication, and robustness across skewed silos.

A useful first benchmark: one dataset split into site-like partitions with label skew, feature missingness, dropouts, and poisoning tests.

## DP Accounting Usability

Compare whether engineers, reviewers, and product teams correctly understand privacy-budget reports.

A useful first benchmark: give reviewers three DP release reports and measure whether they identify the privacy unit, budget, and composition risk.

## HE Private Inference Cost

Publish task-level latency, throughput, cost, and model-operation compatibility for modern inference workloads.

A useful first benchmark: compare plaintext, TEE, and HE inference on the same small tabular model.

## MPC Developer Effort

Track schema work, implementation time, debugging, protocol selection, and operational incidents.

A useful first benchmark: implement private sum, private join, and private threshold count with a setup diary.

## Synthetic Data Memorization

Standardize tests for rare-record reproduction, nearest-neighbor leakage, and membership inference.

A useful first benchmark: inject rare records into a dataset, generate synthetic releases, and compare attack success across generators.
