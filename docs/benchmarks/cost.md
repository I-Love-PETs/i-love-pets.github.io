# Cost Benchmarks

!!! info "Review status"
    Last reviewed: 2026-09-16

    Evidence level: Expert judgment

    Source quality: Unsourced / illustrative

    Snapshot scope: Editorial measurement guidance. Validate the method and acceptance thresholds for your workload; examples are illustrative.

## Definition

Cost is the resources and operational effort needed to deliver an allowed output at the required utility and service level. Compare a complete task, such as one successful inference or one approved aggregate release, rather than a cryptographic operation alone.

## What to measure

| Dimension | Record |
| --- | --- |
| Latency and throughput | End-to-end p50/p95/p99, successful tasks per second, concurrency, timeouts |
| Compute | Client, server, and participant CPU/GPU time, memory, idle capacity |
| Bandwidth and storage | Bytes transferred, ciphertext expansion, retained artifacts, egress |
| Setup and integration | Engineering hours, model conversion, schema alignment, participant onboarding |
| Operations | Key management, attestation, monitoring, retries, recovery, support |
| Review | Human privacy/security review time and approval delays |

## Measurement methodology

1. Define the workload, allowed output, utility threshold, and latency target. Include a plaintext or trusted baseline for reference; state if it fails the required threat model.
2. Fix data size, model, number of parties, region, hardware, software versions, protocol/security parameters, batch size, and concurrency. Record the run date and price date separately.
3. Time from request creation to usable output, including encryption, transfer, queueing, computation, and decryption. Separate setup and cold-start runs from steady-state runs.
4. Repeat runs under representative load. Report sample count, latency distributions, errors, dropouts, retries, and successful throughput. Track resources on every party, not just the server.
5. Convert resource use to a stated currency and billing period. Report recurring costs separately from one-time engineering effort; show any amortization horizon and labor rate.

Use `cost per successful task = total recurring workload cost / successful tasks`. Include the cost of failed attempts in the numerator. Keep review hours visible even if you cannot assign a defensible monetary value.

## Worked comparison

!!! warning "Illustrative arithmetic, not a benchmark"
    Evidence level: Needs evidence. Source quality: Unsourced / illustrative. These invented monthly totals demonstrate accounting; they are not prices or performance claims for a PET or product.

Assume both candidates complete 100,000 inferences per month at an agreed utility threshold. Candidate B is assumed to meet an input-confidentiality requirement; the plaintext baseline does not. The assumed p95 latency limit is 300 ms.

| Item | Plaintext baseline | Candidate B |
| --- | ---: | ---: |
| Compute per month | €100 | €180 |
| Network and storage per month | €20 | €40 |
| Recurring operator time at assumed €50/hour | 2 hours = €100 | 4 hours = €200 |
| Total recurring cost | €220 | €420 |
| Cost per 1,000 successful inferences | €2.20 | €4.20 |
| Assumed p95 latency | 80 ms | 240 ms |
| One-time integration effort | 8 hours | 24 hours |

Candidate B adds €200 per month, or €2 per 1,000 successful inferences, under these assumptions. It passes the assumed latency limit. The cheaper baseline remains a cost reference, not an acceptable deployment option if it violates the threat model. The additional 16 integration hours are reported separately; amortizing them over 12 months at €50/hour would add about €66.67 per month.

## Pitfalls

- Comparing different batch sizes, utility levels, security parameters, or numbers of parties.
- Timing only server computation while excluding client work and network delay.
- Dividing by attempted requests when many attempts fail.
- Treating a cloud list price or a one-hour test as a monthly bill without utilization assumptions.
- Hiding onboarding, key rotation, human review, or incident response in an unexplained overhead percentage.

## Reporting

Include hardware, cloud region, protocol settings, model size, data size, number of parties, and retry behavior. Attach raw timings, resource totals, pricing assumptions, and exclusions to the [shared reporting template](scorecards.md#shared-reporting-template). Read cost alongside [utility](utility.md) and [privacy](privacy.md).
