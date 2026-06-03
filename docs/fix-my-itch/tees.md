# TEEs

Trusted execution environments can make general-purpose confidential computation practical, but they introduce trust in hardware, firmware, attestation, cloud configuration, and side-channel mitigations.

## Side-Channel Risk In Real Deployments

| Field | Card |
| --- | --- |
| Problem | How should teams reason about side-channel risk in real TEE deployments? |
| The itch | Security reviews ask whether a TEE is safe, but the answer depends on workload, adversary, cloud configuration, patching, and leakage tolerance. |
| Why it matters | Teams can either overtrust TEEs or reject useful deployments because risk is hard to explain. |
| Current workaround | Cite vendor security material or add broad caveats. |
| Why the workaround is insufficient | It does not connect side channels to concrete architecture choices or mitigations. |
| What good progress would look like | A workload-level side-channel review method with explicit leakage channels, mitigations, and residual-risk statements. |
| Difficulty | Hard |
| Good for | Privacy engineer, systems builder, security researcher |
| Related PETs | TEEs, confidential inference, confidential RAG |
| Possible first contribution | Create a side-channel checklist for one confidential RAG architecture covering memory access, timing, logs, and metadata. |

## Understandable Remote Attestation

| Field | Card |
| --- | --- |
| Problem | Can remote attestation be made understandable to application developers? |
| The itch | Attestation is often treated as a cryptographic ceremony instead of a product requirement developers must integrate and monitor. |
| Why it matters | A confidential-computing claim is weak if clients do not verify what code and environment they are trusting. |
| Current workaround | Vendor SDK examples, manual security review, or no client-side verification. |
| Why the workaround is insufficient | It leaves attestation fragile, invisible, or disconnected from deployment changes. |
| What good progress would look like | Developer-facing attestation flows with clear failure states, version binding, policy checks, and logs. |
| Difficulty | Medium |
| Good for | Systems builder, privacy engineer, security engineer |
| Related PETs | TEEs |
| Possible first contribution | Build a minimal attested API example where the client refuses responses from unexpected code measurements. |

## Cloud Portability For Confidential Workloads

| Field | Card |
| --- | --- |
| Problem | How portable are confidential-computing workloads across clouds? |
| The itch | Teams want multi-cloud or migration options, but TEE features, attestation formats, operational tooling, and performance differ. |
| Why it matters | Lock-in can become a security, procurement, and resilience issue. |
| Current workaround | Pick one cloud and document assumptions. |
| Why the workaround is insufficient | It hides the cost of migration and makes privacy claims dependent on a single platform. |
| What good progress would look like | A portability matrix for workloads, attestation, key release, logging, and performance across major confidential-computing offerings. |
| Difficulty | Medium |
| Good for | Systems builder, privacy engineer, benchmark maintainer |
| Related PETs | TEEs, confidential inference, confidential RAG |
| Possible first contribution | Run one small confidential inference service on two environments and compare setup, attestation, and latency. |

## TEE Output Leakage

| Field | Card |
| --- | --- |
| Problem | How can TEE applications avoid leaking sensitive data through outputs and logs? |
| The itch | Teams protect runtime plaintext but still emit answers, traces, support bundles, and metrics that contain sensitive facts. |
| Why it matters | Many real privacy failures happen outside the protected enclave. |
| Current workaround | Add access controls and manual log review. |
| Why the workaround is insufficient | It treats output policy as an afterthought rather than part of the architecture. |
| What good progress would look like | Patterns that bind attested code, output policy, log minimization, and audit events. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, systems builder |
| Related PETs | TEEs, DP, confidential RAG |
| Possible first contribution | Instrument a toy confidential API to classify and suppress sensitive logs, then document remaining leaks. |
