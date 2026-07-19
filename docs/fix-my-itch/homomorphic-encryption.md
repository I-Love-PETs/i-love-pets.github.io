# Homomorphic Encryption

HE is compelling when a service must compute over encrypted inputs, but practical ML workloads are bounded by operator support, latency, ciphertext size, and model design.

## Research Handoff

| Problem | Who benefits if solved | Why it is difficult | Starting directions |
| --- | --- | --- | --- |
| Practical HE model architectures | Model providers, ML engineers, and buyers comparing private inference options | HE constraints interact with layers, activations, precision, batching, and accuracy | Benchmark small model families; publish unsupported operations; compare redesign cost |
| Debugging encrypted computation | ML engineers, incident responders, and HE library maintainers | Production failures can hide behind ciphertext, encoding, scaling, and approximation errors | Build plaintext shadow traces; publish test vectors; flag parameter drift and unsupported paths |
| HE inference benchmarks that matter | Buyers, benchmark maintainers, and vendors | One latency number rarely includes keys, transfer, batching, accuracy loss, and cloud cost | Report end-to-end measurements; compare HE, TEE, and plaintext baselines; include ciphertext size |
| Explaining HE failure early | Architects, sales engineers, and product teams | Teams often discover incompatibility only after model adaptation work has begun | Write model preflight analyzers; map layers to HE support; estimate latency bands before implementation |

## Practical HE Model Architectures

| Field | Card |
| --- | --- |
| Problem | What model architectures are actually practical for HE inference? |
| The itch | Teams hear that encrypted inference is possible, then discover their model uses layers, activations, or precision that are painful under HE. |
| Why it matters | Product teams need to know whether to redesign the model, switch PETs, or abandon private inference. |
| Current workaround | Use toy models, vendor demos, or late-stage prototypes. |
| Why the workaround is insufficient | It hides accuracy loss, batching constraints, and deployment cost. |
| What good progress would look like | A model catalog with supported operators, latency, accuracy, ciphertext size, and parameter choices for common tasks. |
| Difficulty | Medium |
| Good for | ML researcher, systems builder, cryptographer, benchmark maintainer |
| Related PETs | HE, private inference, TEEs |
| Possible first contribution | Benchmark three small architectures for tabular or image inference under one HE library and publish unsupported operations. |

## Debugging Encrypted Computation

| Field | Card |
| --- | --- |
| Problem | How can developers debug encrypted computation? |
| The itch | When encrypted inference returns the wrong answer, developers cannot inspect intermediate plaintext values in the deployed path. |
| Why it matters | Debuggability affects trust, incident response, and adoption by normal ML engineering teams. |
| Current workaround | Compare against plaintext simulations or ask cryptography specialists to inspect parameters. |
| Why the workaround is insufficient | It misses production-only failures such as encoding mistakes, scale drift, key handling bugs, and data distribution shifts. |
| What good progress would look like | Debug tooling that links encrypted traces to safe plaintext simulations, parameter warnings, and reproducible test vectors. |
| Difficulty | Hard |
| Good for | Systems builder, cryptographer, ML engineer |
| Related PETs | HE |
| Possible first contribution | Build a test harness that runs a plaintext shadow computation and reports where HE approximation error diverges. |

## HE Inference Benchmarks That Matter

| Field | Card |
| --- | --- |
| Problem | How can HE inference be benchmarked across latency, cost, and accuracy? |
| The itch | Benchmarks often report one impressive latency number without deployment context. |
| Why it matters | Buyers need to compare HE with TEEs, client-side inference, or standard hosted inference. |
| Current workaround | Vendor-specific demos and single-model papers. |
| Why the workaround is insufficient | It rarely captures batching, key setup, ciphertext transfer, accuracy loss, and cloud cost. |
| What good progress would look like | A benchmark format that reports end-to-end latency, throughput, ciphertext size, accuracy, parameter choices, and cost. |
| Difficulty | Good first research problem |
| Good for | Benchmark maintainer, systems builder, ML researcher |
| Related PETs | HE, TEEs, private inference |
| Possible first contribution | Create a reproducible benchmark for one tabular classifier comparing plaintext, TEE, and HE inference. |

## Explaining HE Failure Early

| Field | Card |
| --- | --- |
| Problem | How can tools tell teams early that HE is the wrong PET for a workload? |
| The itch | Engineers may spend weeks adapting a model before realizing the latency or operator set will not work. |
| Why it matters | Honest rejection criteria save time and reduce overclaiming. |
| Current workaround | Ask experts to review the model manually. |
| Why the workaround is insufficient | Expert review does not scale and may happen after sales or architecture commitments. |
| What good progress would look like | A preflight analyzer that flags unsupported layers, expensive operations, precision risks, and expected latency bands. |
| Difficulty | Medium |
| Good for | Systems builder, cryptographer, ML engineer |
| Related PETs | HE, private inference |
| Possible first contribution | Write a model-inspection script for one framework that maps layers to HE support and warnings. |
