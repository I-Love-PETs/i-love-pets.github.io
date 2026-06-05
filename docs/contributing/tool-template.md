# Tool Review Template

Use this template when reviewing a PET tool, library, platform, or service. Do not add a tool only because it exists.

```markdown
# Tool Name

## Evaluation Summary

| Field | Answer |
| --- | --- |
| What it helps build | Pattern, architecture, or use case |
| PET family | FL / DP / MPC / HE / TEE / synthetic data / clean room / other |
| Best fit | The narrow workload where the tool is strongest |
| Fit label | Strong fit / promising fit / narrow fit / poor fit / unknown fit |
| Evidence level | Measured / deployment-backed / literature-backed / expert judgment / needs evidence |

## What It Helps Build

Name the concrete pattern, architecture, or use case.

## Protected Assets

Inputs, updates, prompts, embeddings, outputs, logs, model weights, or other artifacts.

## Threat Model Support

Who is protected from whom? What adversaries are out of scope?

## Best Fit

Use this when...

## When Not To Use

Avoid this when...

## Privacy Claims

What claims does the tool make, and what evidence supports them?

## Benchmarks Or Evidence

Latency, cost, utility, security proof, deployment evidence, independent evaluation, or gaps.

## First Benchmark To Run

What should a reader measure before adopting this tool?

## Operational Notes

Setup, deployment, keys, logging, monitoring, upgrades, debugging, and failure recovery.

## Failure Modes

How can users misuse the tool or overclaim what it provides?

## Review Verdict

Recommend / watch / reject for the stated use case, with a short reason.

## Related Pages

Patterns, architectures, use cases, or threat models that help evaluate fit.
```

## Review Checklist

- Does the review explain fit rather than listing features?
- Are protected assets named?
- Are threat-model assumptions visible?
- Are benchmarks or evidence included?
- Does it say when not to use the tool?
- Are operational risks described?
- Is the first benchmark clear?
