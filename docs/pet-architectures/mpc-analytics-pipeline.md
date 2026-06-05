# MPC Analytics Pipeline

## Goal

Compute a joint analytic result across parties without revealing each party's raw inputs to a central processor.

## Actors

Data-contributing parties, protocol participants, query requester, output reviewer, auditors, and downstream decision makers.

## Data Flow

```mermaid
flowchart LR
  Q[Query requester] -->|approved query| P[Policy review]
  P -->|protocol spec| A[Party A]
  P -->|protocol spec| B[Party B]
  A -->|secret shares / protocol messages| M[MPC protocol]
  B -->|secret shares / protocol messages| M
  M -->|allowed output| O[Output reviewer]
  O -->|released metric| U[Decision makers]
```

## Trust Boundaries

| Boundary | What crosses | Who can see it | Risk |
| --- | --- | --- | --- |
| Requester to review | Query and intended output | Reviewers | Query may be too revealing |
| Parties to protocol | Shares and protocol messages | Protocol parties | Collusion or malformed inputs |
| Protocol to reviewer | Computed output | Reviewer | Output leakage |
| Reviewer to users | Released metric | Decision makers | Misuse or overinterpretation |

## Assumptions

- Collusion threshold is explicit.
- Parties authenticate each other and run the agreed protocol.
- Output policy is defined before computation.
- Malformed inputs are validated or handled.

## PET Stack

MPC, participant authentication, schema validation, query approval, output thresholding, optional DP, and audit logging.

## What This Does Not Protect Against

- Outputs that reveal sensitive facts.
- Collusion beyond the stated threshold.
- Malicious inputs if the protocol is only semi-honest.
- Poor schema alignment.
- Operational metadata leakage.

## Deployment Notes

Estimate rounds, bandwidth, availability requirements, and failure behavior before committing to the protocol.

## Tradeoffs

MPC reduces reliance on one trusted processor but increases protocol, networking, debugging, and participant-coordination complexity.

## Failure Modes

Unrealistic collusion assumptions, high latency, participant unavailability, malformed inputs, tiny-cohort outputs, and opaque cost.

## Evaluation Checklist

- What collusion threshold is claimed?
- Is malicious security required?
- What outputs are allowed or suppressed?
- How are schemas validated?
- What happens when a party drops out?
