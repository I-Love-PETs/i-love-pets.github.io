# Private Inference

## Problem

A client wants predictions from a model without exposing sensitive inputs to the model service.

## When To Use

Use private inference when input confidentiality is central and latency budgets can absorb cryptographic overhead.

## When Not To Use

Avoid it for large modern models unless model compression, batching, or hybrid designs make cost acceptable.

## Typical Architecture

The client encrypts inputs, the service evaluates a constrained model over ciphertexts, and the client decrypts the result.

## Threat Model

The service is honest-but-curious and should not see plaintext inputs. Output leakage and model extraction may still matter.

## Privacy Properties

HE can protect inputs during computation. It does not protect against revealing outputs or all metadata.

## Tools And Building Blocks

Homomorphic encryption libraries, quantization, polynomial approximations, batching, and model simplification.

## Common Failure Modes

Unacceptable latency, unsupported model operations, ciphertext expansion, weak key handling, and unmodeled output leakage.

## Open Research Problems

Cost reduction, programming abstractions, private inference for modern architectures, and privacy-aware model design.

## Related Pages

HE private inference API, confidential inference, cost benchmarks.
