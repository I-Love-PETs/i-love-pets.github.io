---
description: "Differentially Private Synthetic Data Release: protected assets, adversaries, allowed outputs, leakage, assumptions, non-goals, and checks for a concrete design review."
---

# Differentially Private Synthetic Data Release

## Decision framing

| Field | Scope |
| --- | --- |
| Protected asset | The contribution of the declared privacy unit to the released synthetic artifact. |
| Adversary | Recipients inspecting the release with auxiliary information. |
| Allowed output | Synthetic records and approved documentation under a stated DP budget. See [allowed output](../start-here/glossary.md#allowed-output). |
| Leakage surface | Preprocessing, model selection, helper statistics, tuning outputs, and unaccounted releases. See [leakage](../start-here/glossary.md#leakage). |
| Assumptions | The DP mechanism, privacy unit, clipping or sensitivity, randomness, and composition accounting cover the actual release process. |
| Non-goals | Perfect anonymity, preservation of every rare pattern, or protection of source data from the trusted data processor. |

--8<-- "decision-guidance.md"

## Problem

A team wants to share data-like artifacts without exposing raw records.

## When To Use

Use it for external research, prototyping, education, testing, and analytics when formal individual privacy is required.

## When Not To Use

Avoid it when downstream tasks need rare-tail fidelity that cannot survive privacy noise, or when no one will audit utility and memorization.

## Typical Architecture

Curate source data, train or fit a DP generator, release synthetic records, then publish privacy parameters, utility tests, and known limitations.

## Threat Model

Attackers may inspect released records, run membership inference, and compare against auxiliary data.

## Privacy Properties

DP limits the influence of any one record if the full pipeline is accounted for.

## Does not protect

- Raw records visible to the trusted processor.
- Population-level facts that the release is designed to preserve.
- Utility for every rare subgroup or misuse of the released data.

## Tools And Building Blocks

DP accounting, private histograms, DP generative models, memorization tests, utility benchmarks, and release review.

<span id="common-failure-modes"></span>

## Failure modes

Overstated anonymity, unaccounted preprocessing, weak epsilon choices, rare-record memorization, and misleading utility claims.

## Open Research Problems

Privacy auditing, utility measurement, memorization detection, and task-specific synthetic data evaluation.

## Related Pages

- [Synthetic data release pipeline](../pet-architectures/synthetic-data-release-pipeline.md)
- [Privacy benchmarks](../benchmarks/privacy.md)
- [Synthetic data research problems](../fix-my-itch/synthetic-data.md)
