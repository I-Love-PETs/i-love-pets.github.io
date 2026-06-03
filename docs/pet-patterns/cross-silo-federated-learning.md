# Cross-Silo Federated Learning

## Motivating Example

Five hospitals want to train a sepsis prediction model. Each hospital has sensitive patient records, different coding practices, and its own security review. They can run training locally but cannot send raw records to a central model owner.

## Problem

Cross-silo FL trains a shared model from local updates. It reduces raw-data movement, but gradients, model deltas, metrics, and final models can still leak. The deployment must handle non-IID data, dropouts, poisoning, update privacy, and local operations.

## When To Use

- Raw training data cannot centralize.
- The desired output is a shared model.
- Participants are stable organizations, not millions of unreliable devices.
- Each participant can run local training and maintain a secure environment.
- The program can evaluate per-site utility, not only global performance.

## When Not To Use

- Do not use FL if your real problem is governance, not data movement.
- Do not use FL when participants cannot operate local training reliably.
- Do not claim privacy from FL alone.
- Do not use FL for simple aggregate measurement; use federated analytics, MPC, or a clean room.
- Do not hide poor per-site performance behind a global average.

## Architecture

1. Coordinator defines model architecture, training code, round schedule, and evaluation plan.
2. Participants validate code and train locally on approved data.
3. Participants send updates, metrics, or encrypted/masked updates.
4. Aggregation combines updates and produces a new global model.
5. Evaluation reports global, per-site, and subgroup performance.
6. Release review checks memorization, inference risk, and intended use.

## Threat Model

| Actor | Concern |
| --- | --- |
| Coordinator | May inspect updates or infer participant data |
| Participant | May poison training or submit low-quality updates |
| Other participants | May infer information from the final model or shared metrics |
| Model user | May extract memorized training examples |
| External attacker | May compromise local training systems or coordinator infrastructure |

## Privacy Properties

- Raw data can remain inside each silo.
- Secure aggregation can hide individual participant updates from the coordinator if threshold assumptions hold.
- DP can bound individual contribution to the released model when correctly configured.
- TEEs can protect orchestration or aggregation under hardware trust assumptions.

## What This Does Not Protect Against

- Gradient or update leakage without supporting controls.
- Poisoning or backdoors by malicious participants.
- Inference attacks on the final model.
- Poor local security at participant sites.
- Bias from non-IID data and underrepresented participants.

## Tools And Building Blocks

- FL orchestration and participant clients.
- Secure aggregation.
- DP-SGD or output-level DP.
- Robust aggregation and anomaly detection.
- Local data validation.
- Model memorization and membership-inference tests.

## Operational Complexity

High. Cross-silo FL is a distributed systems program with ML risk. Expect participant onboarding, versioned code, key setup, round scheduling, failure recovery, per-site evaluation, and support for non-expert local operators.

## Cost Drivers

- Number of rounds and model size.
- Local compute and data engineering at each silo.
- Secure aggregation and DP overhead.
- Participant support and incident response.
- Evaluation across sites and subgroups.

## Failure Modes

- A small participant's update dominates a round and leaks information.
- Secure aggregation prevents useful debugging.
- DP budget choices make the model useless or indefensible.
- Non-IID data causes model harm at smaller sites.
- A participant poisons the model while update visibility is reduced.

## Evaluation Checklist

- Is the privacy unit a patient, account, device, or organization?
- Are updates treated as sensitive artifacts?
- What minimum round size is enforced?
- Are participant dropouts simulated?
- Are poisoning and backdoor attacks tested?
- Does evaluation include per-site and subgroup metrics?
- Is the final model tested for memorization or membership inference?

## Open Research Problems

- Realistic cross-silo non-IID benchmarks.
- Poisoning detection compatible with secure aggregation.
- Low-infrastructure FL participant tooling.
- Honest FL privacy claim templates.

## Related Pages

- [FL + secure aggregation](../pet-architectures/fl-secure-aggregation.md)
- [FL + differential privacy](../pet-architectures/fl-differential-privacy.md)
- [Federated learning problems](../fix-my-itch/federated-learning.md)
