# Federated RAG

## Problem

Users need retrieval-augmented generation across sensitive corpora that cannot be copied into one central index.

## When To Use

Use it when retrieval must respect data ownership, residency, or access boundaries.

## When Not To Use

Avoid it when source systems cannot enforce access control or when generated answers could expose unauthorized context.

## Typical Architecture

Each data holder maintains local retrieval. A broker routes queries, combines authorized evidence, and sends constrained context to a model.

## Threat Model

The broker, model provider, retrievers, and users may each learn too much from queries, embeddings, context, or outputs.

## Privacy Properties

Data remains with holders, but prompts, embeddings, retrieved snippets, and generated answers require explicit controls.

## Tools And Building Blocks

Access control, confidential computing, query minimization, audit logs, redaction, secure retrieval, and output filters.

## Common Failure Modes

Prompt leakage, cross-tenant retrieval, embedding inversion, unauthorized citations, and poor provenance.

## Open Research Problems

Private RAG evaluation, leakage-resistant retrieval, policy-aware generation, and usability for evidence provenance.

## Related Pages

Confidential RAG, private LLM fine-tuning, AI use cases.
