# Membership Inference

Membership inference asks whether a person, record, or organization was included in a dataset, training run, or cohort.

## Practical Example

An attacker queries a fine-tuned model and infers that a particular medical note was part of training.

## Why It Matters

Membership itself can be sensitive, even if the record content is not revealed.

## Mitigations

Differential privacy, train/test discipline, memorization audits, access controls, and avoiding overfitting.

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
