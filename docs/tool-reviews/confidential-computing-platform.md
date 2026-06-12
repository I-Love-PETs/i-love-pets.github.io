# AWS Nitro Enclaves

> Worked example applying the [tool evaluation framework](../contributing/tool-evaluation-framework.md) and [tool review template](../contributing/tool-template.md). Reviewed 2026-06-10. Not an endorsement.

## Evaluation Summary

| Field | Answer |
| --- | --- |
| What it helps build | [Confidential inference](../pet-patterns/confidential-inference.md) and [confidential RAG](../pet-architectures/confidential-rag.md): process sensitive data (or run a model) inside an isolated, attested enclave |
| PET family | TEE / confidential computing (a hardware-isolated execution environment with attestation) |
| Best fit | Processing decrypted sensitive data on the cloud while excluding the parent OS, the operator, and other tenants — gated by cryptographic attestation |
| Fit label | Strong fit (for operator/host exclusion); narrow on side-channel-hardened workloads |
| Evidence level | Deployment-backed (GA AWS service, KMS integration); Expert judgment / Needs evidence for side-channel resistance of *your* code |

## What It Helps Build

AWS Nitro Enclaves carve an **isolated, hardened virtual machine** out of an EC2 instance using the same Nitro Hypervisor that isolates instances. The enclave has **no persistent storage, no interactive (SSH) access, and no external networking** — it talks to its parent instance only over a local `vsock` channel. It can request a **signed attestation document** from the Nitro Hypervisor containing measurements (PCRs) of the enclave image, kernel, application, and parent IAM role/instance, and present that document to external services to prove what is running before it is trusted ([AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/), [cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html)).

This is the substrate for the [confidential inference](../pet-patterns/confidential-inference.md) pattern and the [confidential RAG](../pet-architectures/confidential-rag.md) architecture.

## Protected Assets

The protected assets are the **plaintext data and code inside the enclave** — and, critically, **secrets released only to a verified enclave**. The headline mechanism: a [TEE](../fix-my-itch/tees.md) lets you process data *in the clear* (unlike HE/MPC) while keeping it out of reach of the host OS and operator. Via KMS attestation, decryption keys can be made releasable **only** to an enclave whose measurements match a policy, so even the parent-instance administrator cannot decrypt the data themselves ([Using cryptographic attestation with AWS KMS](https://docs.aws.amazon.com/enclaves/latest/user/kms.html)).

## Threat Model Support

- **In scope (the core value)**: the **platform/operator and the parent instance's own OS**. AWS KMS will perform `Decrypt`/`GenerateDataKey`/`GenerateRandom` for an enclave only when the signed attestation document's PCRs match the `kms:RecipientAttestation:ImageSha384` / `kms:RecipientAttestation:PCR` condition keys in the key policy — and the result is returned encrypted to the enclave's public key, so the parent never sees plaintext ([KMS condition keys for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html)). The parent-instance admin is explicitly modelled as *not* trusted to perform crypto operations or change the key policy.
- **Cross-tenant CPU side channels (largely mitigated by design)**: AWS allocates dedicated cores and does **not** share L1/L2 cache or CPU threads (no SMT sharing) across instances, which rules out the class of CPU side channels predicated on shared cores ([AWS Nitro side-channel design](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-ec2-approach-to-preventing-side-channels.html)).
- **Application-level side channels (your responsibility)**: timing side channels in the code *running inside* the enclave remain a real threat; independent analysis stresses that enclave applications must process secrets in constant time ([Trail of Bits: Nitro Enclaves attack surface](https://blog.trailofbits.com/2024/09/24/notes-on-aws-nitro-enclaves-attack-surface/)).
- **Trust assumptions / out of scope**: you must **trust AWS and the Nitro Hypervisor** (the hypervisor is assumed correct and non-malicious) — this is a fundamentally different trust model from HE/MPC, where no platform need be trusted. The enclave is a single trust zone: compromise of any component (e.g. via a supply-chain attack on what you put in the image) is total compromise. Attacks come from the parent instance and from any traffic the parent forwards.

## Best Fit

Use Nitro Enclaves when:

- you must process **decrypted** sensitive data or run a model in the cloud while excluding the host OS, the operator, and co-tenants;
- you can accept **trusting AWS/Nitro** as part of your model;
- you want keys/secrets released **only** to attested, measured code (KMS integration);
- your workload tolerates the constraints: no inbound network, no persistent disk, communication only via `vsock`.

## When Not To Use

Avoid, or reconsider, when:

- your threat model **cannot trust the cloud platform/hardware vendor**. If "no trusted third party" is a hard requirement, use [HE](microsoft-seal.md) or [MPC](../pet-architectures/mpc-analytics-pipeline.md) instead;
- you need protection against **application-level timing side channels** but cannot invest in constant-time code — the platform will not save you here;
- you require a guarantee that is **provable from cryptographic assumptions** rather than from trusting a vendor's hardware and attestation;
- your architecture needs the enclave to have direct network or persistent storage (it has neither by design; everything is proxied through the parent over `vsock`).

## Privacy Claims

The defensible claim is **hardware-isolated, attested execution that excludes the host and operator**, with secret release gated by measured code. This is Deployment-backed: Nitro Enclaves is a generally available AWS service with documented, built-in KMS attestation. The claim is explicitly **conditional on trusting AWS/Nitro** and on the integrator writing side-channel-aware code and managing attestation correctly — AWS does not claim the enclave protects you from your own non-constant-time code or from a compromised enclave image.

## Benchmarks Or Evidence

- **Platform maturity** (Deployment-backed): GA AWS service; first-party KMS attestation with documented PCR-based condition keys and a documented end-to-end attestation+decryption workflow ([enclave workflow](https://docs.aws.amazon.com/enclaves/latest/user/flow.html)).
- **Side-channel posture** (mixed; Literature/Expert): cross-tenant CPU side channels are addressed by AWS's dedicated-core/no-SMT-sharing design (vendor whitepaper); application-level side channels remain the developer's job per independent review (Trail of Bits, 2024).
- **Independent evaluation** (Literature-backed for attack surface): Trail of Bits has published a detailed attack-surface analysis (vsock handling, randomness/entropy, time sources, attestation best practices) — useful, named, third-party scrutiny rather than vendor-only documentation.
- **Workload performance** (Needs evidence): enclave provisioning time, `vsock` throughput, and the overhead for *your* model/data are not published constants and must be measured.

## First Benchmark To Run

Per the framework's TEE row: **attestation verification, log review, side-channel assumptions, and failure behavior.**

1. Build a minimal enclave image; record the PCR0/PCR1/PCR2 measurements emitted by `nitro-cli build-enclave`.
2. Write a KMS key policy gated on those PCRs (plus PCR3/PCR8 for IAM-role/signing-cert binding) and confirm `kms-decrypt` **succeeds inside the attested enclave and fails from the parent instance**. That asymmetry is the core security property — prove it, do not assume it.
3. Review what the parent instance and enclave **log**; confirm no plaintext or secret leaks through logs/support paths into the untrusted parent.
4. Validate failure behaviour: what happens on attestation mismatch, on a debug-mode enclave (PCRs become all-zero — confirm your policy rejects it), and on `vsock` errors.
5. State your side-channel assumption explicitly and, for any secret-dependent branch, confirm constant-time handling.

## Operational Notes

- **Setup**: enable enclave support on the EC2 instance; package the app as an enclave image file (`.eif`) via the Nitro CLI; boot it from the parent. No SSH into the enclave by design.
- **Keys / attestation**: secret release is wired through KMS condition keys on PCRs; the parent admin should have neither crypto permissions on the key nor the ability to edit the key policy. Sign your `.eif` (PCR8) for flexible, image-bound policies.
- **Networking / storage**: none directly — everything is proxied over `vsock` through the parent. Architect data in/out accordingly.
- **Randomness / time**: verify the enclave uses the Nitro hardware RNG and a sound time source (both called out as pitfalls by independent analysis).
- **Upgrades**: changing the enclave image changes its PCRs, which **breaks PCR-pinned KMS policies** — plan a rollout that updates measurements and policies together (PCR3/PCR8 give you flexibility here).
- **Debugging**: `--debug-mode` zeroes the PCRs, so debug builds must never satisfy a production key policy.

## Failure Modes

- Believing a TEE removes all trust assumptions — it **moves** trust to AWS/Nitro rather than eliminating it.
- Assuming the platform handles application-level timing side channels; it does not.
- Shipping a debug-mode enclave (all-zero PCRs) against a production policy.
- Leaking plaintext or secrets through the parent instance's logs or the `vsock` boundary.
- Forgetting that a new enclave image's changed PCRs will silently break attestation-gated key access on the next deploy.

## Review Verdict

**Recommend (with the trust caveat stated loudly).** AWS Nitro Enclaves is a defensible, GA, well-documented representative of the confidential-computing family, with genuine first-party attestation and KMS integration and credible independent scrutiny. It is a strong fit for excluding the host OS, operator, and co-tenants from plaintext processing — *provided you accept trusting AWS/Nitro and write side-channel-aware code.* It is the wrong tool when your requirement is "trust no platform" (use HE/MPC) or when application-level side channels dominate your threat model. Recommend for the confidential-inference / confidential-RAG patterns; watch the side-channel and attestation-lifecycle details.

## Related Pages

- Pattern: [Confidential Inference](../pet-patterns/confidential-inference.md)
- Architecture: [Confidential RAG](../pet-architectures/confidential-rag.md)
- Threat model: [Side Channels](../threat-models/side-channels.md)
- Itch: [TEEs](../fix-my-itch/tees.md)
