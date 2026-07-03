# PET Architectures

Architecture pages turn PET choices into deployable system shapes. They emphasize actors, data flow, trust boundaries, PET stack, deployment notes, tradeoffs, and failure modes.

## Architecture Catalog

| Architecture | Use when | Main trust-boundary question |
| --- | --- | --- |
| [FL + secure aggregation](fl-secure-aggregation.md) | Individual model updates should be hidden from the coordinator | Who can see individual updates before aggregation? |
| [FL + differential privacy](fl-differential-privacy.md) | Training participation or records need formal protection | What privacy unit and budget apply to the released model? |
| [MPC analytics pipeline](mpc-analytics-pipeline.md) | Multiple parties need joint analytics without a trusted central processor | Which parties may collude, and what output is allowed? |
| [HE private inference API](he-private-inference-api.md) | Clients need inference without revealing plaintext inputs | Who controls encryption keys and sees predictions? |
| [Confidential RAG](confidential-rag.md) | Retrieval and generation cross sensitive trust boundaries | Who can see prompts, snippets, logs, and answers? |
| [Synthetic data release pipeline](synthetic-data-release-pipeline.md) | Teams need data-like artifacts with privacy and utility review | What privacy claim applies to the released artifact? |

## Review Standard

Every architecture should make these visible:

- actors and data owners;
- data flows, including logs and outputs;
- trust boundaries and control points;
- assumptions about hardware, collusion, keys, and participants;
- what the PET does not protect against;
- operational risks and evaluation checks.

If a diagram omits logs or outputs, assume the architecture is incomplete until the text covers them.

## Architecture Review Questions

| Question | Good answer looks like |
| --- | --- |
| What assumptions am I making? | Named assumptions about parties, thresholds, hardware, keys, privacy units, and output policy. |
| What can fail operationally? | Dropouts, unavailable parties, key rotation, logging mistakes, attestation drift, budget exhaustion, or release pressure. |
| What attacks are outside scope? | Explicit exclusions such as malicious participants, side channels, compromised clients, or downstream misuse. |
| Which PETs are commonly combined? | The supporting PETs needed for the real threat model, not a longer acronym list. |
| How do I know it worked? | Evaluation checks tied to the protected artifact and allowed output. |
