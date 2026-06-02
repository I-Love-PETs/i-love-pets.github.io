# By Threat Model

## Honest-But-Curious Parties

Start with FL plus secure aggregation, MPC, HE, PSI, or clean rooms depending on the computation. This model is common for early designs but too weak for many real deployments.

## Malicious Parties

Prefer protocols and architectures with malicious-security controls, input validation, auditability, robust aggregation, and abuse monitoring. Expect more cost and less simplicity.

## Collusion

Ask which parties can combine views. Secure aggregation and MPC assumptions often depend on threshold assumptions. Clean rooms can also fail if platform operators and participants collude.

## External Attackers

PETs do not replace security engineering. Harden identity, access, key management, logging, vulnerability management, and incident response.

## Inference Attackers

If the concern is membership inference, reconstruction, gradient leakage, or attribute inference, use DP, output controls, secure aggregation, model auditing, and careful release review.

## Side-Channel Attackers

For TEEs and some cryptographic systems, consider timing, memory access, cache behavior, error channels, and operational metadata.
