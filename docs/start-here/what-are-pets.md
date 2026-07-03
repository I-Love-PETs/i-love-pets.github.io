# What Are PETs?

Privacy-enhancing technologies are techniques that reduce privacy risk while still allowing useful computation, measurement, learning, sharing, or verification.

They usually change one of four things:

- where data moves;
- what a party can observe;
- what outputs reveal;
- which trust assumptions are required.

A PET is therefore a design constraint, not a privacy certificate. It can make one
data path safer while making another path more important: outputs, logs, metadata,
keys, model releases, and governance decisions still need their own review.

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

They are especially useful when the team can describe the minimum output needed
for the job. "Train a fraud model" is still broad. "Produce a model update that
improves cross-bank recall without exposing customer-level transactions or
bank-specific anomalies" is closer to an engineering requirement.

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

## What To Ask In A Review

| Review question | Bad answer | Better answer |
| --- | --- | --- |
| What is protected? | "The data." | "Raw records are local; aggregate updates and the final model are still visible." |
| From whom? | "Unauthorized users." | "The coordinator must not inspect individual site updates; participants may still see the final model." |
| Under which assumption? | "The platform is secure." | "At least 20 sites complete each round and the secure-aggregation key setup is correct." |
| What is intentionally revealed? | "Only insights." | "A model, validation metrics, and round-level participation metadata." |
| How do we know it worked? | "The PET is state of the art." | "We measured leakage tests, subgroup utility, latency, and operational failure cases on the target workflow." |

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
