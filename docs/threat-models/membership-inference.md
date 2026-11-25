# Membership Inference

Membership inference asks whether a person, record, or organization was included in a dataset, training run, or cohort.

## Practical Example

An attacker queries a fine-tuned model and infers that a particular medical note was part of training.

## Why It Matters

Membership itself can be sensitive, even if the record content is not revealed.

## Mitigations

Use [differential privacy](../start-here/glossary.md#differential-privacy) when the released artifact needs a formal membership bound. Access controls and regularization can reduce risk in some settings. Use an audit to measure residual risk under the stated attacker access.

Report the true-positive rate at a low false-positive rate, with uncertainty. A single average accuracy or AUC can hide exposure among the examples most vulnerable to inference. See [Carlini et al. on LiRA (IEEE S&P 2022)](https://arxiv.org/abs/2112.03570). *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic.)*

Mitigation is strongest when it is built into the release process. Running a
membership test after the model is already integrated usually produces a hard
choice between delaying launch and accepting unclear risk.

## Common Gap

Synthetic data and fine-tuned models are often released without testing membership or memorization risk.

## When To Care Most

| Situation | Why membership matters |
| --- | --- |
| Medical, legal, employment, or child data | Inclusion can reveal sensitive status even when content is hidden. |
| Small cohorts or rare conditions | The model may learn distinctive records because there are few substitutes. |
| Public model or dataset release | Attackers can run many probes without operational friction. |
| Repeated releases | Differences between versions can reveal who entered or left the data. |

## Selected References

- Shokri et al., [*Membership Inference Attacks against Machine Learning Models*](https://arxiv.org/abs/1610.05820), IEEE Security & Privacy 2017. Introduces the common black-box framing for membership inference against ML models.
- Carlini et al., [*Extracting Training Data from Large Language Models*](https://arxiv.org/abs/2012.07805), USENIX Security 2021. Shows that rare or repeated training examples can sometimes be extracted from language models.
