# Membership Inference

Membership inference asks whether a person, record, or organization was included in a dataset, training run, or cohort.

## Practical Example

An attacker queries a fine-tuned model and infers that a particular medical note was part of training.

## Why It Matters

Membership itself can be sensitive, even if the record content is not revealed.

## Mitigations

Differential privacy, train/test discipline, memorization audits, access controls, and avoiding overfitting.

## Common Gap

Synthetic data and fine-tuned models are often released without testing membership or memorization risk.
