# What Are PETs?

Privacy-enhancing technologies are techniques that reduce privacy risk while still allowing useful computation, measurement, learning, or verification.

They usually change one of four things:

- Where data moves
- What a party can observe
- What outputs reveal
- Which trust assumptions are required

## What PETs Are Good For

PETs are useful when the desired outcome is legitimate but the raw data is too sensitive, regulated, commercially valuable, or risky to centralize.

Common goals include:

- Collaborative analytics
- Cross-institution model training
- Privacy-preserving measurement
- Secure data matching
- Encrypted inference
- Safer data release
- Compliance-supporting data minimization

## What PETs Do Not Magically Solve

PETs do not remove the need for product judgment, security engineering, legal review, access controls, or incident response.

A PET can reduce one class of risk while leaving another untouched. For example, federated learning can reduce raw-data movement but still expose sensitive information through model updates. A trusted execution environment can protect data during computation but still depends on hardware trust and careful enclave design.

## A Useful Mental Model

Every PET claim should complete this sentence:

> This system protects `<data or behavior>` from `<adversary>` under `<assumptions>`, while revealing `<allowed output>`.

If a claim cannot say that clearly, it is probably marketing rather than engineering.
