# Federated RAG

## Motivating Example

A multinational company wants employees to ask questions across legal, finance, HR, and regional policy documents. Documents live in different business units and jurisdictions. No single team should receive all raw documents or all prompts.

## Problem

Federated RAG answers questions across distributed or separately controlled knowledge sources. Privacy risk appears in retrieval, embeddings, prompts, context windows, generated answers, logs, and citations. A protected model runtime is useful but not sufficient.

## When To Use

- Documents cannot be centralized or should remain under separate owners.
- Users need answers across multiple repositories.
- Retrieval policy can be enforced per document owner.
- The system can preserve provenance and deny unauthorized snippets.
- Logs and generated answers are covered by policy.

## When Not To Use

- Do not use federated RAG if ordinary access control and one repository solve the problem.
- Do not use it when document owners cannot agree on metadata, permissions, or retention.
- Do not claim privacy from decentralization alone.
- Do not add TEEs if the main failure is overbroad authorization.
- Do not expose citations that reveal restricted document existence to unauthorized users.

## Architecture

1. User submits a query with identity and purpose context.
2. Policy engine determines which repositories may be queried.
3. Each repository performs local retrieval or exposes a controlled retriever.
4. A coordinator or confidential runtime assembles approved snippets.
5. The model generates an answer with provenance and output policy checks.
6. Logs store only approved metadata with retention limits.

## Threat Model

| Actor | Concern |
| --- | --- |
| User | May query beyond authorization or infer restricted document existence |
| Retriever owner | May see sensitive prompts or cross-unit interest |
| Coordinator | May see snippets, prompts, and repository metadata |
| Model/runtime operator | May inspect prompts or context |
| Auditor/support staff | May see logs containing sensitive content |

## Privacy Properties

- Documents can remain with their owners.
- Retrieval can be scoped by identity, purpose, and policy.
- TEEs can reduce exposure of prompts and assembled context to the runtime operator.
- Redaction and output policy can reduce answer leakage.
- Provenance can make access decisions inspectable.

## What This Does Not Protect Against

- Incorrect permissions.
- Prompt injection inside retrieved documents.
- Answers that summarize restricted content for an unauthorized user.
- Logs that store sensitive prompts or snippets.
- Embeddings or metadata that reveal sensitive document content.
- Hallucinations or unsupported legal/medical advice.

## Tools And Building Blocks

- Policy engine and identity integration.
- Local retrievers or repository-scoped search.
- Confidential runtime for prompt/context assembly.
- Redaction and data-loss-prevention checks.
- Provenance, citation policy, and answer review.
- Prompt-injection and unauthorized-retrieval tests.

## Operational Complexity

High. The hardest work is usually not model serving; it is permission modeling, repository onboarding, metadata quality, prompt/log handling, and incident response when a document is exposed.

## Cost Drivers

- Number of repositories and permission models.
- Embedding refresh and index maintenance.
- Confidential runtime cost if TEEs are used.
- Policy review and audit logging.
- Human review for high-risk answers.

## Failure Modes

- Retrieval crosses a trust boundary the answer policy cannot fix.
- A user learns that a restricted document exists through a citation.
- Prompts and snippets are stored in plaintext logs.
- Prompt injection causes the model to ignore access policy.
- One repository returns broad snippets because local ranking is poor.
- Embeddings retain deleted or restricted content.

## Evaluation Checklist

- Are document owners and trust boundaries named?
- Can the system prove which policy allowed each snippet?
- Are denied retrievals tested?
- Do logs exclude prompts and snippets unless explicitly allowed?
- Are citations filtered for unauthorized users?
- Are prompt-injection tests included?
- Can users report and trace an unsafe answer?

## Open Research Problems

- PET benchmark suite for private RAG.
- Attested retrieval and context assembly that developers can verify.
- Tests for unauthorized snippet exposure.
- Composition guidance for access control, TEEs, redaction, and output review.

## Related Pages

- [Confidential RAG architecture](../pet-architectures/confidential-rag.md)
- [Private RAG benchmark problems](../fix-my-itch/benchmarks-needed.md)
- [By ML task](../pet-compass/by-ml-task.md#private-rag)
