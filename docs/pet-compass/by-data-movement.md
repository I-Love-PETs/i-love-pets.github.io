# By Data Movement

Data movement is the first hard constraint. It does not decide the PET alone, but it rules out many bad ideas quickly.

## Decision Matrix

| Data movement pattern | Use this when... | Candidate PETs | Avoid this when... | Hidden cost |
| --- | --- | --- | --- | --- |
| Raw data centralizes | One party is allowed to process data and can be held accountable | Centralized processing, DP, minimization, access controls | The central operator is not trusted or cannot legally receive the data | Concentrated breach and misuse risk |
| Raw data stays at each party | Participants can compute locally and send protected artifacts | FL, federated analytics, secure aggregation, MPC, PSI | Participants cannot run reliable infrastructure or agree on protocols | Coordination, versioning, identity, and dropouts |
| Data enters a controlled environment | Data can move only into a governed or confidential boundary | Clean rooms, TEEs, confidential computing | The platform operator is in the adversary model and hardware trust is unacceptable | Policy, attestation, logging, and procurement |
| Only encrypted inputs move | The service must not see plaintext inputs | HE, MPC, PSI | The workload is broad, interactive, or latency-sensitive without benchmarking | Cost, limited operators, complex debugging |
| Model updates move | Training data remains local but gradients, weights, or metrics leave | FL, secure aggregation, DP, robust aggregation | You cannot tolerate update leakage or poisoning risk | Updates are still sensitive artifacts |
| Data-like artifacts leave | External users need something shaped like data | Synthetic data, DP synthetic data | Users need high-fidelity rare cases or individual-level truth | Memorization testing and utility validation |

## Raw Data Can Centralize

Centralization can be the right answer. Do not choose a complex PET only to avoid saying that governance is the real problem.

Use centralization when:

- one accountable operator is acceptable;
- access control, minimization, retention limits, and audit logs are enforceable;
- the workload needs high fidelity, low latency, or operational simplicity;
- the privacy claim is about controlled processing, not cryptographic separation.

Add **differential privacy** when the released output must limit the contribution of one person, account, device, or organization. DP is an output guarantee; it does not make sloppy data handling safe.

## Raw Data Cannot Move

| Need | Better starting point | What can break |
| --- | --- | --- |
| Train a shared model | Cross-silo FL | Update leakage, poisoning, non-IID data, weak local operations |
| Compute aggregate metrics | Federated analytics or MPC | Small-cell leakage, collusion, expensive protocols |
| Find common records | PSI | The intersection may itself be sensitive |
| Serve inference | HE or TEE confidential inference | HE latency, TEE trust assumptions, output leakage |
| Release data-like artifacts | DP synthetic data | Memorization, weak utility, misunderstood residual risk |

The phrase "data cannot move" is underspecified. Ask whether **records**, **features**, **labels**, **identifiers**, **gradients**, **embeddings**, **prompts**, **logs**, or **outputs** can move. Many failures happen because teams protect one artifact and leak another.

## Data Moves To A Controlled Environment

Clean rooms and TEEs are useful when data can move only into a governed or confidential environment.

Use this when:

- the main need is controlled collaboration, auditability, or policy enforcement;
- the computation is too broad for HE or MPC;
- the parties accept a platform, hardware, or operator trust assumption;
- outputs can be reviewed before release.

Avoid this when:

- the platform operator is explicitly untrusted;
- participants cannot verify code, policy, logs, or attestation;
- the output will reveal the sensitive fact anyway;
- the team is using "clean room" as a vague procurement label.

## Data Moves As Updates

Federated systems move gradients, model deltas, sketches, or metrics. Treat these as sensitive unless there is evidence otherwise.

Use supporting PETs based on the leakage:

| Leakage concern | Add | Caveat |
| --- | --- | --- |
| Coordinator should not inspect individual updates | Secure aggregation | Makes debugging and poisoning detection harder |
| Individual participation should be bounded | Differential privacy | Utility may drop and accounting must be maintained |
| Clients may send malicious updates | Robust aggregation, validation, anomaly detection | Harder when updates are hidden |
| Sites may be small or unique | Minimum round sizes, grouping, DP | Small cohorts can defeat aggregate privacy intuition |

## Worked Example: Cross-Bank Fraud Signals

Two banks cannot share raw transactions. They first think "federated learning," but the immediate business question is whether accounts appearing at both banks are associated with known mule patterns.

Better path:

1. Use **PSI** to identify permitted overlap or **MPC** if the fraud score requires joint features.
2. Apply thresholds and output review so tiny match sets are not exposed.
3. Consider FL only after there is a stable shared modeling task.

The recommendation changes if the banks need a continuously trained model rather than a specific joint computation.

## Checklist

- What exact artifact is forbidden to move?
- Who sees intermediate values?
- Who sees the final output?
- Can parties collude?
- Are there minimum cohort sizes?
- Does the chosen PET protect inputs, outputs, both, or neither?
- What is the cheapest evidence that would disprove the design?
