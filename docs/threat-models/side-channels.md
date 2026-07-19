# Side Channels

Side channels leak information through indirect signals rather than intended data paths.

## Examples

- Timing differences
- Cache behavior
- Memory access patterns
- Error messages
- Query volume
- Output size
- Power or resource usage

## Practical Example

A TEE protects plaintext during inference, but timing behavior reveals which branch of a model or retrieval pipeline was used.

## PET Implications

TEEs, HE, MPC, and RAG systems need metadata and implementation review, not just high-level architecture diagrams.

## Design Review Prompts

| Signal | Example control |
| --- | --- |
| Timing | Batch, pad, or rate-limit requests when timing reveals private branches or cohort size. |
| Error messages | Return coarse errors and keep detailed diagnostics in access-controlled logs. |
| Output size | Normalize response shapes or document why variable output length is safe. |
| Query volume | Monitor repeated probing and apply per-user or per-partner budgets. |
| Resource usage | Review autoscaling, cache, and memory patterns for tenant or participant leakage. |
