# By Data Movement

## Raw Data Can Centralize

Centralization may be the simplest option, but privacy risk concentrates. Consider DP outputs, access controls, minimization, retention limits, and auditability.

## Raw Data Cannot Move

| Need | PET Candidates | Key Question |
| --- | --- | --- |
| Train a model | FL, secure aggregation, DP | Can participants support local training reliably? |
| Compute aggregate metrics | Federated analytics, MPC, clean rooms | Who is allowed to see the aggregate? |
| Match records | PSI, clean rooms | Is the intersection itself sensitive? |
| Run inference | HE, TEE | Is hardware trust acceptable? |
| Release data-like artifact | Synthetic data, DP synthetic data | How will privacy and utility be audited? |

## Data Moves To A Controlled Environment

Clean rooms and TEEs are useful when data can move only into a governed or confidential environment. The design question becomes: who controls code, policies, keys, logs, and outputs?

## Data Moves As Updates

Federated systems move gradients, model deltas, metrics, or sketches. Treat those artifacts as sensitive unless secure aggregation, DP, or other protections justify a narrower claim.
