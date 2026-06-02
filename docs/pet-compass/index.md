# PET Compass

!!! info "Review status"
    Last reviewed: 2026-06-02
    Evidence level: Expert judgment
    Snapshot scope: Starter decision guidance. Cost, maturity, and tooling claims need stronger sourced evidence before production use.

The PET Compass helps you choose a short list of candidate technologies before designing an architecture.

For the project's evidence standard, see [Evidence Policy](../project-standards/evidence-policy.md). For claims that need sourcing or measurement, see [Claim Register](../project-standards/claim-register.md).

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
