# Private LLM Fine-Tuning

## Motivating Example

An enterprise wants to fine-tune a language model on support tickets, internal policies, and incident reports. The data contains customer identifiers, credentials, employee information, and commercially sensitive procedures.

## Problem

Private LLM fine-tuning adapts a model using sensitive data while reducing exposure during training and release. The hard questions are where data lives, whether the model memorizes, what formal guarantee is required, and whether the resulting model can be used safely.

## When To Use

- The base model is not good enough with prompting or retrieval alone.
- Sensitive examples are needed for the target behavior.
- The team can measure utility and memorization.
- The deployment can define who may access the tuned model.
- Privacy controls are chosen before training, not added after release.

## When Not To Use

- Do not fine-tune if RAG, prompting, or rules solve the problem with less privacy risk.
- Do not use synthetic data without privacy evaluation.
- Do not claim privacy because training happened in FL or a TEE.
- Do not use DP fine-tuning without checking utility under realistic compute budgets.
- Do not release tuned weights broadly if the training data is sensitive.

## Architecture

| Data constraint | Pattern | Main risk |
| --- | --- | --- |
| Data can centralize in a controlled environment | Centralized fine-tuning with minimization and audits | Concentrated data and model-release risk |
| Data stays at organizations | Federated fine-tuning | Update leakage, non-IID data, local operations |
| Formal record-level guarantee is required | DP fine-tuning or DP adapters | Utility loss and budget accounting |
| Hardware trust is acceptable | TEE-based training or adapter tuning | Attestation, side channels, logs |
| Raw examples are too risky | Redaction or synthetic data plus evaluation | Weak privacy guarantees and lost utility |

## Threat Model

| Actor | Concern |
| --- | --- |
| Training operator | May inspect raw examples, gradients, logs, or checkpoints |
| Model user | May extract memorized training examples |
| Data owner | May lose control of tuned weights or adapters |
| Participant in FL | May infer other participants' data from updates or model behavior |
| External attacker | May compromise training infrastructure, artifacts, or logs |

## Privacy Properties

- DP can bound contribution to training when configured and accounted for correctly.
- FL can keep raw examples local but does not hide updates by itself.
- Secure aggregation can hide participant updates from a coordinator.
- TEEs can reduce training-time exposure under hardware trust assumptions.
- Redaction and minimization reduce the amount of sensitive data entering training.

## What This Does Not Protect Against

- Memorization in the final model unless tested and mitigated.
- Sensitive outputs produced during ordinary use.
- Prompt injection or misuse after deployment.
- Leaks through checkpoints, experiment trackers, or logs.
- Poor privacy-budget choices.
- Data that should never have been used for training.

## Tools And Building Blocks

- Data minimization and redaction pipelines.
- DP-SGD, DP adapters, clipping, and accounting.
- FL orchestration and secure aggregation.
- TEE training environments and attestation.
- Memorization, canary, and extraction tests.
- Model access controls and release review.

## Operational Complexity

High. Private fine-tuning touches data governance, ML training, privacy accounting, infrastructure security, evaluation, model release, and incident response.

## Cost Drivers

- DP training overhead and utility recovery.
- Model size, adapter strategy, and number of experiments.
- Secure or confidential training infrastructure.
- Human review of training data and outputs.
- Memorization testing and red-team evaluation.

## Failure Modes

- Training examples appear verbatim in model outputs.
- Experiment trackers store sensitive prompts or gradients.
- DP budget is chosen after utility tuning, invalidating the claim.
- FL updates leak site-specific information.
- A tuned adapter is shared more broadly than the data owner intended.
- Synthetic examples reproduce sensitive records.

## Evaluation Checklist

- Is fine-tuning necessary compared with RAG or prompting?
- What data is excluded before training?
- What privacy unit and budget apply if DP is used?
- Are checkpoints, logs, and experiment artifacts covered?
- Are memorization and extraction tests run before release?
- Who can access the tuned model, adapter, or weights?
- What outputs are blocked or reviewed?

## Open Research Problems

- Useful DP fine-tuning under realistic compute budgets.
- Memorization tests that reflect enterprise data.
- FL fine-tuning benchmarks with non-IID organizations.
- Release policies for tuned models and adapters trained on sensitive data.

## Related Pages

- [By ML task](../pet-compass/by-ml-task.md#fine-tuning)
- [Differential privacy problems](../fix-my-itch/differential-privacy.md)
- [Federated learning problems](../fix-my-itch/federated-learning.md)
- [Synthetic data problems](../fix-my-itch/synthetic-data.md)
