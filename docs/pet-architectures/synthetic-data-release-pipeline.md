# Synthetic Data Release Pipeline

## Goal

Release data-like artifacts with explicit privacy and utility review.

## Actors

Data owner, privacy reviewer, generator operator, utility evaluator, release approver, and data consumers.

## Data Flow

Source data is minimized, a generator is trained, synthetic data is evaluated, privacy risk is audited, and release documentation is published.

## Trust Boundaries

Raw data remains inside the producing organization. Consumers receive only the synthetic artifact and documentation.

## PET Stack

DP mechanisms, synthetic data generators, memorization tests, utility benchmarks, and release governance.

## Deployment Notes

Publish limitations, privacy parameters if DP is used, evaluation tasks, and prohibited uses.

## Tradeoffs

Synthetic data is easy to consume but can overstate fidelity or privacy if not audited.

## Failure Modes

Rare-record leakage, utility overclaiming, unaccounted preprocessing, and reuse beyond intended scope.
