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

## Source Quality Labels

Evidence level says what kind of support a claim has. Source quality says how much independence and context the source provides.

| Label | Meaning | Good use | Caveat |
| --- | --- | --- | --- |
| Primary / official | Documentation, report, paper, or data from the deploying organization, standards body, regulator, or project team | Establish what was shipped, what parameters were claimed, and what the operator says the system does | May omit failures, user impact, or independent validation |
| Peer-reviewed / academic | Journal, conference, or technical paper with methods and results | Support measured results, attack claims, and limitations with methods attached | May still be a research prototype rather than a production deployment |
| Independent analysis | Evaluation by a party not operating or selling the system | Check utility impact, risk, criticism, and external validity | Methods, incentives, and data access still need review |
| Vendor case study | Marketing, customer story, or product documentation from a vendor or platform operator | Identify candidate deployments and product controls | Do not treat as independent proof of maturity, utility, or privacy |
| Press / secondary | News, blog coverage, analyst write-up, or conference report | Background and leads to primary sources | Use only when primary evidence is unavailable, and label the uncertainty |
| Unsourced / illustrative | Maintainer-created example or value with no supporting measurement | Teaching examples and benchmark templates | Never use as decision evidence |

Use both labels together when needed:

> *(Evidence: Deployment-backed. Source quality: Vendor case study. Reviewed 2026-06-17 — product documentation confirms the control exists, but no independent production evaluation was found.)*

For organizational privacy-risk language, align with the NIST Privacy Framework's
risk-management framing rather than treating PET use as a standalone assurance
claim. See NIST, [Privacy Framework](https://www.nist.gov/privacy-framework).

## Deployment Maturity Labels

Deployment maturity is separate from source quality. A production system can still be supported only by vendor documentation, and a peer-reviewed paper can still describe only a prototype.

| Label | Meaning |
| --- | --- |
| Production | Used in a live public, commercial, clinical, civic, or institutional workflow |
| Production, batch / periodic | Used in a real workflow, but run as a periodic release or recurring study rather than an always-on service |
| Pilot | Tested with real organizations or real data, but not clearly sustained as a production workflow |
| Demonstration experiment | Tested with real partners or realistic data to prove feasibility; operational adoption is not established |
| Research prototype | Published experiment, demo, or study; may use real data but is primarily research evidence |
| Vendor case study | Deployment described mainly by a vendor, platform operator, or customer story; maturity may be real but independently thin |
| Proposed use case | Plausible application with no named deployment evidence on the page |
| Unclear | Public sources do not provide enough detail to classify maturity |

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

## Resolved and Unresolved Claim Status

Each entry in the [Claim Register](claim-register.md) carries a **Resolved** or **Unresolved** status. A claim is **Resolved** when sufficient evidence has been identified or the claim has been narrowed and labelled so readers can calibrate their confidence (inline notes are in place on the relevant pages). A claim is **Unresolved** when it remains too broad, too vague, or unsourced for decision use. The register records a dated note explaining what evidence was found or what is still missing. Status is re-evaluated on each editorial pass; inline evidence notes on content pages use the form `*(Evidence: <level>, <date> — <one-line note>.)*`.

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
