# Benchmarks Needed

PET benchmarks should help teams make decisions. A useful benchmark reports privacy, utility, cost, latency, robustness, developer effort, and the assumptions that make the result meaningful.

## Private RAG Benchmark Suite

| Field | Card |
| --- | --- |
| Problem | What should a PET benchmark suite for private RAG measure? |
| The itch | RAG privacy discussions focus on model execution while leaks often occur in retrieval, authorization, prompts, logs, and answers. |
| Why it matters | Enterprises may deploy "private RAG" that protects the wrong part of the pipeline. |
| Current workaround | Evaluate answer quality and add security review separately. |
| Why the workaround is insufficient | It misses privacy-specific failure modes and cannot compare TEE, governance-only, or hybrid designs. |
| What good progress would look like | A benchmark with document-access policies, adversarial prompts, logging checks, retrieval leakage tests, latency, and cost. |
| Difficulty | Medium |
| Good for | Benchmark maintainer, systems builder, privacy engineer |
| Related PETs | TEEs, confidential RAG, DP, access control |
| Possible first contribution | Build a small corpus with role-based permissions and measure unauthorized snippet exposure across two RAG designs. |

## Small-Organization PET Benchmark

| Field | Card |
| --- | --- |
| Problem | What PETs work for small organizations with limited infrastructure? |
| The itch | Many benchmarks assume expert operators, stable servers, and generous budgets. |
| Why it matters | Clinics, local governments, schools, nonprofits, and smaller firms need privacy-preserving collaboration too. |
| Current workaround | Exclude smaller participants or use centralized processing. |
| Why the workaround is insufficient | It reduces representativeness and blocks useful collaborations. |
| What good progress would look like | A benchmark that scores setup time, failure recovery, local compute needs, documentation quality, and support burden. |
| Difficulty | Good first research problem |
| Good for | Benchmark maintainer, systems builder, privacy engineer |
| Related PETs | FL, secure aggregation, clean rooms, TEEs |
| Possible first contribution | Time a fresh participant onboarding flow for an FL or analytics tool and record every manual step and failure. |

## Cost/Privacy/Utility Tradeoff Suite

| Field | Card |
| --- | --- |
| Problem | How can benchmarks compare cost, privacy, and utility tradeoffs across PETs? |
| The itch | Teams compare PETs using incompatible metrics: epsilon for DP, latency for HE, trust assumptions for TEEs, and protocol cost for MPC. |
| Why it matters | Decision makers need to see what they are buying with complexity and cost. |
| Current workaround | Run separate PET-specific evaluations. |
| Why the workaround is insufficient | It hides tradeoffs and makes the strongest-looking PET win the wrong workload. |
| What good progress would look like | A scorecard that reports protected asset, adversary, output leakage, utility, latency, cloud cost, and operational effort for the same task. |
| Difficulty | Hard |
| Good for | Benchmark maintainer, privacy engineer, systems builder |
| Related PETs | DP, MPC, HE, TEEs, FL |
| Possible first contribution | Compare DP query access, MPC aggregate, and clean-room aggregate for one measurement task using a shared scorecard. |

## Benchmark Reproducibility For PET Claims

| Field | Card |
| --- | --- |
| Problem | How can PET benchmark results be made reproducible enough for procurement and review? |
| The itch | Results often omit environment, parameter choices, data assumptions, and failure cases. |
| Why it matters | Builders cannot tell whether a benchmark applies to their workload. |
| Current workaround | Ask vendors or authors for clarification. |
| Why the workaround is insufficient | It does not create durable evidence. |
| What good progress would look like | A reporting standard with code, configs, threat model, data-generation process, parameters, cloud cost, and negative results. |
| Difficulty | Good first research problem |
| Good for | Benchmark maintainer, systems builder, policy researcher |
| Related PETs | All PETs |
| Possible first contribution | Publish a reproducibility checklist and apply it to three existing PET benchmarks. |
