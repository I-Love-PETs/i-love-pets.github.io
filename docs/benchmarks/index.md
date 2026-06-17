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

## Benchmark Source Quality

Benchmark claims need both an evidence level and a source-quality label. A measured value from a vendor blog is not the same thing as a reproducible benchmark package, and an illustrative scorecard value is not a measurement.

| Source quality | Meaning | Decision use |
| --- | --- | --- |
| Reproducible benchmark package | Workload, code, data or data generator, environment, and run date are available | Strongest benchmark evidence if the workload matches |
| Peer-reviewed measurement | Paper reports workload, method, parameters, and limits | Useful with scope checks; reproduce before procurement |
| Operator measurement | Deploying team or vendor reports measured results | Useful lead; validate independently for high-stakes decisions |
| Independent replication | Non-operator repeats or challenges a claimed result | Strong evidence for or against generalization |
| Expert estimate | Maintainer or practitioner estimate without a run artifact | Planning only; replace before commitment |
| Unsourced / illustrative | Teaching value created for a scorecard example | Never cite as performance evidence |

*(Evidence: Expert judgment. Source quality: Project standard. Reviewed 2026-06-17 — this taxonomy is a reporting discipline, not a measurement result.)*

## Benchmark Card

Every benchmark should report:

- workload and intended decision;
- data shape and privacy unit;
- threat model and allowed output;
- PET stack and parameters;
- hardware, software versions, and deployment assumptions;
- baselines and rejected alternatives;
- privacy, utility, cost, latency, and robustness results;
- evidence level and source-quality label for each high-impact result;
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
