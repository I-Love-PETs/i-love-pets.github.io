# Evidence Policy

Decision support requires evidence. Qualitative claims are allowed, but the reader should be able to see how much confidence to place in them.

## Evidence Levels

| Level | Meaning | Use for | Required context |
| --- | --- | --- | --- |
| Measured | Backed by a benchmark with workload, environment, and date | Latency, throughput, utility, cost, leakage tests | Workload, data shape, hardware/software, date, limits |
| Deployment-backed | Backed by a named deployment, case study, incident, or postmortem | Operational lessons, integration failures, governance issues | Organization/project, maturity, source, caveats |
| Literature-backed | Backed by papers, standards, specifications, or technical reports | Security properties, known attacks, formal guarantees | Source, scope, assumptions, date where relevant |
| Expert judgment | Editorial judgment from maintainers or contributors | Early guidance where public evidence is thin | Why the judgment is plausible and what would change it |
| Needs evidence | Useful claim that should not yet be treated as decision-grade | Open tradeoff assertions and suspected pain points | What evidence would make the claim usable |

## Claim States

Use these labels when reviewing pages:

| State | Meaning | Action |
| --- | --- | --- |
| Decision-grade | Claim is scoped and supported enough for practical use | Keep dated and linked |
| Usable with caveat | Claim is useful but has workload or maturity limits | State caveat next to claim |
| Expert judgment | Claim is maintainer judgment, not sourced evidence | Mark explicitly and add to claim register if important |
| Needs evidence | Claim is plausible but not yet reliable | Soften wording and add needed evidence |
| Too broad | Claim is true only in some settings | Narrow the claim before sourcing |
| Remove | Claim is generic, unsupported, or not decision-relevant | Delete it |

## Claims That Need Evidence

Add evidence or mark uncertainty for claims about:

- cost;
- latency;
- scalability;
- maturity;
- production readiness;
- security strength;
- privacy strength;
- common failure rates;
- tooling quality;
- regulatory acceptance.

## Dated Claims

Fast-moving claims should include:

- `Last reviewed`;
- evidence date or source date;
- workload or environment if measured;
- scope of the claim;
- what may have changed.

Use this metadata block for fast-moving decision pages:

```markdown
!!! info "Review status"
    Last reviewed: 2026-06-05
    Evidence level: Expert judgment
    Snapshot scope: Public guidance and examples available at review time.
```

## Wording Rules

Prefer:

> As of 2026, public benchmarks for this workload suggest...

Avoid:

> This PET is slow.

Prefer:

> This is an expert-judgment claim until benchmarked for the target workload.

Avoid:

> This is production-ready.

Prefer:

> This protects inputs from the model service under the stated key-management assumptions.

Avoid:

> This protects user privacy.

## Citation Standard

A citation should support the specific claim near it. A page-level reading list is not enough for decision support.

For benchmark claims, include workload, dataset or data shape, hardware, software versions, date, and what the benchmark does not cover.

For deployment claims, include maturity: production, pilot, research prototype, or unclear.

## Review Workflow

1. Find claims that affect a PET choice.
2. Narrow claims until the protected asset, adversary, workload, and output are clear.
3. Assign an evidence level and claim state.
4. Add a source, benchmark, deployment entry, or caveat.
5. Add unresolved high-impact claims to the [Claim Register](claim-register.md).
