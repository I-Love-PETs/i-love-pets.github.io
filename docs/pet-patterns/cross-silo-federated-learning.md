# Cross-Silo Federated Learning

## Problem

Organizations want to train a shared model without pooling raw training data.

## When To Use

Use it when participants are known institutions, data governance blocks centralization, and local training is operationally feasible.

## When Not To Use

Avoid it when participants cannot run reliable local jobs, labels are incompatible, or update leakage cannot be mitigated.

## Typical Architecture

A coordinator distributes model weights. Each silo trains locally and returns updates. Aggregation combines updates into a global model.

## Threat Model

Coordinator and silos may be honest-but-curious. Stronger designs consider poisoning, free-riding, collusion, and gradient leakage.

## Privacy Properties

Raw data stays local. Secure aggregation can hide individual updates. DP can bound training-record influence.

## Tools And Building Blocks

Federated orchestration, secure aggregation, DP-SGD, robust aggregation, model auditing, and participant attestation.

## Common Failure Modes

Non-IID performance collapse, poisoning, gradient leakage, participant dropouts, privacy budget confusion, and weak reproducibility.

## Open Research Problems

Personalization under privacy constraints, practical poisoning resistance, communication efficiency, and better leakage diagnostics.

## Related Pages

FL secure aggregation, FL differential privacy, membership inference, gradient leakage.
