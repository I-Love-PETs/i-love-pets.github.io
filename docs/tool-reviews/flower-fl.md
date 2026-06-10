# Flower (`flwr`)

> Worked example applying the [tool evaluation framework](../contributing/tool-evaluation-framework.md) and [tool review template](../contributing/tool-template.md). Reviewed 2026-06-10. Not an endorsement.

## Evaluation Summary

| Field | Answer |
| --- | --- |
| What it helps build | [Cross-silo federated learning](../pet-patterns/cross-silo-federated-learning.md) and [federated analytics](../pet-patterns/federated-analytics.md): train or evaluate a model across data holders without centralising raw data |
| PET family | FL (orchestration framework; composes with DP and secure aggregation) |
| Best fit | A small-to-medium number of organisational silos, each keeping data local, coordinating a shared model with a custom strategy and any ML framework |
| Fit label | Strong fit (for FL orchestration) |
| Evidence level | Deployment-backed for orchestration maturity; Needs evidence for the privacy of raw model updates |

## What It Helps Build

Flower is a framework-agnostic orchestration layer for federated AI: federated learning, federated evaluation, and federated analytics. A central `ServerApp` coordinates rounds; each data holder runs a `ClientApp` that trains locally and returns model updates. It works with PyTorch, TensorFlow, scikit-learn, JAX, XGBoost, Hugging Face, and raw NumPy, and supports both a Simulation Engine (for experiments) and a Deployment Engine (for real federations) without code changes ([flower.ai docs](https://flower.ai/docs/framework/), [PyPI `flwr`](https://pypi.org/project/flwr/)).

It maps directly onto the [cross-silo FL pattern](../pet-patterns/cross-silo-federated-learning.md) and underpins the [FL + secure aggregation](../pet-architectures/fl-secure-aggregation.md) and [FL + differential privacy](../pet-architectures/fl-differential-privacy.md) architectures.

## Protected Assets

The protected asset is each silo's **raw training data**, which never leaves the silo. What *does* leave the silo are **model updates** (gradients or weights). This distinction is the whole review: Flower keeps data local, but model updates can leak training data through gradient-inversion and membership-inference attacks unless additional controls (secure aggregation, differential privacy) are layered on. Flower is the transport and orchestration; it is not, by itself, the privacy guarantee.

## Threat Model Support

- **Plain FedAvg in Flower**: protects against a naive "ship all the data to one place" design. It does **not** protect model updates from an [honest-but-curious](../threat-models/honest-but-curious.md) server, which sees every per-client update and can attempt [inference attacks](../threat-models/inference-attacks.md) or [membership inference](../threat-models/membership-inference.md).
- **Flower + SecAgg+**: Flower ships built-in Secure Aggregation via the SecAgg+ protocol (`SecAggPlusWorkflow` on the server, `secaggplus_mod` on the client), so the server sees only the **aggregate** of updates, not individual ones ([SecAgg+ example](https://github.com/flwrlabs/flower/tree/main/examples/flower-secure-aggregation)). This raises the bar against an honest-but-curious server and partially against [collusion](../threat-models/collusion.md), within the protocol's threshold assumptions.
- **Flower + central DP**: Flower provides components for central differential privacy with client-side clipping (e.g. the `fl-dp-sa` example combining DP and secure aggregation), bounding what any single client contributes to the released model ([Flower DP+SA example](https://flower.ai/docs/examples/fl-dp-sa.html)).
- **Out of scope**: a fully malicious server that can deviate arbitrarily from the protocol, poisoning/backdoor attacks by malicious clients, and side channels. Flower gives you the hooks; the threat-model guarantee comes from the protocol you compose, not the framework name.

## Best Fit

Use Flower when:

- you have a defined set of cooperating silos (hospitals, banks, business units) that cannot pool raw data;
- you want to keep your existing ML stack and bolt federation on;
- you need to prototype in simulation and then deploy the *same* code to a real federation;
- you are prepared to add SecAgg+ and/or DP yourself to protect updates.

## When Not To Use

Avoid, or look harder, when:

- you need a turnkey privacy guarantee out of the box. Plain Flower without SecAgg/DP exposes per-client updates;
- your adversary is a **malicious** server or you need robustness to model poisoning. Flower's built-in protocols target honest-but-curious settings;
- you have millions of unreliable edge devices and need Google-scale cross-device infrastructure. Flower supports large fleets but cross-device-at-massive-scale with carrier-grade reliability is a different operational problem;
- the workload is a one-off aggregate query better served by [MPC analytics](../pet-architectures/mpc-analytics-pipeline.md) or DP federated analytics.

## Privacy Claims

Flower's defensible claim is **orchestration plus optional privacy building blocks**: raw data stays local, and the framework provides SecAgg+ and DP integrations to protect updates. It does not claim that plain FedAvg is private. The maintainers' own tutorials flag "privacy and security in FL" as a topic requiring the extra mechanisms, which is the honest framing.

## Benchmarks Or Evidence

- **Maturity / adoption** (Deployment-backed): published on PyPI with status "5 - Production/Stable", Apache-2.0 licensed, with roughly 400k+ monthly downloads and active releases — v1.30.0 was released 2026-05-20 ([PyPI `flwr`](https://pypi.org/project/flwr/), [changelog](https://flower.ai/docs/framework/ref-changelog.html)). Origin is a University of Oxford research project; it is widely used in research and industry.
- **Privacy of updates** (Needs evidence): the *effectiveness* of SecAgg+ and DP for your specific model, data shape, and adversary is not something download counts demonstrate. There is no single number here; it must be measured per deployment.

## First Benchmark To Run

Per the framework's FL row: **non-IID cross-silo training with client dropouts, per-site utility, and an update-leakage review.**

1. Partition a representative dataset non-IID across the number of silos you actually expect.
2. Run FedAvg, then re-run with `SecAggPlusWorkflow` + `secaggplus_mod`, then add central DP with client-side clipping (start from the `fl-dp-sa` example).
3. Record per-site utility (not just global accuracy), convergence under simulated dropouts, and the DP `epsilon`/`delta` you actually spend.
4. Attempt a gradient-inversion or membership-inference probe against captured plain updates to confirm *why* you need SecAgg/DP, then confirm the aggregate-only path closes it.

## Operational Notes

- **Setup**: SuperLink (server) and SuperNode (clients) processes; recent versions add TLS for the AppIo APIs and token/HMAC-based authentication between components ([v1.29](https://flower.ai/blog/2026-04-12-announcing-flower-1.29-release)/[v1.30](https://flower.ai/blog/2026-05-20-announcing-flower-1.30-release) notes). Docker images are published.
- **Keys / transport**: enabling TLS and SuperNode authentication is a deliberate configuration step, not a default — budget for certificate management.
- **Upgrades**: Flower now enforces matching `major.minor` runtime versions across components, and v1.30 disallows manually launching internal `flwr-*` processes. Expect to upgrade server and clients in lockstep; cross-silo coordination of upgrades is a real operational cost.
- **Debugging**: the Simulation Engine lets you reproduce issues locally before touching the real federation, which is a genuine operational advantage.

## Failure Modes

- Shipping plain FedAvg and *calling it private* because "the data stayed local" — the classic overclaim this review exists to prevent.
- Assuming SecAgg+ protects against a malicious server or against collusion above its threshold; it does not.
- Setting DP clipping/noise to make benchmarks look good and quietly spending an `epsilon` that provides little real protection.
- Running without TLS/auth in a deployment because the simulation worked without them.

## Review Verdict

**Recommend (watch the privacy layer).** For the cross-silo FL pattern, Flower is a strong, mature, framework-agnostic orchestration choice and is a defensible default for this guide. The recommendation is explicitly conditional: Flower earns "recommend" as *orchestration*, but the privacy of model updates depends entirely on composing SecAgg+ and/or DP and measuring them — that part is "watch / needs evidence" until you benchmark it for your own deployment.

## Related Pages

- Pattern: [Cross-Silo Federated Learning](../pet-patterns/cross-silo-federated-learning.md)
- Pattern: [Federated Analytics](../pet-patterns/federated-analytics.md)
- Architecture: [FL + Secure Aggregation](../pet-architectures/fl-secure-aggregation.md)
- Architecture: [FL + Differential Privacy](../pet-architectures/fl-differential-privacy.md)
- Threat models: [Honest-But-Curious](../threat-models/honest-but-curious.md), [Membership Inference](../threat-models/membership-inference.md)
- Itch: [Federated Learning](../fix-my-itch/federated-learning.md)
