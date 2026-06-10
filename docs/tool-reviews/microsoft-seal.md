# Microsoft SEAL

> Worked example applying the [tool evaluation framework](../contributing/tool-evaluation-framework.md) and [tool review template](../contributing/tool-template.md). Reviewed 2026-06-10. Not an endorsement.

## Evaluation Summary

| Field | Answer |
| --- | --- |
| What it helps build | An [HE private inference API](../pet-architectures/he-private-inference-api.md) or [private inference](../pet-patterns/private-inference.md): compute on encrypted inputs so the server never sees plaintext |
| PET family | HE (a lattice-based homomorphic encryption library; a primitive, not a turnkey service) |
| Best fit | Bounded-depth arithmetic on encrypted data — encrypted analytics or shallow private inference — where the operation circuit is known and shallow |
| Fit label | Narrow fit (powerful primitive, constrained workload) |
| Evidence level | Literature-backed (HE schemes are published and proven); Needs evidence for end-to-end latency/accuracy on any specific model |

## What It Helps Build

Microsoft SEAL is a C++ homomorphic encryption library (with a .NET wrapper) implementing the **BFV**, **BGV**, and **CKKS** schemes. BFV/BGV operate on exact integers/modular arithmetic; CKKS performs approximate arithmetic on real/complex numbers, which is what most encrypted-ML work uses. It lets a client encrypt data, send ciphertexts to a server, have the server compute *directly on the ciphertexts*, and return an encrypted result that only the client can decrypt ([Microsoft SEAL project](https://www.microsoft.com/en-us/research/project/microsoft-seal/)).

It is the cryptographic engine behind the [HE private inference API](../pet-architectures/he-private-inference-api.md) pattern and the [private inference](../pet-patterns/private-inference.md) pattern.

## Protected Assets

The protected asset is the **client's input** (and the **output**), which remain encrypted throughout the server-side computation. The server never holds the decryption key, so it never sees plaintext inputs or results. SEAL does **not** protect the **model weights** — in the standard setup the server computes with plaintext weights over encrypted inputs, so HE alone does not hide the model from the party running it, nor does it hide the *function* being computed.

## Threat Model Support

- **In scope**: an [honest-but-curious](../threat-models/honest-but-curious.md) server (or any party holding ciphertexts without the key) that wants to read the client's inputs/outputs. Security rests on the hardness of lattice problems (Ring-LWE); the schemes are published and analysed.
- **Partially in scope**: a [malicious](../threat-models/malicious-adversary.md) server that returns a *wrong* answer. HE protects confidentiality, not integrity/correctness of the computation — detecting a server that computes the wrong circuit needs additional verifiable-computation machinery SEAL does not provide.
- **Out of scope**: protecting the model owner from the client, hiding which function is computed, and parameter misuse. CKKS in particular has known **approximate-result leakage** subtleties (the noisy decryption can leak information about the secret if results are shared naively); using it safely requires care.
- **Implementation side channels**: as with any crypto library, timing/cache side channels in how you call it are your responsibility, not the scheme's.

## Best Fit

Use SEAL when:

- you have a **known, shallow arithmetic circuit** (sums, weighted sums, low-degree polynomials) to evaluate on encrypted data — encrypted aggregation/analytics or a deliberately shallow inference head;
- you need a mature, well-documented, permissively licensed HE primitive to build on;
- the client must hold the only key and the server must never see plaintext;
- you can pre-plan multiplicative depth and encryption parameters.

## When Not To Use

Avoid, or look elsewhere, when:

- you need **deep** neural-network inference on encrypted data. SEAL does **not** ship native bootstrapping, so the multiplicative depth you can evaluate is bounded by your parameter choice; deep circuits exhaust the noise budget. (Third-party projects add CKKS bootstrapping on top of SEAL, but that is not core SEAL — treat it as a separate dependency to evaluate.) For deep encrypted inference, evaluate libraries with built-in bootstrapping (e.g. OpenFHE) or a compiler such as Concrete ML as comparisons;
- you also need to hide the **model weights** from whoever runs inference — HE-over-plaintext-weights does not do that; consider a [TEE](confidential-computing-platform.md) or two-party MPC;
- you need integrity/verifiability of the result, not just confidentiality;
- you want a turnkey "private ML API" — SEAL is a low-level building block, not a service.

## Privacy Claims

SEAL's defensible claim is **confidential computation on encrypted data** under standard lattice assumptions: the server computes without ever decrypting. This is literature-backed at the *scheme* level. SEAL is careful **not** to claim it is a complete private-ML solution; turning the primitive into a safe end-to-end system (parameter selection, CKKS result-leakage handling, no bootstrapping) is the integrator's job.

## Benchmarks Or Evidence

- **Cryptographic evidence** (Literature-backed): BFV, BGV, and CKKS are published, peer-reviewed schemes; SEAL is a faithful, widely cited implementation, MIT-licensed and open source ([project page](https://www.microsoft.com/en-us/research/project/microsoft-seal/)).
- **Maintenance / version** (mostly verified): SEAL uses a versioned release model; as of this review the latest tagged releases are in the 4.3.x line (e.g. v4.3.0 with v4.3.1/v4.3.2 following), per the GitHub release feed ([release notes mirror](https://newreleases.io/project/github/microsoft/SEAL/release/v4.3.0)). The exact "newest patch" number drifts — treat the precise patch level as **Needs evidence** and check the [SEAL repository](https://github.com/microsoft/SEAL) at adoption time. Note also that newer versions are no longer published to NuGet.org; .NET users build their own package from source.
- **Bootstrapping** (verified, with caveat): core SEAL does **not** implement bootstrapping; bootstrapping for CKKS exists only via third-party extensions.
- **End-to-end performance** (Needs evidence): latency, ciphertext size, and accuracy loss for *your* circuit depend entirely on scheme, polynomial-modulus degree, coefficient-modulus chain, and batching. There is no single headline number; this must be measured.

## First Benchmark To Run

Per the framework's HE row: **end-to-end latency, ciphertext size, supported operators, and accuracy loss** for one concrete operation.

1. Pick one real operation (e.g. an encrypted dot-product / shallow linear layer over CKKS).
2. Choose `poly_modulus_degree` and the coefficient-modulus chain to fit the multiplicative depth you need; document the security level implied.
3. Measure: client encrypt time, ciphertext size on the wire, server compute time, decrypt time, and — for CKKS — the **accuracy loss** vs a plaintext baseline.
4. Push the circuit depth until the noise budget is exhausted to find your hard ceiling *without* bootstrapping. That ceiling is the central result of the review.
5. Confirm how you avoid CKKS approximate-result leakage before sharing any decrypted output.

## Operational Notes

- **Setup**: build from source (CMake), or use the .NET wrapper. CMake presets are provided for Windows/Linux/macOS, and there is iOS xcframework tooling in recent releases.
- **Keys**: the client owns the secret key; public/relinearization/Galois keys are generated and shipped to the server. Key and parameter management is a first-class operational concern.
- **Parameter selection is the hard part**: getting `poly_modulus_degree` and the modulus chain right for your depth *and* a sound security level is where most of the engineering effort goes.
- **No bootstrapping in core**: plan circuits to fit the noise budget, or take on a third-party bootstrapping dependency and re-audit it.
- **Upgrades**: pin the version; HE libraries evolve and parameter/API details change. The NuGet deprecation means .NET pipelines must build from source.

## Failure Modes

- Assuming HE hides the **model** — it protects inputs/outputs, not plaintext weights held by the server.
- Choosing parameters that look fast but provide an inadequate security level, or that silently lose CKKS precision.
- Sharing CKKS decrypted results without accounting for approximate-result leakage.
- Trying to run a deep network and discovering the noise budget is exhausted mid-circuit (no native bootstrapping).
- Treating confidentiality as integrity — HE does not detect a server that computes the wrong function.

## Review Verdict

**Watch / narrow-fit recommend.** Microsoft SEAL is a defensible, mature, MIT-licensed representative of the HE family and a sound choice for **bounded-depth** encrypted computation where only the client holds the key. It earns a conditional recommendation for shallow encrypted analytics or shallow private inference. For **deep** encrypted inference it is a poor fit on its own (no native bootstrapping) — evaluate OpenFHE or Concrete ML for that workload — and it never hides model weights, so pair it with a [TEE](confidential-computing-platform.md) or MPC if the model is also sensitive.

## Related Pages

- Pattern: [Private Inference](../pet-patterns/private-inference.md)
- Architecture: [HE Private Inference API](../pet-architectures/he-private-inference-api.md)
- Threat models: [Honest-But-Curious](../threat-models/honest-but-curious.md), [Side Channels](../threat-models/side-channels.md)
- Itch: [Homomorphic Encryption](../fix-my-itch/homomorphic-encryption.md)
