# Benchmarks

PET decisions should be based on evidence, not vibes. A benchmark is the place
where a PET claim becomes falsifiable: it either protects the artifact you care
about within the workload constraints, or it does not.

Use this section when a PET choice sounds plausible but you need to know whether it survives real workload constraints.

Good benchmark design starts by writing the decision the benchmark must support.
"Compare HE and TEEs" is too broad. "Decide whether encrypted inference can meet
300 ms p95 latency for this fraud model while hiding client features from the
model host" is actionable.

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

## What To Report Even When The Result Is Bad

| Finding | Why it belongs in the benchmark |
| --- | --- |
| Parameter settings that failed | They prevent future teams from repeating the same tuning path. |
| Utility loss by subgroup or participant | Average utility can hide the exact population harmed by the PET. |
| Operational failure cases | Dropouts, key rotation, attestation gaps, and logging errors often dominate deployment risk. |
| Cost shape | PET costs can be nonlinear with parties, ciphertext size, rounds, or privacy budget. |
| Rejected baseline | A PET result is only meaningful if the simpler alternative is visible. |

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
- Treating a vendor demo as a workload benchmark without rerunning it under your data shape, latency budget, and operations model.
