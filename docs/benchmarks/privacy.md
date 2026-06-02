# Privacy Benchmarks

## What To Measure

Privacy benchmarks should test the claim the system actually makes.

| Claim | Measurement |
| --- | --- |
| Model updates are protected | Gradient leakage and reconstruction tests |
| Training records are protected | Membership inference and DP accounting |
| Synthetic records are safe | Memorization and nearest-neighbor audits |
| Query outputs are safe | Differencing, small-cell, and repeated-query tests |
| Runtime is confidential | Side-channel and logging review |

## Reporting

State the adversary, auxiliary information, query budget, and success metric.
