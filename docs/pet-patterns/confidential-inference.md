---
description: "Confidential Inference: protected assets, adversaries, allowed outputs, leakage, assumptions, non-goals, and checks for a concrete design review."
---

# Confidential Inference

## Decision framing

| Field | Scope |
| --- | --- |
| Protected asset | Inference inputs and model data inside the selected TEE. |
| Adversary | Infrastructure operators and other tenants outside the trusted runtime. |
| Allowed output | Predictions delivered to authorized clients; state whether the model service may also see them. See [allowed output](../start-here/glossary.md#allowed-output). |
| Leakage surface | Plaintext in the runtime, outputs, logs, request metadata, and hardware side channels. See [leakage](../start-here/glossary.md#leakage). |
| Assumptions | Clients verify attestation and bind the secure channel to approved code; hardware and runtime controls are trusted. |
| Non-goals | Hiding data from approved runtime code, eliminating all side channels, or preventing inference from predictions. |

--8<-- "decision-guidance.md"

## Problem

Sensitive inference needs general-purpose model execution with protection from infrastructure operators or other tenants.

## When To Use

Use TEEs when performance and model flexibility matter and hardware trust is acceptable.

## When Not To Use

Avoid this pattern when side-channel risk is unacceptable or when attestation cannot be made understandable to relying parties.

## Typical Architecture

Model code runs inside a TEE. Clients verify attestation, establish secure channels, send inputs, and receive outputs.

## Threat Model

Infrastructure operators are not fully trusted. Hardware vendors and enclave implementation become part of the trust base.

## Privacy Properties

Inputs and model data are protected in use, subject to hardware assumptions, enclave design, and side-channel controls.

## Does not protect

- Sensitive information intentionally revealed by predictions.
- Compromised clients or approved runtime code that exports plaintext.
- Side channels outside the selected hardware threat model.

## Tools And Building Blocks

TEEs, remote attestation, confidential containers, key release services, access controls, and audit logging.

<span id="common-failure-modes"></span>

## Failure modes

Attestation confusion, enclave misconfiguration, side channels, logging plaintext, and weak output controls.

## Open Research Problems

Attestation usability, multi-cloud portability, side-channel resilience, and composable guarantees with DP.

## Related Pages

- [Confidential RAG](../pet-architectures/confidential-rag.md)
- [TEE research problems](../fix-my-itch/tees.md)
- [Side channels](../threat-models/side-channels.md)
- [Deployments](../deployments/index.md)
