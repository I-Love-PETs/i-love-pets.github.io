# Choose a PET

## If Data Cannot Move

Use **federated learning** when the output is a trained model and participants can run local training.

Use **federated analytics** when the output is aggregate measurement rather than a model.

Use **MPC** when multiple parties need a joint computation and do not want to trust one platform operator.

Use **HE** when a service must compute over encrypted inputs and the workload is narrow enough to afford the cost.

Use **TEEs** when general-purpose confidential computation is needed and hardware trust is acceptable.

Use **clean rooms** when governance, auditing, and platform workflows are as important as cryptographic controls.

## If Formal Privacy Guarantees Are Required

Use **differential privacy** when the output must limit the influence of any single person or record.

DP is often the guarantee layer rather than the whole architecture. It can sit on top of federated analytics, model training, synthetic data, or clean-room outputs.

## If Encrypted Inference Is Needed

Use **homomorphic encryption** when the provider must not see plaintext inputs.

Use **confidential inference** with TEEs when performance, model complexity, or operational simplicity matters more than avoiding hardware trust.

## If Safer Sharing Is Needed

Use **synthetic data** when downstream users need data-like artifacts for testing, prototyping, education, or analysis.

Use **DP synthetic data** when the release needs a formal individual privacy claim.

## Tradeoff Table

| PET | Privacy Strength | Utility Risk | Cost | Operational Complexity |
| --- | --- | --- | --- | --- |
| FL | Medium without add-ons | Medium | Medium | High |
| DP | High if parameterized well | Medium to high | Low to medium | Medium |
| MPC | High for inputs | Low to medium | Medium to high | High |
| HE | High for encrypted inputs | Medium | High | High |
| TEE | Medium to high under hardware trust | Low | Medium | Medium |
| PSI | High for nonmatches | Low | Low to medium | Medium |
| Synthetic data | Low to high depending on method | Medium | Medium | Medium |
| Clean room | Governance-dependent | Low to medium | Medium | Medium |
