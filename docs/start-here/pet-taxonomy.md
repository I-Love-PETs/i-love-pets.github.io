# PET Taxonomy

## Federated Learning

**What it is:** A way to train models across multiple data holders while raw training data stays local.

**What problem it solves:** It helps organizations collaborate on model training when centralizing raw data is infeasible or unacceptable.

**Strengths:** Reduces raw-data movement, fits cross-silo collaboration, and can pair with secure aggregation or differential privacy.

**Weaknesses:** Model updates can leak information, non-IID data can degrade quality, and coordination is operationally heavy.

**Common misconception:** Federated learning is not automatically private. It changes where data lives; it does not by itself guarantee that updates reveal nothing.

## Differential Privacy

**What it is:** A mathematical framework for limiting how much the output of a computation can depend on any one record or person.

**What problem it solves:** It gives a formal privacy guarantee for statistics, model training, synthetic data, and other outputs.

**Strengths:** Clear guarantee, composable accounting, and strong protection against many inference attacks when applied correctly.

**Weaknesses:** Utility can suffer, privacy accounting is hard to communicate, and bad parameter choices can make the guarantee weak.

**Common misconception:** Differential privacy is not just adding noise. The mechanism, sensitivity, accounting, and release process all matter.

## Secure Multiparty Computation

**What it is:** Protocols that let parties compute a function over private inputs without revealing those inputs to each other.

**What problem it solves:** It supports joint analytics, matching, scoring, and measurement across organizations that cannot share raw data.

**Strengths:** Strong cryptographic privacy for inputs and flexible computation for some workloads.

**Weaknesses:** Protocols can be expensive, integration can be difficult, and malicious-security variants often cost more.

**Common misconception:** MPC hides inputs, not necessarily outputs. A revealing output can still leak sensitive facts.

## Homomorphic Encryption

**What it is:** Encryption that supports computation over ciphertexts, producing encrypted results that can later be decrypted.

**What problem it solves:** It enables private inference or analytics when a service should compute without seeing plaintext inputs.

**Strengths:** Strong data confidentiality during computation and useful for narrow, high-value workloads.

**Weaknesses:** Expensive operations, model constraints, ciphertext expansion, and challenging engineering.

**Common misconception:** Fully homomorphic encryption does not make arbitrary production workloads cheap or simple.

## Trusted Execution Environments

**What it is:** Hardware-backed isolated execution environments that protect code and data while in use.

**What problem it solves:** TEEs let a party run sensitive computation on infrastructure that other parties may not fully trust.

**Strengths:** General-purpose computation, practical performance, and useful deployment patterns for confidential computing.

**Weaknesses:** Hardware trust, side channels, supply-chain concerns, and attestation usability.

**Common misconception:** A TEE is not a complete security boundary by itself. Code, configuration, inputs, outputs, and side channels still matter.

## Private Set Intersection

**What it is:** Protocols that reveal the overlap between sets without revealing nonmatching elements.

**What problem it solves:** PSI supports privacy-preserving matching for fraud, advertising, contact discovery, and research cohorts.

**Strengths:** Clear purpose, mature protocols, and strong fit for overlap questions.

**Weaknesses:** The intersection itself can be sensitive, and repeated queries can leak more than intended.

**Common misconception:** PSI does not mean "no data is revealed." The output is explicitly revealed to one or more parties.

## Synthetic Data

**What it is:** Generated data intended to preserve useful statistical structure from real data.

**What problem it solves:** It can support safer sharing, prototyping, testing, and education when raw data access is too risky.

**Strengths:** Easy to consume, useful for downstream workflows, and compatible with differential privacy when designed that way.

**Weaknesses:** Can memorize rare records, may miss important tails, and often lacks formal privacy guarantees.

**Common misconception:** Synthetic data is not automatically anonymous.

## Data Clean Rooms

**What it is:** Governed environments for controlled collaboration, measurement, and analysis over datasets.

**What problem it solves:** Clean rooms help organizations collaborate while constraining access, queries, outputs, and governance.

**Strengths:** Practical business fit, policy controls, auditing, and integration with existing data platforms.

**Weaknesses:** Query leakage, platform trust, policy bypasses, and limited formal guarantees unless combined with PETs.

**Common misconception:** A clean room is a governance architecture, not necessarily a cryptographic privacy guarantee.

## Zero-Knowledge Proofs

**What it is:** Proof systems where one party proves a statement is true without revealing the private witness.

**What problem it solves:** ZKPs support verifiable compliance, credentials, computation, and integrity claims without exposing underlying data.

**Strengths:** Strong verification properties and compelling fit for selective disclosure.

**Weaknesses:** Circuit design, proving cost, setup assumptions, and developer experience.

**Common misconception:** ZKPs prove statements; they do not decide whether the statement is the right privacy policy.
