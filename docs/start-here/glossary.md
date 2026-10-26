---
description: "Definitions for PET decision reviews, including allowed output, leakage, private and confidential inference, differential privacy, HE, and MPC."
---

# Glossary

## Adversary

The party or coalition whose capabilities the system is designed to resist. Example: a curious coordinator in FL, a platform operator in confidential inference, or a malicious participant in MPC.

## Allowed output

The result the system is intentionally allowed to reveal, to specified recipients and at a specified frequency. It is a design permission, not proof that the result is harmless. Include intermediate recipients such as output reviewers and key holders.

## Attestation

Evidence that code is running in an expected trusted execution environment with expected configuration. Attestation is useful only if a relying party verifies it.

## Clean room

A governed collaboration environment that constrains data access, queries, and outputs. A clean room is not automatically a cryptographic guarantee.

## Collusion

Coordination between parties that are assumed to be separate in the privacy design. Many MPC and secure-aggregation claims depend on explicit collusion thresholds.

## Differential privacy budget

A way to account for cumulative privacy loss across differentially private releases. Budget choices are meaningful only with a defined privacy unit and release process.

## Encrypted inference

In this guide, inference that computes on cryptographically protected values, for example HE ciphertexts or MPC shares. State which values and parties are protected. A TEE executes on plaintext inside a trusted boundary; we call that confidential inference. Encryption in transit or at rest alone does not make inference encrypted in this sense.

## Honest-but-curious

An adversary model where parties follow the protocol but try to learn extra information from what they observe.

## Malicious adversary

An adversary that may deviate from the protocol, submit malformed inputs, poison updates, or manipulate outputs.

## Membership inference

An attack that tries to determine whether a record was part of a dataset or model training set.

## Non-IID data

Data that is not independently and identically distributed across participants. In FL, this often means different sites have different populations, labels, missingness, or measurement practices.

## Output leakage

Sensitive information revealed by the result of a computation, even if inputs were protected during computation.

## Privacy unit

The entity protected by a privacy claim, such as a person, device, record, account, hospital, or organization.

## Private set intersection

A protocol for learning set overlap while limiting exposure of nonmatching elements.

## Reconstruction attack

An attack that tries to infer sensitive records or attributes from outputs, gradients, embeddings, or statistics.

## Secure aggregation

A protocol that reveals an aggregate of updates while hiding individual updates, usually under threshold and dropout assumptions.

## Side channel

An indirect leakage path such as timing, memory access, power use, cache behavior, error patterns, or operational metadata.

## Synthetic data

Generated data intended to preserve useful structure from real data. It is not automatically anonymous.

## Threat model

A statement of who the adversary is, what they can do, what is protected, what output is allowed, and what assumptions the system relies on.

## Trust boundary

A point where control, visibility, or assumptions change. Examples: site to coordinator, client to model service, runtime to logs, or clean room to analyst.

## Zero-knowledge proof

A proof that a statement is true without revealing the private witness. ZKPs prove statements; they do not decide whether the statement is the right policy.

## Private inference

An umbrella goal: protect specified information during model inference from named parties. The term alone is not a guarantee. State whether the design uses [encrypted inference](#encrypted-inference), [confidential inference](#confidential-inference), or local execution, and identify output recipients.

## Confidential inference

Inference inside a trusted execution environment (TEE). Plaintext exists inside the protected runtime. The claim depends on the hardware, approved code, attestation verification, channel binding, and the selected side-channel threat model. See the [pattern](../pet-patterns/confidential-inference.md).

## Leakage

Information observable about protected data through outputs, intermediate values, logs, access patterns, sizes, timing, or other metadata. A leakage surface is the set of such observation points to review. Distinguish intentionally [allowed output](#allowed-output), leakage permitted by a protocol’s security model, and unintended implementation exposure.

## Differential privacy

A property of a randomized mechanism that bounds how its output distribution changes between neighboring datasets. Specify adjacency, the [privacy unit](#privacy-unit), epsilon, delta where applicable, and composition across releases. DP limits the additional disclosure attributable to that unit; it does not hide all population facts or secure the raw-data processor.

*(Evidence: Literature-backed. Source quality: Primary / official. [NIST SP 800-226](https://doi.org/10.6028/NIST.SP.800-226), 2025, explains the guarantee and implementation hazards.)*

## Homomorphic encryption

Encryption that supports specified computations on ciphertexts, yielding an encrypted result for an authorized key holder to decrypt. Security depends on the scheme, parameters, implementation, and key handling. Input confidentiality does not by itself prove correct computation or hide information revealed by the decrypted result.

*(Evidence: Literature-backed. Source quality: Primary / official. [Homomorphic Encryption Security Standard](https://homomorphicencryption.org/standard/), 2018, describes schemes, security properties, and parameter choices.)*

## MPC

Secure multiparty computation: parties jointly evaluate a function while protecting inputs according to a specified security model. State the allowed output, corrupted-party threshold, collusion assumptions, and whether security is semi-honest or malicious. Malicious security constrains protocol deviations; it does not establish that a party’s chosen input is truthful. Availability, fairness, and output delivery depend on the protocol.

See the [MPC analytics architecture](../pet-architectures/mpc-analytics-pipeline.md) for an editorial design example and its assumptions.
