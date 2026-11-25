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

!!! warning "Physical access can invalidate attestation assumptions"
    Research disclosed in 2025 showed why physical access belongs in the threat model. [WireTap](https://wiretap.fail/) reported attestation-key exposure on tested Intel server SGX systems. [Battering RAM](https://batteringram.eu/) reported SGX confidentiality and SEV-SNP launch-integrity failures. [TEE.fail](https://tee.fail/), published at IEEE S&P 2026, reported Intel SGX/TDX attestation-key exposure and application signing-key exposure in a tested SEV-SNP guest.

    Assess the specific hardware and deployment. Determine who can physically access the servers, what the vendor threat model covers, and whether the operator can enforce physical controls. If those assumptions do not hold, choose a design whose confidentiality does not depend on that hardware boundary.

*(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. These results concern tested configurations and specific physical-access assumptions.)*

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
