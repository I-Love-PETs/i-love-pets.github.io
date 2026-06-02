# Evidence Policy

Decision support requires evidence. Qualitative claims are allowed, but the reader should be able to see how much confidence to place in them.

## Evidence Levels

| Level | Meaning | Example Use |
| --- | --- | --- |
| Measured | Backed by a benchmark with workload, environment, and date | Latency, throughput, cost, model accuracy |
| Deployment-backed | Backed by a named deployment, case study, incident, or postmortem | Operational lessons, integration failures, governance issues |
| Literature-backed | Backed by papers, standards, specifications, or technical reports | Security properties, known attacks, formal guarantees |
| Expert judgment | Editorial judgment from maintainers or contributors | Early guidance where public evidence is thin |
| Needs evidence | Useful claim that should not yet be treated as decision-grade | Open tradeoff assertions and suspected pain points |

## Claims That Need Evidence

Add evidence or mark uncertainty for claims about:

- Cost
- Latency
- Scalability
- Maturity
- Production readiness
- Security strength
- Privacy strength
- Common failure rates
- Tooling quality
- Regulatory acceptance

## Dated Claims

Fast-moving claims should include:

- `Last reviewed`
- Evidence date or source date
- Workload or environment if measured
- Scope of the claim
- What may have changed

## Wording Rules

Prefer:

> As of 2026, public benchmarks for this workload suggest...

Avoid:

> This PET is slow.

Prefer:

> This is an expert-judgment claim until benchmarked for the target workload.

Avoid:

> This is production-ready.

## Citation Standard

A citation should support the specific claim near it. A page-level reading list is not enough for decision support.

For benchmark claims, include workload, dataset or data shape, hardware, software versions, date, and what the benchmark does not cover.
