# Confidential Inference

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

## Tools And Building Blocks

TEEs, remote attestation, confidential containers, key release services, access controls, and audit logging.

## Common Failure Modes

Attestation confusion, enclave misconfiguration, side channels, logging plaintext, and weak output controls.

## Open Research Problems

Attestation usability, multi-cloud portability, side-channel resilience, and composable guarantees with DP.

## Related Pages

Confidential RAG, TEEs, side channels, deployments.
