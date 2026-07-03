# FL + Secure Aggregation

## Goal

Train a shared model while hiding individual participant updates from the coordinator.

## Actors

Participants, coordinator, model owner, secure-aggregation service, auditors, and downstream model users.

## Data Flow

```mermaid
flowchart LR
  C[Coordinator] -->|global model + training code| A[Site A]
  C -->|global model + training code| B[Site B]
  C -->|global model + training code| D[Site C]
  A -->|masked update| S[Secure aggregation]
  B -->|masked update| S
  D -->|masked update| S
  S -->|aggregate update| C
  C -->|new global model| U[Model users]
  C -->|round logs + metrics| L[Audit log]
```

## Trust Boundaries

| Boundary | What crosses | Who can see it | Risk |
| --- | --- | --- | --- |
| Site to coordinator | Training code, model version, round instructions | Site operators, coordinator | Bad code or wrong model version |
| Site to aggregation | Masked updates and metadata | Aggregation service | Update leakage if threshold/key assumptions fail |
| Aggregation to coordinator | Aggregate update | Coordinator | Small rounds can expose participants |
| Coordinator to users | Final model | Model users | Memorization and membership inference |
| System to logs | Metrics, errors, round metadata | Operators, auditors | Logs can reveal participant behavior |

## Assumptions

- Enough participants complete each round to satisfy secure-aggregation thresholds.
- Participant identity and key setup are reliable.
- Local training code is reviewed and versioned.
- The coordinator cannot inspect individual unmasked updates.

## PET Stack

Federated learning, secure aggregation, participant authentication, optional DP, robust aggregation, and model auditing.

## What This Does Not Protect Against

- Poisoned updates by malicious participants.
- Leakage from the final model.
- Weak local security at participant sites.
- Small-round inference.
- Debug logs that expose update metadata.

## Deployment Notes

Plan for participant dropouts, versioned training code, reproducible evaluation, secure key setup, and rollback when aggregation fails.

## Tradeoffs

Secure aggregation improves update privacy but makes debugging, anomaly detection, and malicious-client handling harder.

## Failure Modes

Gradient leakage without aggregation, poisoning, small participant rounds, key setup errors, weak participant identity, and plaintext operational logs.

## Evaluation Checklist

- What minimum number of participants is required per round?
- Are update sizes, timing, and dropouts logged safely?
- Is the final model tested for memorization?
- Can poisoning be detected without inspecting individual updates?
- Is the key setup recoverable after participant failure?

## References

- Bonawitz et al., [*Practical Secure Aggregation for Privacy-Preserving Machine Learning on User-Held Data*](https://arxiv.org/abs/1611.04482), 2016/2017.
- Zhu, Liu, and Han, [*Deep Leakage from Gradients*](https://arxiv.org/abs/1906.08935), NeurIPS 2019.
