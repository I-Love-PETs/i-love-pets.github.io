# Private Inference

## Motivating Example

A fraud model provider wants banks to send transaction features for scoring without exposing plaintext inputs to the provider. The provider also wants to protect model IP and meet a strict latency target.

## Problem

Private inference protects sensitive inputs during prediction. The main design choice is usually between homomorphic encryption, TEEs, client-side inference, or standard hosted inference with governance. The right answer depends on model architecture, latency, trust assumptions, and what the output reveals.

## When To Use

- Client inputs are sensitive enough that the model service should not see them.
- The output is allowed to be returned to the client.
- The model can be adapted to the PET or the deployment accepts hardware trust.
- Latency, throughput, and cost have been benchmarked end to end.

## When Not To Use

- Do not use HE for arbitrary modern ML workloads without checking latency and operator support.
- Do not use TEEs without understanding attestation and side-channel assumptions.
- Do not use private inference if the prediction itself reveals the sensitive fact and no output policy exists.
- Do not ignore client-side inference when the model can run locally and IP risk is acceptable.

## Architecture

| Option | Flow | Best fit |
| --- | --- | --- |
| HE inference | Client encrypts input, service evaluates on ciphertext, client decrypts output | Narrow models, strict no-plaintext-input requirement |
| TEE inference | Client verifies attestation, sends plaintext into confidential runtime, runtime scores model | Broader models, lower latency, hardware trust acceptable |
| Client-side inference | Provider ships model or adapter to client environment | Small models, strong input privacy, manageable IP exposure |
| Governed hosted inference | Client sends plaintext under contract and controls | Lower-sensitivity inputs or high operational constraints |

## Threat Model

| Actor | Concern |
| --- | --- |
| Model provider | Should not see plaintext client inputs |
| Client | May try to extract model IP or learn sensitive model behavior |
| Cloud/platform operator | May inspect runtime, logs, or metadata |
| External attacker | May compromise API, keys, or logs |
| Output recipient | May misuse or overinterpret predictions |

## Privacy Properties

- HE can keep inputs encrypted during computation.
- TEEs can restrict plaintext exposure to an attested runtime.
- Client-side inference keeps inputs local but exposes more model material.
- Output controls can reduce leakage from returned predictions.

## What This Does Not Protect Against

- Leakage through outputs, explanations, confidence scores, or repeated queries.
- Poor client key handling.
- Model extraction by adversarial clients.
- TEE side channels or invalid attestation workflows.
- HE parameter mistakes or unsupported model operations.

## Tools And Building Blocks

- HE libraries and HE-friendly model conversion.
- Confidential-computing platforms and attestation clients.
- Model quantization, pruning, and operator audits.
- Key management and client SDKs.
- Rate limits, output shaping, and monitoring.

## Operational Complexity

Medium to high. HE is often harder to debug and optimize. TEEs are easier for model support but add attestation, runtime hardening, and hardware trust review.

## Cost Drivers

- HE ciphertext size, bootstrapping, batching, and operator depth.
- TEE instance pricing, enclave memory limits, and attestation integration.
- Model redesign and accuracy recovery.
- Client SDK support and key management.
- Monitoring for abuse and output leakage.

## Failure Modes

- HE latency makes the product unusable.
- A model layer is unsupported or approximated badly.
- Attestation is optional or ignored by clients.
- Logs capture plaintext inputs or outputs.
- Confidence scores allow repeated-query inference.
- The provider protects inputs but leaks sensitive predictions to the wrong user.

## Evaluation Checklist

- What exact input is protected from whom?
- Is the output allowed to reveal the prediction?
- Are model layers compatible with the PET?
- What is p50/p95/p99 latency including encryption and transfer?
- How are keys generated, stored, rotated, and revoked?
- Does the client verify attestation on every relevant deployment version?
- Are repeated queries and model extraction monitored?

## Open Research Problems

- HE model preflight analyzers.
- Debugging tools for encrypted computation.
- Benchmarks comparing HE, TEE, and client-side inference on the same workload.
- Output-leakage tests for private inference APIs.

## Related Pages

- [HE private inference API](../pet-architectures/he-private-inference-api.md)
- [Confidential inference](confidential-inference.md)
- [Private inference guidance](../pet-compass/by-ml-task.md#private-inference)
