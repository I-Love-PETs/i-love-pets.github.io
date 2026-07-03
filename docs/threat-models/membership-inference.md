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

## Selected References

- Shokri et al., [*Membership Inference Attacks against Machine Learning Models*](https://arxiv.org/abs/1610.05820), IEEE Security & Privacy 2017. Introduces the common black-box framing for membership inference against ML models.
- Carlini et al., [*Extracting Training Data from Large Language Models*](https://arxiv.org/abs/2012.07805), USENIX Security 2021. Shows that rare or repeated training examples can sometimes be extracted from language models.
