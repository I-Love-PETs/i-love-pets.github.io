# Utility Benchmarks

!!! info "Review status"
    Last reviewed: 2026-09-16

    Evidence level: Expert judgment

    Source quality: Unsourced / illustrative

    Snapshot scope: Editorial measurement guidance. Validate the method and acceptance thresholds for your workload; examples are illustrative.

## Definition

Utility is how well the protected workflow supports its intended downstream decision. It is task-specific: a useful synthetic dataset for one aggregate analysis may be unsuitable for training a classifier. Measure the outcome that matters to the reader, including who loses utility.

## What to measure

| Workload | Useful measures |
| --- | --- |
| Model training or inference | Accuracy, precision/recall, calibration, and error by site, class, and subgroup |
| Synthetic data | Error on intended statistics, downstream task performance, rare-group fidelity |
| RAG | Retrieval precision/recall and answer correctness under each user's access constraints |
| DP aggregates | Absolute/relative error, uncertainty, and decision changes at operational thresholds |
| PSI-backed workflow | Match precision/recall and downstream false positives/negatives, including identifier errors |

## Measurement methodology

1. Name the decision and set acceptance thresholds before tuning. Include minimum subgroup performance and acceptable error where decisions have unequal consequences.
2. Define an eligible baseline and a fixed evaluation set. Keep training and evaluation separate, document site/time splits, and prevent duplicate people or records from leaking across splits.
3. Compare the same downstream task and output semantics. Keep data, preprocessing, and operating thresholds fixed where possible; report any model or workflow changes required by the PET.
4. Sweep relevant parameters, such as DP noise, quantization, or batching. Report utility together with privacy settings and cost. Account for data-dependent tuning in the privacy analysis when required.
5. Repeat stochastic runs and report sample sizes, variability, and an appropriate uncertainty interval. Break results down by site, subgroup, and rare cases; test drift or missing participants where relevant.

## Worked comparison

!!! warning "Illustrative arithmetic, not a benchmark"
    Evidence level: Needs evidence. Source quality: Unsourced / illustrative. The counts below are invented to show why aggregate accuracy can hide a failed acceptance threshold.

Suppose an evaluation set contains 1,000 independently held-out cases: 900 in group A and 100 in group B. Before testing, the team requires at least 85% overall accuracy and at least 80% in each group.

| Result | Baseline | PET candidate |
| --- | ---: | ---: |
| Group A correct / total | 828 / 900 = 92% | 819 / 900 = 91% |
| Group B correct / total | 82 / 100 = 82% | 70 / 100 = 70% |
| Overall correct / total | 910 / 1,000 = 91% | 889 / 1,000 = 88.9% |

The candidate loses 2.1 percentage points overall and still passes the overall threshold. It loses 12 percentage points in group B and fails that group's threshold. Under the stated rule, the team must revise or reject this candidate despite its acceptable average. A real report would add uncertainty intervals, repeat-run results, class balance, and error consequences before making a decision.

## Pitfalls

- Reporting only a global average, particularly across unequal sites or groups.
- Mixing percentage-point changes with relative percentage changes.
- Comparing a protected model with a baseline trained on different data without explaining the difference.
- Selecting privacy parameters on the test set, then reporting the same set as independent validation.
- Rewarding unauthorized retrieval because it makes answers more accurate; authorization is a requirement of the task.
- Treating utility on one task as evidence for all uses of a released dataset.

## Reporting

Report baselines, variance, subgroup behavior, and cases where the PET changes the decision. Include split rules, sample sizes, seeds, parameter sweeps, failed settings, and the predeclared acceptance thresholds in the [shared reporting template](scorecards.md#shared-reporting-template). Pair the result with [privacy](privacy.md) and [cost](cost.md).
