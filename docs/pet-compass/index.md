# PET Compass

!!! info "Review status"
    Last reviewed: 2026-06-02
    Evidence level: Expert judgment
    Snapshot scope: Starter decision guidance. Cost, maturity, and tooling claims need stronger sourced evidence before production use.

The PET Compass helps you choose a short list of candidate technologies before designing an architecture.

For the project's evidence standard, see [Evidence Policy](../project-standards/evidence-policy.md). For claims that need sourcing or measurement, see [Claim Register](../project-standards/claim-register.md).

Use the Compass to write a decision memo, not just a technology name. Each
recommendation should include:

| Field | What to write |
| --- | --- |
| Recommended PET | The primary PET or PET stack to test first. |
| Alternative PETs | Plausible options and the condition that would make each one better. |
| Why | The protected asset, adversary, allowed output, and data-movement constraint. |
| Tradeoffs | Utility, latency, cost, trust, governance, and developer effort. |
| Failure modes | Leakage paths, abuse cases, and assumptions that commonly break. |
| Operational considerations | Keys, attestation, logging, monitoring, incident response, and benchmark ownership. |

## Decision Inputs

| Question | Why It Matters |
| --- | --- |
| Can raw data move? | Determines whether centralization, federated learning, MPC, HE, TEEs, or clean rooms are realistic. |
| Is a formal privacy guarantee required? | Differential privacy may be necessary, either alone or in composition. |
| What output is allowed? | Protected inputs do not prevent output leakage. |
| Who is the adversary? | Honest-but-curious, malicious, colluding, and external attackers require different controls. |
| Is hardware trust acceptable? | TEEs are practical when hardware and attestation are acceptable assumptions. |
| What latency and cost are tolerable? | HE and MPC may be excellent but too expensive for some workloads. |

## Starter Recommendation Matrix

| Constraint | Start With | Often Combine With |
| --- | --- | --- |
| Data cannot move | FL, MPC, HE, TEE, clean room | Secure aggregation, DP, auditing |
| Formal individual privacy is required | DP | FL, synthetic data, clean rooms |
| Encrypted inference is required | HE | TEE for hybrid designs, model compression |
| Hardware trust is acceptable | TEE | DP, audit logs, policy controls |
| Aggregate measurement is needed | Federated analytics, clean room, MPC | DP thresholds, output review |
| Safer sharing is needed | Synthetic data | DP, privacy auditing, utility tests |

## Do Not Stop At The Matrix

The matrix produces candidates, not an architecture. After choosing a candidate PET, move to patterns and threat models.

Before committing to a design, collect evidence for the target workload: expected latency, utility, privacy guarantee, adversary model, deployment complexity, and output leakage.

## Common Recommendation Shapes

| Scenario | Recommended PET | Alternative PETs | Why | Tradeoffs | Failure modes | Operational considerations |
| --- | --- | --- | --- | --- | --- | --- |
| Healthcare model training | Cross-silo FL + secure aggregation; add DP if patient-level contribution must be bounded | Governed centralization, clean room training, MPC for narrow analytics | Hospitals keep records local while contributing to a model | Non-IID data, local infra, DP utility cost | Update leakage, poisoned updates, small-site underperformance | Participant onboarding, round thresholds, per-site evaluation, rollback |
| Finance fraud collaboration | PSI or MPC for joint signals; FL when the goal is a shared model | Clean room, governed exchange, federated analytics | Fraud evidence often depends on overlap and joint features | Entity resolution, latency, collusion assumptions | Sensitive match sets, repeated-query leakage, unfair outcomes | Identifier hygiene, minimum cohorts, analyst audit trail |
| Private inference | TEE for broad model support; HE for narrow models with strict no-plaintext-input requirements | Client-side inference, standard hosted inference with controls | The service should not see plaintext inputs | HE latency/operator limits; TEE hardware trust | Output leakage, weak attestation, plaintext logs | Key management, attestation verification, p95 latency benchmark |
| Private RAG | Confidential RAG with authorization-aware retrieval | Ordinary RAG with governance, segmented search, redaction workflow | Retrieval context and prompts cross trust boundaries | Runtime protection does not fix permissions | Overbroad retrieval, answer leakage, sensitive logs | Access-control tests, provenance, log retention, incident workflow |
| Synthetic data release | DP synthetic data for broad release claims | DP query access, restricted sharing, non-DP synthetic data for internal prototyping | Users need data-like artifacts without raw release | Utility loss and privacy-budget explanation | Memorization, rare-record leakage, overtrusted data | Release review, nearest-neighbor tests, downstream task benchmarks |
| Cross-organizational analytics | Federated analytics or MPC; clean room when governance is the main need | DP query system, governed centralization | Parties need an aggregate output without broad raw sharing | Protocol cost, metric harmonization, output policy | Small-cell leakage, collusion, repeated queries | Schema alignment, thresholds, query review, evidence labels |
