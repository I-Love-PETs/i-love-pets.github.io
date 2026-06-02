# Claim Register

This register tracks claims that should be sourced, measured, narrowed, or softened before the guide is treated as decision-grade.

## Highest Priority Claims

| Claim Area | Current Risk | Needed Evidence | Evidence Level Target |
| --- | --- | --- | --- |
| HE inference cost | Qualitative cost claims can become stale quickly | Benchmarks by model family, latency, throughput, and hardware | Measured |
| MPC deployment cost | "Medium-to-high" is too vague | Named deployments or benchmarked analytics workloads | Measured or deployment-backed |
| DP utility impact | Utility loss depends heavily on task and privacy unit | Task-specific examples with epsilon, delta, and utility metrics | Measured |
| TEE side-channel risk | Risk varies by hardware, workload, and mitigation | Literature-backed threat summaries and deployment mitigations | Literature-backed |
| Synthetic data privacy | "Synthetic" is often mistaken for anonymous | Memorization and membership-inference audits | Measured |
| Clean room privacy | Governance claims may be confused with PET guarantees | Examples of output leakage and policy controls | Deployment-backed |
| Federated learning leakage | "Data stays local" can mislead readers | Gradient leakage examples and mitigation evidence | Literature-backed or measured |
| Private RAG leakage | Emerging area with weak shared benchmarks | Prompt, embedding, retrieval, and output leakage evaluations | Measured |

## How To Use This Register

When improving a page:

1. Pick one claim area.
2. Replace generic wording with a scoped claim.
3. Add evidence, or mark the claim as expert judgment.
4. Add a last-reviewed date for fast-moving claims.
5. Link to the relevant benchmark, threat model, or Fix My Itch page.

## Open Evidence Backlog

- Add 15 to 20 anchored quantitative or dated claims.
- Add 5 named deployment summaries or postmortems.
- Add source-backed "when not to use" statements for the top PET patterns.
- Add benchmark cards for HE inference, MPC analytics, DP synthetic data, and private RAG.
