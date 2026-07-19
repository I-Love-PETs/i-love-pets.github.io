# By Threat Model

A PET recommendation without a threat model is a guess. Start by naming the adversary, what they can observe, what they can change, and what output they are allowed to learn.

## Threat-Model Matrix

| Threat model | Use this when... | PETs to consider | Caveat |
| --- | --- | --- | --- |
| Honest-but-curious coordinator | The coordinator follows the protocol but wants to inspect data or updates | FL + secure aggregation, MPC, HE, PSI, TEEs | Too weak if participants or operators can deviate |
| Malicious participant | A party may send bad inputs, poisoned updates, or adaptive queries | Malicious-secure MPC, robust FL, input validation, abuse monitoring | Stronger security usually increases cost and complexity |
| Colluding parties | Some parties may combine their views | Threshold MPC, secure aggregation with dropout thresholds, DP, audit controls | Write the exact collusion threshold; do not imply "no collusion" by silence |
| Curious platform operator | The cloud, clean-room, or model-service operator may inspect data | HE, MPC, TEEs with attestation | TEEs shift trust to hardware, firmware, supply chain, and attestation |
| Inference attacker | The output may reveal membership, attributes, or training examples | DP, output review, memorization testing, model auditing | Input protection does not prevent output leakage |
| Side-channel attacker | Timing, memory, cache, logs, or metadata can leak sensitive information | Constant-time crypto, hardened TEEs, metadata minimization | Expensive to reason about and easy to under-scope |
| External attacker | The system may be breached or misused | Security engineering, key management, least privilege, monitoring | PETs do not replace basic security controls |

## Use This When / Avoid This When

### Federated learning

Use this when the primary concern is **raw-data centralization** and participants can run local training.

Avoid this when the privacy claim is "the coordinator learns nothing." FL updates can leak information. Add secure aggregation and DP only after deciding how you will handle poisoning, debugging, and small rounds.

| Field | Guidance |
| --- | --- |
| Recommended PET | FL with secure aggregation for a curious coordinator; add DP for record-level output privacy. |
| Alternative PETs | Centralized training with governance, clean room training, MPC for analytics. |
| Why | The threat is raw-data centralization or coordinator update visibility, not every possible model leakage path. |
| Tradeoffs | Less central access, more distributed operations and harder debugging. |
| Failure modes | Update leakage, poisoning, non-IID underperformance, small-round exposure. |
| Operational considerations | Participant identity, round thresholds, update visibility policy, per-site evaluation, incident response. |

### Differential privacy

Use this when the concern is **individual contribution to an output**.

Avoid this when nobody can define the privacy unit, budget owner, neighboring dataset, or release accounting. "We used DP" is not meaningful without those choices.

| Field | Guidance |
| --- | --- |
| Recommended PET | DP on the released statistic, model, or synthetic data when contribution bounds are required. |
| Alternative PETs | Thresholds and governance for low-risk internal outputs; restricted access when utility cannot survive DP. |
| Why | The adversary learns from outputs, not just from input access. |
| Tradeoffs | Formal guarantee in exchange for utility loss, accounting work, and harder communication. |
| Failure modes | Wrong privacy unit, untracked composition, weak epsilon, hidden non-DP releases. |
| Operational considerations | Budget owner, release ledger, parameter review, utility gates, plain-language claim. |

### MPC

Use this when multiple parties need a joint computation without trusting one operator.

Avoid this when the parties cannot agree on identity, availability, protocol versioning, or collusion assumptions. MPC is a system, not only a protocol.

| Field | Guidance |
| --- | --- |
| Recommended PET | MPC when no single operator should see intermediate values in a joint computation. |
| Alternative PETs | Clean room if operator trust is acceptable; PSI if the computation is only matching; FL if the output is a trained model. |
| Why | The adversary is another party or operator that should not inspect private inputs. |
| Tradeoffs | Strong input privacy for agreed functions, but protocol operations and availability matter. |
| Failure modes | Unrealistic collusion assumptions, abort leakage, schema mismatch, output leakage. |
| Operational considerations | Party identity, protocol versioning, key setup, retry behavior, output approval. |

### Homomorphic encryption

Use this when a service must compute on encrypted inputs and the computation is narrow enough to benchmark.

Avoid this when the workload is arbitrary modern ML and nobody has checked supported operators, accuracy loss, ciphertext size, and latency.

| Field | Guidance |
| --- | --- |
| Recommended PET | HE for narrow computations where the service must not see plaintext inputs. |
| Alternative PETs | TEE for complex/low-latency inference, client-side inference, MPC for multi-party input. |
| Why | The adversary is the compute service or model host observing client features. |
| Tradeoffs | Strong input confidentiality with significant operator and performance constraints. |
| Failure modes | Unsupported operations, ciphertext expansion, latency misses, insecure key handling, output leakage. |
| Operational considerations | Model redesign, batching, key ownership, accuracy regression tests, p95/p99 latency. |

### TEEs

Use this when general-purpose confidential computation is needed and hardware trust is acceptable.

Avoid this when the design cannot explain attestation, side-channel assumptions, log handling, and what happens after the TEE emits an output.

| Field | Guidance |
| --- | --- |
| Recommended PET | TEEs when general-purpose confidential computation is needed and hardware trust is acceptable. |
| Alternative PETs | HE/MPC if the operator or hardware vendor is in scope; governed centralization if trust is acceptable. |
| Why | The adversary is an infrastructure operator or platform layer outside the confidential runtime. |
| Tradeoffs | Practical performance and workload breadth in exchange for hardware, firmware, attestation, and side-channel assumptions. |
| Failure modes | Unverified attestation, plaintext logs, vulnerable images, output leakage, side channels. |
| Operational considerations | Enclave image review, attestation verification, patching, support access, telemetry policy. |

### Synthetic data

Use this when users need a data-like artifact and you can evaluate privacy and utility directly.

Avoid this when the release needs a strong privacy claim but the generator is not DP or the team has no memorization test.

| Field | Guidance |
| --- | --- |
| Recommended PET | DP synthetic data for public or broad releases that require a formal claim. |
| Alternative PETs | DP query access, restricted sharing, non-DP synthetic data for internal prototyping. |
| Why | The adversary can inspect the released artifact and compare it with auxiliary data. |
| Tradeoffs | More release flexibility, but privacy-utility tension and harder documentation. |
| Failure modes | Memorized rare records, misleading utility, membership leakage, downstream misuse. |
| Operational considerations | Privacy budget, release review, memorization testing, utility benchmarks, data-use documentation. |

## Worked Example: Private RAG

An enterprise wants a chatbot over legal, finance, and HR documents. The initial proposal says "use a TEE so prompts and documents are private."

Threat-model review changes the design:

| Asset | Likely adversary | Control |
| --- | --- | --- |
| Document text | Model/runtime operator, unauthorized employees | Access control, TEEs, retrieval policy |
| User prompts | Platform operator, logs, support staff | Confidential runtime, log minimization, retention limits |
| Retrieved snippets | Authorized user with overbroad access | Policy engine, least-privilege retrieval, provenance |
| Generated answers | Any answer recipient | Output filters, citations, review for high-risk domains |
| Embeddings and metadata | Platform operator, search admins | Encryption, access controls, deletion workflows |

The TEE helps with runtime exposure, but it does not solve authorization or answer leakage. If all users and infrastructure are already inside one trusted boundary, ordinary RAG plus governance may be more honest.

## Threat-Model Caveats

- **Output leakage is central.** HE, MPC, FL, PSI, and TEEs can protect inputs while the final answer reveals sensitive facts.
- **Collusion assumptions must be explicit.** "Secure unless everyone colludes" and "secure unless one server colludes" are very different claims.
- **Small groups are dangerous.** Aggregate outputs can reveal individuals, hospitals, banks, or companies when cohorts are tiny.
- **Logs are part of the system.** Prompts, errors, metrics, traces, and support bundles often bypass the PET boundary.
- **Hardware trust is trust.** TEEs reduce who can inspect plaintext, but they do not remove dependence on hardware vendors, firmware, cloud configuration, and side-channel mitigations.
- **Governance can be the real problem.** A PET cannot fix unclear rights, weak incentives, or disagreement about acceptable use.

## Checklist

- Who can see inputs, intermediate values, logs, and outputs?
- Who can change inputs, code, policies, or model weights?
- Which parties may collude?
- What does the final output intentionally reveal?
- What side channels and metadata remain?
- What assumption would make the privacy claim false?
