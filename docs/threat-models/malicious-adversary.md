# Malicious Adversary

A malicious adversary may deviate from the protocol, submit malformed inputs, manipulate outputs, or selectively abort.

## Practical Example

A participant in federated learning sends poisoned updates while secure aggregation makes individual update inspection difficult.

## Good Fit

Use this model when parties have competing incentives, financial stakes, or weak governance.

## PET Implications

Prefer malicious-secure protocols, input validation, robust aggregation, audit logs, rate limits, and incident response plans.

## Common Gap

Many prototypes claim privacy against curious parties while product teams assume protection against malicious ones.

## What Changes In The Design

| Design area | Honest-but-curious design | Malicious-adversary review |
| --- | --- | --- |
| Inputs | Well-formed inputs are assumed | Validate format, range, provenance, and replay behavior |
| Participants | Identity is mostly administrative | Authenticate, rate-limit, suspend, and audit participants |
| Computation | Protocol privacy is the main concern | Add robustness, malicious security, or verifiable execution |
| Failure handling | Retry failed runs | Treat aborts, dropouts, and timing as possible signals |
| Operations | Debugging can inspect more artifacts | Debugging paths must not bypass privacy controls |
