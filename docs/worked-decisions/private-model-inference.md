# Worked Decision: Serving Inference Without Seeing Client Inputs

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Figures are illustrative and labeled. Validate latency, accuracy loss, operator support, and attestation on the real model before committing.

A provider wants to offer model inference as a service while *not* seeing the client's input — think a health-screening classifier, a fraud-scoring API, or a sensitive document classifier. The client's input is the protected asset. The naive framing is "use the most cryptographically pure option." The realistic framing weighs how broad the model is, how much latency the use case tolerates, and whether hardware trust is acceptable.

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | Client inputs at inference time (the sensitive asset) and the provider's model weights (often also sensitive/proprietary). |
| Parties | The client (input owner), the inference provider (model owner and operator), possibly the infrastructure host if separate from the provider. |
| Constraints | The provider must not learn the plaintext input — or at least not retain it. Latency and throughput targets exist (interactive vs. batch). The model may be large and use operators that some PETs do not support. Outputs are returned to the client and may themselves leak attributes. |
| What success looks like | Inputs are protected per the agreed claim (encrypted throughout, or never readable by the host), latency/throughput meet the use case, accuracy loss is acceptable, and outputs do not leak more than intended. |

!!! note "How broad is the model, and how fast must it be?"
    These two questions decide almost everything. A narrow model with relaxed latency opens the door to heavy cryptography; a large model with interactive latency usually forces a hardware-trust approach.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| TEE confidential inference | Run the model inside attested hardware so the host/operator cannot read inputs. Supports broad, large models at modest overhead. The pragmatic default for general workloads. See [Confidential Inference](../pet-patterns/confidential-inference.md). |
| Homomorphic encryption (HE) | Keeps the input encrypted *throughout* computation — the strongest "no plaintext ever" claim. Viable only for narrow models and latency-tolerant use. See [Private Inference](../pet-patterns/private-inference.md). |
| Model compression / quantization | Shrinks the model so heavier PETs (especially HE) become tractable and TEE memory fits. A supporting enabler. |
| Remote attestation + key management | Lets the client verify the runtime before sending input and control keys. Essential glue for the TEE path. |
| Output review / controls | Constrain returned outputs so they do not leak sensitive attributes beyond the intended prediction. |

## 3. Rejected Options

| Rejected option | Why rejected |
| --- | --- |
| **Plain hosted inference (send plaintext, trust the provider)** | Acceptable only if the input is not sensitive enough to justify PET overhead. Given the stated constraint that the provider must not see plaintext, this is rejected — though it is the right answer when inputs are low-sensitivity. |
| **HE as the default for a modern, broad model** | The canonical anti-pattern: choosing HE before checking architecture, operator support, batching, and latency. For large models with unsupported operators, HE latency and ciphertext size are prohibitive today. Rejected as a *default*; retained for the narrow-model case. |
| **MPC between client and provider for general inference** | Two-party MPC for inference exists but adds rounds of interaction and bandwidth that often blow interactive latency budgets, and it complicates the client. For general serving it loses to TEEs on operability. Rejected on latency/complexity for the general case. |
| **TEE treated as a magic secure box** | A TEE protects inputs from the host, but only if **attestation is verified** and side channels, supply chain, logs, and output leakage are addressed. Deploying a TEE and skipping attestation verification is rejected — it is the cost of a TEE with the assurance of plain hosting. |
| **Client-side inference (ship the model to the client)** | If the model could run locally, that would sidestep the whole problem — but it exposes proprietary weights and assumes capable client hardware. Rejected when the model is proprietary or too large for clients; noted as the right answer when it is not. |

## 4. Final Recommendation

Branch on model breadth and latency tolerance:

- **General / large model, interactive latency, hardware trust acceptable:** lead with **TEE confidential inference**. Make it real with **enforced remote attestation** (the client verifies the enclave *before* sending input), disciplined **key management**, **output controls**, and side-channel and log hardening. This is the pragmatic default. See [HE Private Inference API](../pet-architectures/he-private-inference-api.md) for the contrasting cryptographic design.
- **Narrow model (e.g., small classifier / scoring), latency-tolerant, "no plaintext ever" is a hard requirement:** consider **HE**, but only after confirming **operator support, batching strategy, ciphertext size, and end-to-end latency** on the actual model. Use **model compression/quantization** to make it tractable.
- **Model can run on the client and weights are not proprietary:** prefer **client-side inference** — the strongest privacy at the lowest serving cost.

!!! tip "Default to TEE for breadth, reach for HE only when the model is narrow"
    Most real model-serving workloads are too broad and too latency-sensitive for HE today. TEEs cover the general case at modest overhead *if* you actually verify attestation. Save HE for the narrow, latency-forgiving scoring problems where its guarantee is worth the cost.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | A curious provider/operator who wants to read client inputs; a curious infrastructure host; an external attacker; a client trying to extract the model via its outputs. |
| Trust boundaries | The client does not trust the provider with plaintext. With a TEE, trust is shifted to the hardware vendor and the attestation chain. With HE, no plaintext leaves the client at all (strongest boundary), at a latency cost. |
| What this design protects | TEE: the host/operator cannot read inputs *if attestation is verified and side channels are controlled*. HE: inputs remain encrypted throughout computation, so the provider never sees plaintext. Output controls limit what predictions reveal. |
| What is **not** protected | TEE security rests on the **hardware-trust and attestation assumptions** and is vulnerable to side channels and supply-chain compromise if unaddressed. HE protects the input but the **returned output** can still leak attributes, and HE does nothing about model-extraction via repeated queries. Neither protects against a client probing the model, nor against insecure **logging** of decrypted results. See [Side Channels](../threat-models/side-channels.md) and [Inference Attacks](../threat-models/inference-attacks.md). |

!!! warning "Attestation is the whole TEE claim"
    A TEE's privacy claim is exactly as strong as the attestation the client enforces. If the client sends input without verifying the enclave, the provider could be running anything. Enforce attestation in the request path or do not claim TEE protection.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Latency | End-to-end inference latency vs. the use case budget (interactive vs. batch) | Needs evidence — the deciding factor between TEE and HE |
| Accuracy | Accuracy loss vs. plaintext inference (quantization/compression effects; HE approximations) | Expert judgment (2026-06-10): TEE near-lossless; HE may force approximations — measure |
| Operator support (HE) | Fraction of model operators supported under HE; need for model surgery | Needs evidence — often the silent blocker for HE |
| Throughput / cost | Ciphertext size and cost per inference (HE); enclave overhead and cost (TEE) | Expert judgment (2026-06-10): HE cost per inference is far higher than TEE today |
| Attestation | Fraction of requests where attestation is verified before input is sent | Expert judgment (2026-06-10): must be 100% for the TEE claim to hold |
| Output leakage | Whether returned outputs leak attributes beyond the intended prediction | Needs evidence |
| Complexity | Key management, attestation operations, and integration burden | Expert judgment (2026-06-10): key/attestation ops dominate the TEE operational cost |

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| The model can run on the client and weights are not secret | Switch to **client-side inference** — best privacy, lowest serving cost. |
| Inputs turn out not to be very sensitive | Use **plain hosted inference**; do not pay PET overhead you do not need. |
| HE latency/operator support proves unworkable on the real model | Fall back to **TEE confidential inference** for the general case. |
| Hardware trust is unacceptable (no TEE allowed) | For narrow models, push on **HE**; otherwise reconsider whether the service can be offered privately at all, or move computation client-side. |
| Side-channel risk on the TEE is judged too high | Harden the enclave, restrict co-tenancy, or move to a cryptographic approach for the most sensitive paths. |
| Model-extraction via outputs becomes a concern | Add **output controls and query rate limits**; input confidentiality alone does not stop model theft. |

!!! note "The honest summary"
    TEEs give you broad, fast private inference *if* you verify attestation and address side channels. HE gives you a stronger no-plaintext guarantee but only pays off for narrow, latency-tolerant models. Neither protects the *output* — decide separately what the prediction itself is allowed to reveal.
