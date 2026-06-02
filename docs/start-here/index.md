# Start Here

Privacy-enhancing technologies are not interchangeable. They protect different parts of a system, assume different adversaries, and create different tradeoffs.

Use this section to build a working vocabulary before choosing a PET.

## The Short Version

| PET | Best Fit | Watch Out For |
| --- | --- | --- |
| Federated learning | Training across data silos without centralizing raw data | Gradients and model updates can still leak information |
| Differential privacy | Limiting what can be learned about one person or record | Utility loss and accounting complexity |
| Secure multiparty computation | Joint computation across parties that do not reveal inputs | Cost, coordination, and protocol complexity |
| Homomorphic encryption | Computing on encrypted data | High cost and narrow workload fit |
| Trusted execution environments | Isolating computation in hardware-protected enclaves | Hardware trust, side channels, and attestation usability |
| Private set intersection | Finding overlap between datasets without exposing nonmatches | Output leakage and protocol integration |
| Synthetic data | Sharing generated data instead of raw data | Memorization, weak privacy claims, and utility drift |
| Data clean rooms | Controlled collaboration over governed datasets | Governance does not automatically equal cryptographic privacy |
| Zero-knowledge proofs | Proving a statement without revealing the witness | Circuit cost and proving-system expertise |

## How To Read This Guide

Start with the problem, not the PET. Ask:

- Who owns the data?
- What output is needed?
- Who must not learn what?
- What adversary is in scope?
- What latency, cost, and accuracy constraints are acceptable?

Then use the PET Compass to choose candidates and the pattern pages to design a system.
