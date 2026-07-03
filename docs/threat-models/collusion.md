# Collusion

Collusion occurs when parties that are treated as separate in the design combine information.

## Practical Example

Two MPC compute parties share their views, violating the threshold assumption that protected the inputs.

## Questions To Ask

- Which parties can collude before privacy breaks?
- Is the platform operator separate from the analyst?
- Can participants compare outputs across repeated queries?
- Are legal and technical separation assumptions aligned?

## PET Implications

Secure aggregation, MPC, clean rooms, and TEEs all need explicit collusion assumptions.

## Write The Threshold Down

Do not say "parties do not collude" unless there is a control that makes that
credible. Write the smallest collusion set that breaks privacy, then check
whether the business arrangement, infrastructure, and incident response plan make
that threshold realistic.

| System | Collusion question |
| --- | --- |
| Secure aggregation | How many participants, coordinator components, or key servers must cooperate to reveal an update? |
| MPC | Which compute parties can share views before inputs are exposed? |
| Clean room | Can the platform operator and analyst combine logs, query history, and outputs? |
| Confidential computing | Can the cloud operator, workload owner, and attestation verifier bypass separation in practice? |
