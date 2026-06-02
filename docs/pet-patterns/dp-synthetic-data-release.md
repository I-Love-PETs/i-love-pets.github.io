# Differentially Private Synthetic Data Release

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

## Tools And Building Blocks

DP accounting, private histograms, DP generative models, memorization tests, utility benchmarks, and release review.

## Common Failure Modes

Overstated anonymity, unaccounted preprocessing, weak epsilon choices, rare-record memorization, and misleading utility claims.

## Open Research Problems

Privacy auditing, utility measurement, memorization detection, and task-specific synthetic data evaluation.

## Related Pages

Synthetic data release pipeline, DP benchmarks, synthetic data research problems.
