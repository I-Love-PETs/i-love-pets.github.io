# Benchmarks

PET decisions should be based on evidence, not vibes.

Use this section when a PET choice sounds plausible but you need to know whether it survives real workload constraints.

## Benchmark Dimensions

| Dimension | Question |
| --- | --- |
| Privacy | Does the benchmark test the claim the system actually makes? |
| Utility | Does the PET preserve the downstream decision, not just a generic score? |
| Cost | What are compute, latency, bandwidth, storage, integration, and review costs? |
| Robustness | What happens under drift, poisoning, repeated queries, dropouts, or small cohorts? |
| Operations | Can a normal team deploy, monitor, debug, and explain the system? |
| Evidence quality | Is the result measured, deployment-backed, literature-backed, or expert judgment? |

## Benchmark Card

Every benchmark should report:

- workload and intended decision;
- data shape and privacy unit;
- threat model and allowed output;
- PET stack and parameters;
- hardware, software versions, and deployment assumptions;
- baselines and rejected alternatives;
- privacy, utility, cost, latency, and robustness results;
- failure cases and what the benchmark does not measure.

## Scorecards

Start with [Scorecards](scorecards.md) for reusable benchmark templates covering:

- private RAG;
- private inference;
- cross-silo FL;
- synthetic data release;
- federated analytics and MPC analytics.

## Anti-Patterns

- Reporting only accuracy when privacy loss is the core claim.
- Reporting only cryptographic runtime when integration dominates cost.
- Hiding failed parameter settings.
- Benchmarking on clean centralized data when deployment data is distributed and messy.
- Comparing PETs without naming the protected asset and adversary.
