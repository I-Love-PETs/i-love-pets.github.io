# Claim Register

This register tracks claims that should be sourced, measured, narrowed, or softened before the guide is treated as decision-grade.

!!! info "Review status"
    Last reviewed: 2026-06-17
    Evidence level: Expert judgment
    Snapshot scope: Current decision-support backlog after v0.7. Claims listed here are useful but still need stronger evidence, narrower wording, source-quality labels, or more explicit uncertainty labels before v1.0.

## Status Convention

Each tracked claim carries one of two statuses:

- **Resolved** — sufficient evidence has been identified or the claim has been narrowed and labelled so readers can calibrate their confidence. Inline notes on the relevant pages are in place.
- **Unresolved** — the claim is still too broad, too vague, or lacks sourcing that would make it decision-grade. The "Needed evidence" column describes what would close it.

Status is re-evaluated on each editorial pass and dated on change.

## Highest Priority Claims

| Claim area | Current risk | Needed evidence | Target level | Current state | Status | Note (2026-06-17) |
| --- | --- | --- | --- | --- | --- | --- |
| HE inference cost | Qualitative cost claims become stale quickly | Benchmarks by model family, latency, throughput, ciphertext size, and hardware, with source-quality labels | Measured | Needs evidence | **Unresolved** | No public cross-model latency benchmark found. Benchmark examples now mark HE numbers as Unsourced / illustrative; private-inference guidance remains Expert judgment until workload-specific measurements exist. |
| MPC deployment cost | "Medium-to-high" is too vague for buyers | Named deployments or benchmarked analytics workloads with parties, rounds, bandwidth, and operational effort | Measured or deployment-backed | Needs evidence | **Unresolved** | Boston MPC provides recurring civic-deployment evidence, but not a general cost model. Deployment pages now distinguish recurring production from proposed use cases. |
| DP utility impact | Utility loss depends heavily on task, privacy unit, and budget | Task-specific examples with epsilon, delta, utility metrics, release cadence, and independent analysis where available | Measured | Too broad | **Unresolved** | Census deep dive remains the strongest production example and is labeled primary/official plus independent analysis; no single source covers all DP workloads. |
| TEE side-channel risk | Risk varies by hardware, workload, and mitigation | Literature-backed threat summaries and deployment mitigation checklists | Literature-backed | Usable with caveat | **Resolved** | Covered by well-known research on SGX/TDX side-channels (e.g., Van Bulck et al., USENIX Security 2018; Intel Product Security advisories). Inline note remains on private-inference.md. |
| Synthetic data privacy | "Synthetic" is often mistaken for anonymous | Memorization and membership-inference audits for release workflows | Measured | Needs evidence | **Unresolved** | No single production audit standard exists. Benchmark examples now explicitly label synthetic-data values Unsourced / illustrative. |
| Clean room privacy | Governance claims can be confused with PET guarantees | Examples of output leakage, query controls, policy enforcement, and independent evaluations | Deployment-backed | Too broad | **Unresolved** | Ads Data Hub deep dive now labels source quality as primary/official vendor documentation; no public independent re-identification evaluation found. |
| Federated learning leakage | "Data stays local" can mislead readers | Gradient leakage examples, secure aggregation limits, DP mitigation evidence, and deployment-specific privacy tests | Literature-backed or measured | Usable with caveat | **Resolved** | Gradient leakage literature is well-established; EXAM and Japanese bank deep dives now explicitly separate raw-data locality from full privacy proof. |
| Private RAG leakage | Emerging area with weak shared benchmarks | Prompt, embedding, retrieval, log, citation, and output leakage evaluations | Measured | Needs evidence | **Unresolved** | No public benchmark covers all leakage surfaces. Example benchmark values remain illustrative only with Unsourced / illustrative source quality. |

## Page-Level Claim Review

| Section | Claim to watch | Risk | Next improvement |
| --- | --- | --- | --- |
| PET Compass | Tradeoff scores across PETs | Scores can look more precise than they are | Add review note explaining expert-judgment basis and workload variance |
| PET Patterns | Operational complexity labels | Complexity depends on tooling and deployment scale | Tie complexity to observable cost drivers |
| PET Architectures | Trust-boundary assumptions | Diagrams can imply stronger protection than text supports | Keep assumptions and non-protections next to data flows |
| Deployments | Production maturity and source quality | Vendor and consortium materials can overclaim maturity | Keep production, recurring, pilot, demonstration, vendor-case-study, and proposed-use labels visible |
| Benchmarks | Scorecard completeness and source quality | A scorecard can become checklist theater, and hypothetical example numbers can look like measured results | Label illustrative values as Unsourced / illustrative, or replace them with sourced measured runs |
| Use Cases | Domain recommendations | Domain rules can become too broad | Anchor recommendations to named scenarios |
| Tool Reviews | Tool maturity and version facts | Release, maintenance, and performance details drift quickly | Date each review, label uncertain facts, and re-check before procurement or adoption |

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
| Replace hypothetical benchmark values with sourced measurements | One measured or literature-backed scorecard each for HE inference, MPC analytics, DP synthetic data, and private RAG, with source-quality labels |
| Add stale-claim sweeps | Quarterly review of AI, RAG, tool maturity, and cost claims |
