# PET Composition

Real systems combine PETs. The hard part is not naming the stack; it is explaining how guarantees interact, degrade, or leave gaps.

## FL + DP + Secure Aggregation

| Field | Card |
| --- | --- |
| Problem | What does it mean to compose FL, DP, and secure aggregation? |
| The itch | Teams describe the stack as if each PET simply adds privacy, but each one protects a different artifact under different assumptions. |
| Why it matters | Misstated guarantees lead to bad architecture reviews and overconfident deployment claims. |
| Current workaround | List all PETs used and add caveats separately. |
| Why the workaround is insufficient | It does not explain which adversary sees updates, aggregates, final models, logs, and outputs. |
| What good progress would look like | A composition template that maps each PET to protected assets, adversaries, assumptions, and residual leakage. |
| Difficulty | Medium |
| Good for | Privacy engineer, ML researcher, systems builder |
| Related PETs | FL, DP, secure aggregation |
| Possible first contribution | Draw one FL + secure aggregation + DP architecture and annotate every privacy claim with protected artifact and failure mode. |

## Guarantee Degradation Across Chains

| Field | Card |
| --- | --- |
| Problem | How do guarantees degrade when PETs are chained? |
| The itch | A pipeline may use DP statistics, synthetic data, clean-room joins, and model training, but the end-to-end claim is unclear. |
| Why it matters | Users hear the strongest component guarantee and assume it applies to the whole system. |
| Current workaround | Review each component independently. |
| Why the workaround is insufficient | Component reviews miss composition, repeated releases, auxiliary information, and output reuse. |
| What good progress would look like | A method for tracing privacy units, assumptions, outputs, and composition costs across a pipeline. |
| Difficulty | Hard |
| Good for | Privacy engineer, policy researcher, cryptographer |
| Related PETs | DP, synthetic data, clean rooms, MPC |
| Possible first contribution | Analyze one synthetic-data pipeline from raw data to release and identify where the strongest claim stops applying. |

## Trust-Boundary Architecture Diagrams

| Field | Card |
| --- | --- |
| Problem | How can architecture diagrams include explicit trust boundaries? |
| The itch | PET diagrams often show data flows but omit who controls code, keys, logs, policies, and outputs. |
| Why it matters | Reviewers cannot evaluate a privacy claim if they cannot see where trust changes. |
| Current workaround | Add prose threat-model notes after the diagram. |
| Why the workaround is insufficient | Prose gets separated from the design and misses changes during implementation. |
| What good progress would look like | A diagram notation for actors, trust zones, protected artifacts, allowed outputs, and assumption labels. |
| Difficulty | Good first research problem |
| Good for | Systems builder, privacy engineer, technical writer |
| Related PETs | All PETs |
| Possible first contribution | Redraw three existing PET diagrams with trust boundaries, control points, and output leakage notes. |

## Composition Test Cases

| Field | Card |
| --- | --- |
| Problem | What test cases reveal broken PET composition? |
| The itch | A composed PET stack may pass component tests while leaking through logs, outputs, repeated queries, or small cohorts. |
| Why it matters | Builders need tests that catch architecture-level privacy failures before launch. |
| Current workaround | Security review and manual red-team exercises. |
| Why the workaround is insufficient | It is expensive and not reusable across projects. |
| What good progress would look like | Reusable privacy test cases for common compositions such as FL + DP, PSI + clean room, and TEE + RAG. |
| Difficulty | Medium |
| Good for | Privacy engineer, benchmark maintainer, systems builder |
| Related PETs | FL, DP, PSI, TEEs, clean rooms |
| Possible first contribution | Create five failure-mode tests for a confidential RAG demo: overbroad retrieval, prompt logging, citation leakage, attestation bypass, and answer exfiltration. |
