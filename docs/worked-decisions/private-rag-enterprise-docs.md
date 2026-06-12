# Worked Decision: RAG Over Confidential Enterprise Documents

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Figures are illustrative and labeled. Validate retrieval precision, authorization correctness, and leakage rates on your real corpus before rollout.

An enterprise wants employees to ask natural-language questions over a body of confidential documents — contracts, HR files, legal memos, security reviews — using retrieval-augmented generation. The instinct is to ask "how do we keep the model from seeing the data." That instinct is half wrong. In RAG, the model is rarely the biggest leak. The leaks are in *retrieval* (surfacing documents a user should not see), *prompts and logs* (sensitive text retained), and *answers* (the model quoting restricted content to the wrong person).

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | A heterogeneous corpus of confidential documents with **per-document access rules** that differ by user, team, and clearance. |
| Parties | Employees with differing authorization, the platform team operating the RAG system, a model provider (hosted or self-run), security and compliance owners. |
| Constraints | A user must never receive content they are not authorized to see — directly or via a synthesized answer. Prompts and retrieved context must not be retained insecurely. The runtime may need to run on infrastructure not fully trusted by the data owner. |
| What success looks like | Useful answers grounded in documents the asker is actually allowed to see, no authorization bypass via retrieval or generation, controlled prompt/log retention, and an attestation story someone actually verifies. |

!!! note "Hiding the runtime does not fix retrieval"
    Teams often encrypt or confine the inference runtime, then leak through an over-broad retriever or a verbose answer. The runtime is one boundary; retrieval scope, logging, and output policy are equally load-bearing.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| Confidential RAG with tight access control | Treats authorization-aware retrieval, runtime confidentiality, and output governance as one system. The natural fit. See [Federated RAG](../pet-patterns/federated-rag.md) for a related composition and [Confidential Inference](../pet-patterns/confidential-inference.md) for the runtime piece. |
| TEEs + remote attestation | Run retrieval and inference inside attested hardware so the operator/host cannot read prompts or context. Addresses "infrastructure is not fully trusted." |
| Redaction / query minimization | Strip or mask sensitive fields before they reach prompts or logs; minimize what each query carries. Reduces blast radius. |
| Output policy / answer review | Filter or constrain generated answers so they cannot quote restricted content to unauthorized users. Closes the generation-side leak. |
| Strict log controls | Bound retention of prompts, retrieved context, and answers; encrypt and access-restrict any retained logs. Often the most overlooked control. |

## 3. Rejected Options

| Rejected option | Why rejected |
| --- | --- |
| **Ordinary RAG with no access control** | Workable *only* if every user and system already shares one trust boundary and all documents are equally readable by all users. With per-document authorization, a flat retriever will surface restricted content the first time someone asks the right question. Rejected whenever authorization varies. |
| **Homomorphic encryption for the whole pipeline** | HE can keep narrow inference inputs encrypted, but a full RAG pipeline — embedding, vector search, multi-document context assembly, generation — is far outside what HE handles at acceptable latency today. Rejected on feasibility for the pipeline; HE remains conceivable only for an isolated narrow step. |
| **TEE as the entire answer** | A TEE protects prompts and context *from the host*, but it does nothing about an over-broad retriever returning documents the user should not see, or an answer that quotes restricted text. Treating the TEE as a magic secure box while ignoring retrieval scope, logs, and output is the classic anti-pattern. Rejected as a standalone solution; retained as one layer. |
| **DP on the documents or answers** | DP is built for aggregate release, not for serving exact passages to authorized readers. Adding DP noise to a contract lookup makes the answer wrong without fixing the actual exposure (who is allowed to see what). Wrong tool for this job. |
| **Encrypt-at-rest and call it private** | Encryption at rest protects against storage theft, not against an authorized-looking query retrieving content the user should not see. Necessary hygiene, insufficient as the privacy design. Rejected as the *answer* (kept as baseline hygiene). |

## 4. Final Recommendation

A layered confidential-RAG stack — the leak surface is the pipeline, so the controls span the pipeline:

1. **Authorization-aware retrieval.** Enforce per-document access control *at retrieval time*, scoped to the asking user's permissions. This is the single most important control: the retriever must never return what the user cannot read.
2. **TEE-backed runtime with remote attestation** for retrieval and inference, so the operator/host cannot read prompts or retrieved context. Crucially, *someone must actually verify the attestation* — unverified attestation is theater.
3. **Query minimization and redaction** so prompts and context carry only what is needed; mask fields that should never appear in a prompt or log.
4. **Output policy / answer governance** to prevent generated answers from quoting restricted content to unauthorized users, including cross-document inference.
5. **Strict log controls**: bound retention of prompts, context, and answers; encrypt and access-restrict anything kept; make the incident-response path explicit.

See [Confidential RAG](../pet-architectures/confidential-rag.md) for the reference architecture.

!!! tip "Authorization first, runtime second"
    If you have budget for exactly one control, make retrieval authorization-aware. A perfectly confidential runtime that retrieves the wrong documents is still a breach.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | A curious employee probing for documents above their clearance; a curious operator/host of the RAG infrastructure; an external attacker; an over-eager model that synthesizes restricted content. |
| Trust boundaries | The data owner may not trust the runtime host — hence TEEs and attestation. The asking user is authenticated but only partially trusted (authorization-limited). The model is treated as a component that can leak through its outputs. |
| What this design protects | Users receive only content their permissions allow (authorization-aware retrieval + output policy). The host cannot read prompts/context (TEE, if attestation is verified). Sensitive fields are minimized in prompts/logs. Retained logs are bounded and access-controlled. |
| What is **not** protected | If authorization metadata is wrong or stale, the retriever faithfully enforces the *wrong* policy — garbage in, leak out. The model can still **infer** restricted facts from authorized fragments; output policy mitigates but does not eliminate this. Attestation that nobody verifies protects nothing. Prompt-injection in documents can subvert the assistant. Side channels on the TEE are out of scope unless specifically addressed. See [Side Channels](../threat-models/side-channels.md) and [Inference Attacks](../threat-models/inference-attacks.md). |

!!! warning "Unverified attestation is not a control"
    The most common TEE failure in RAG is deploying attested hardware and never checking the attestation in the request path. If verification is not enforced before a prompt is processed, you have the cost of a TEE and the assurance of plain hosting.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Authorization correctness | Rate of retrievals/answers that surface content above the user's permission (target: zero, audited continuously) | Needs evidence — must be red-teamed |
| Retrieval quality | Retrieval precision/recall within the authorized scope | Expert judgment (2026-06-10): authorization filtering can hurt recall; measure the tradeoff |
| Answer leakage | Rate at which answers quote or reconstruct restricted content | Needs evidence |
| Attestation coverage | Fraction of requests where attestation is actually verified before processing | Expert judgment (2026-06-10): should be 100% or the TEE is decorative |
| Log/prompt retention | What is retained, for how long, and who can read it | Needs evidence — often worse than assumed |
| Latency / cost | End-to-end answer latency and per-query cost including TEE overhead | Expert judgment (2026-06-10): TEE overhead is usually modest vs. generation cost |
| Incident response | Time and path to detect and contain an authorization or leakage incident | Needs evidence |

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| Every user and system shares one trust boundary, all docs equally readable | Drop to **ordinary RAG with governance**; the confidential-RAG machinery is unnecessary overhead. |
| The host *is* fully trusted by the data owner | Drop the TEE requirement; keep authorization-aware retrieval, output policy, and log controls (still essential). |
| Only narrow, fixed lookups are needed (not open-ended Q&A) | Consider deterministic, access-controlled search instead of generative RAG — fewer leak surfaces. |
| Regulatory rules forbid any third-party model touching the data | Move to a **self-hosted model inside the TEE boundary**; revisit the provider trust assumption. |
| Prompt-injection from documents proves exploitable | Add input sanitization, tool/output sandboxing, and stricter answer governance before broadening access. |
| Authorization metadata is unreliable | Fix access-control data quality *first*; the best PET stack faithfully enforces whatever policy it is given, correct or not. |

!!! note "The honest summary"
    Private RAG is mostly an access-control and output-governance problem wearing a cryptography costume. TEEs and attestation harden the runtime, but the breaches come from over-broad retrieval, leaky logs, and over-helpful answers. Spend accordingly.
