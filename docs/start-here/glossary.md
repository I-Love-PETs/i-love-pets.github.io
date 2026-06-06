# Glossary

**Adversary:** The party or coalition whose capabilities the system is designed to resist. Example: a curious coordinator in FL, a platform operator in confidential inference, or a malicious participant in MPC.

**Allowed output:** The result the system is intentionally allowed to reveal. PETs often protect inputs while still revealing an output, so define this early.

**Attestation:** Evidence that code is running in an expected trusted execution environment with expected configuration. Attestation is useful only if a relying party verifies it.

**Clean room:** A governed collaboration environment that constrains data access, queries, and outputs. A clean room is not automatically a cryptographic guarantee.

**Collusion:** Coordination between parties that are assumed to be separate in the privacy design. Many MPC and secure-aggregation claims depend on explicit collusion thresholds.

**Differential privacy budget:** A way to account for cumulative privacy loss across differentially private releases. Budget choices are meaningful only with a defined privacy unit and release process.

**Encrypted inference:** Model inference where inputs, model weights, or intermediate values are protected from one or more parties. HE and TEEs are common approaches with different trust assumptions.

**Honest-but-curious:** An adversary model where parties follow the protocol but try to learn extra information from what they observe.

**Malicious adversary:** An adversary that may deviate from the protocol, submit malformed inputs, poison updates, or manipulate outputs.

**Membership inference:** An attack that tries to determine whether a record was part of a dataset or model training set.

**Non-IID data:** Data that is not independently and identically distributed across participants. In FL, this often means different sites have different populations, labels, missingness, or measurement practices.

**Output leakage:** Sensitive information revealed by the result of a computation, even if inputs were protected during computation.

**Privacy unit:** The entity protected by a privacy claim, such as a person, device, record, account, hospital, or organization.

**Private set intersection:** A protocol for learning set overlap while limiting exposure of nonmatching elements.

**Reconstruction attack:** An attack that tries to infer sensitive records or attributes from outputs, gradients, embeddings, or statistics.

**Secure aggregation:** A protocol that reveals an aggregate of updates while hiding individual updates, usually under threshold and dropout assumptions.

**Side channel:** An indirect leakage path such as timing, memory access, power use, cache behavior, error patterns, or operational metadata.

**Synthetic data:** Generated data intended to preserve useful structure from real data. It is not automatically anonymous.

**Threat model:** A statement of who the adversary is, what they can do, what is protected, what output is allowed, and what assumptions the system relies on.

**Trust boundary:** A point where control, visibility, or assumptions change. Examples: site to coordinator, client to model service, runtime to logs, or clean room to analyst.

**Zero-knowledge proof:** A proof that a statement is true without revealing the private witness. ZKPs prove statements; they do not decide whether the statement is the right policy.
