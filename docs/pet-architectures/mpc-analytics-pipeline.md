# MPC Analytics Pipeline

## Goal

Compute joint metrics across organizations without revealing each party's raw inputs.

## Actors

Data providers, MPC compute parties, analyst, governance approver, and auditor.

## Data Flow

Providers secret-share or encrypt inputs, compute parties run the protocol, and only approved outputs are reconstructed.

## Trust Boundaries

No single compute party should learn raw inputs. Output recipients still learn the approved result.

## PET Stack

Secret sharing or garbled circuits, input validation, output policy, query approval, and audit logs.

## Deployment Notes

Define schemas, allowed functions, malicious-security requirements, retry behavior, and incident response before launch.

## Tradeoffs

MPC gives strong input privacy but adds protocol cost, coordination overhead, and specialized debugging.

## Failure Modes

Output leakage, malformed inputs, collusion beyond assumptions, schema drift, and analyst query abuse.
