# PET Architectures

Architecture pages turn PET choices into deployable system shapes. They emphasize actors, data flow, trust boundaries, PET stack, deployment notes, tradeoffs, and failure modes.

## Architecture Catalog

| Architecture | Use When |
| --- | --- |
| FL + secure aggregation | Individual model updates should be hidden from the coordinator |
| FL + differential privacy | Training participation or records need formal protection |
| MPC analytics pipeline | Multiple parties need joint analytics without a trusted central processor |
| HE private inference API | Clients need inference without revealing plaintext inputs |
| Confidential RAG | Retrieval and generation cross sensitive trust boundaries |
| Synthetic data release pipeline | Teams need data-like artifacts with privacy and utility review |
