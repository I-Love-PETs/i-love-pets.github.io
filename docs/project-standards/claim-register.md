# Claim Register

This register tracks claims that should be sourced, measured, narrowed, or softened before the guide is treated as decision-grade.

!!! info "Review status"
    Last reviewed: 2026-06-05
    Evidence level: Expert judgment
    Snapshot scope: v0.4 editorial backlog for claims that need stronger evidence or tighter wording.

## Highest Priority Claims

| Claim area | Current risk | Needed evidence | Target level | Current state |
| --- | --- | --- | --- | --- |
| HE inference cost | Qualitative cost claims become stale quickly | Benchmarks by model family, latency, throughput, ciphertext size, and hardware | Measured | Needs evidence |
| MPC deployment cost | "Medium-to-high" is too vague for buyers | Named deployments or benchmarked analytics workloads with parties, rounds, and bandwidth | Measured or deployment-backed | Needs evidence |
| DP utility impact | Utility loss depends heavily on task, privacy unit, and budget | Task-specific examples with epsilon, delta, utility metrics, and release cadence | Measured | Too broad |
| TEE side-channel risk | Risk varies by hardware, workload, and mitigation | Literature-backed threat summaries and deployment mitigation checklists | Literature-backed | Usable with caveat |
| Synthetic data privacy | "Synthetic" is often mistaken for anonymous | Memorization and membership-inference audits for release workflows | Measured | Needs evidence |
| Clean room privacy | Governance claims can be confused with PET guarantees | Examples of output leakage, query controls, and policy enforcement | Deployment-backed | Too broad |
| Federated learning leakage | "Data stays local" can mislead readers | Gradient leakage examples, secure aggregation limits, and DP mitigation evidence | Literature-backed or measured | Usable with caveat |
| Private RAG leakage | Emerging area with weak shared benchmarks | Prompt, embedding, retrieval, log, citation, and output leakage evaluations | Measured | Needs evidence |

## Page-Level Claim Review

| Section | Claim to watch | Risk | Next improvement |
| --- | --- | --- | --- |
| PET Compass | Tradeoff scores across PETs | Scores can look more precise than they are | Add review note explaining expert-judgment basis and workload variance |
| PET Patterns | Operational complexity labels | Complexity depends on tooling and deployment scale | Tie complexity to observable cost drivers |
| PET Architectures | Trust-boundary assumptions | Diagrams can imply stronger protection than text supports | Keep assumptions and non-protections next to data flows |
| Deployments | Production maturity | Vendor and consortium materials can overclaim maturity | Keep pilot/production/research/unclear labels visible |
| Benchmarks | Scorecard completeness | A scorecard can become a checklist theater | Add example benchmark runs in future versions |
| Use Cases | Domain recommendations | Domain rules can become too broad | Anchor recommendations to named scenarios |

## Claim Rewrite Examples

| Weak claim | Better claim |
| --- | --- |
| FL protects data because data stays local. | FL reduces raw-data movement, but updates and final models can still leak without secure aggregation, DP, and model auditing. |
| HE is too slow for ML. | HE inference can be expensive and operator-constrained; benchmark latency, ciphertext size, and accuracy for the target model before choosing it. |
| Synthetic data is safe to share. | Synthetic data needs memorization and membership-inference testing; use DP synthetic data when the release needs a formal individual privacy claim. |
| TEEs make RAG private. | TEEs can reduce runtime exposure, but private RAG still needs authorization, retrieval policy, log controls, and output review. |
| Clean rooms preserve privacy. | Clean rooms provide governed workflows; privacy depends on query rules, access controls, output policy, and platform trust. |

## How To Use This Register

When improving a page:

1. Pick one claim area.
2. Replace generic wording with a scoped claim.
3. Add evidence, or mark the claim as expert judgment.
4. Add a last-reviewed date for fast-moving claims.
5. Link to the relevant benchmark, threat model, deployment, or Fix My Itch page.

## Open Evidence Backlog

| Backlog item | Best next artifact |
| --- | --- |
| Add anchored quantitative or dated claims | Source-backed inline notes on Compass, Patterns, and Benchmarks pages |
| Add named deployment summaries or postmortems | Deployment entries with maturity and limitations |
| Add source-backed "when not to use" statements | Pattern-page caveats linked to evidence or incidents |
| Add benchmark examples | One worked scorecard each for HE inference, MPC analytics, DP synthetic data, and private RAG |
| Add stale-claim sweeps | Quarterly review of AI, RAG, tool maturity, and cost claims |
