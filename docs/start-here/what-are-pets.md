# What Are PETs?

Privacy-enhancing technologies are techniques that reduce privacy risk while still allowing useful computation, measurement, learning, sharing, or verification.

They usually change one of four things:

- where data moves;
- what a party can observe;
- what outputs reveal;
- which trust assumptions are required.

## What PETs Are Good For

PETs are useful when the desired outcome is legitimate but the raw data is too sensitive, regulated, commercially valuable, or risky to centralize.

Common goals include:

- collaborative analytics;
- cross-institution model training;
- privacy-preserving measurement;
- secure data matching;
- encrypted inference;
- safer data release;
- compliance-supporting data minimization.

## What PETs Do Not Magically Solve

PETs do not remove the need for product judgment, security engineering, legal review, access controls, or incident response.

A PET can reduce one class of risk while leaving another untouched:

| PET claim | Remaining issue |
| --- | --- |
| Federated learning keeps raw data local | Model updates and final models can still leak |
| Differential privacy bounds individual contribution | Utility, budget choice, and release accounting still matter |
| HE protects inputs during computation | Outputs, metadata, and model fit still matter |
| TEEs protect runtime plaintext | Hardware trust, side channels, logs, and attestation still matter |
| PSI hides nonmatches | The intersection itself may be sensitive |
| Synthetic data avoids raw release | Memorization and downstream misuse still matter |

## A Useful Mental Model

Every PET claim should complete this sentence:

> This system protects `<data or behavior>` from `<adversary>` under `<assumptions>`, while revealing `<allowed output>`.

If a claim cannot say that clearly, it is probably marketing rather than engineering.

## Worked Example

Weak claim:

> We use confidential computing to make RAG private.

Better claim:

> This RAG system runs prompt assembly and model execution in an attested TEE, reducing exposure of prompts and retrieved snippets to the cloud operator. It still relies on correct document permissions, log minimization, side-channel assumptions, and output review.

The better claim names the protected assets, adversary, assumptions, and remaining leakage paths. That is the altitude this guide aims for.
