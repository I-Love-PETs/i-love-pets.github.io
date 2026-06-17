# Boston Wage-Gap Study (Secure MPC)

!!! warning "Read the evidence levels"
    This is one of the few civic deployments of secure multi-party computation that has run repeatedly over many years. The hard part was not the cryptography. Reference date: 2026-06-10.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | Boston Women's Workforce Council (BWWC), with Boston University's Hariri Institute (Software and Application Innovation Lab, SAIL) |
| Domain | Public sector / civic data, labor economics |
| Problem | Measure the Greater Boston gender and racial wage gap from real employer payroll data without any party seeing an individual company's confidential payroll |
| PETs used | Secure multi-party computation (secret-sharing based secure summation / vector addition) |
| Deployment maturity | Ongoing program, run six times (2015, 2016, 2017, 2019, 2021, 2023) |
| Source quality | Primary / official plus third-party case study |
| Source | [UN Statistics Wiki case study](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020); [BWWC data privacy page](https://thebwwc.org/mpc) |

## What Was Actually Deployed

Employers that sign the BWWC's "100% Talent Compact" submit confidential payroll data (compensation broken out by gender, race, ethnicity, job category, and tenure, in EEO-1-style buckets). A browser-based tool secret-shares each employer's submission into two shares. One share goes to the BWWC and the other to the Boston University team; the BWWC computes the city-wide aggregate from its shares and learns only the summed/averaged statistics, while Boston University, as a compute party, sees neither the raw inputs nor the final outputs. The result is a city-wide wage-gap measurement that no single party could have produced from data it was allowed to see. *(Deployment-backed — [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020); [BU Hariri Institute](https://www.bu.edu/hic/2017/01/05/mayor-walsh-new-partnership-with-bu/).)*

Parties and trust model:

- **Input parties:** 100+ participating employers. *(Deployment-backed.)*
- **Compute / output party:** the BWWC (computes and receives the aggregate). *(Deployment-backed.)*
- **Compute party:** Boston University (sees neither inputs nor outputs). *(Deployment-backed.)*
- **Trust assumption:** participants trust BU and the BWWC to behave **semi-honestly** (honest-but-curious), with the ability to audit the open-source code. The protocol is **not** hardened against a fully malicious compute party. *(Deployment-backed — [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*

Scale across cycles (employer-reported payroll, not self-reported survey data):

| Report year | Companies / employers | Employees | Notes |
| --- | --- | --- | --- |
| 2016 | 69 | ~112,600 | First report; baseline. *(Deployment-backed — [BWWC](https://thebwwc.org/wage-gap-studies).)* |
| 2017 | 114 | ~166,700 | ~16% of Greater Boston workforce. *(Deployment-backed — [BU Hariri](https://www.bu.edu/hic/2018/01/31/mayor-walsh-bwwc-release-2017-wage-gap-report/).)* |
| 2019 | 123 | ~140,000 | *(Deployment-backed — [BWWC](https://thebwwc.org/wage-gap-studies).)* |
| 2021 | 134 | ~156,000 | ~$17.4B in annual wages. *(Deployment-backed.)* |
| 2023 | 103 | ~165,000 | ~17% of Greater Boston demographic. *(Deployment-backed — [BU Hariri](https://www.bu.edu/hic/2023/12/19/boston-womens-workforce-council-finds-30-percent-decline-gender-wage-gap/).)* |

The code is open source under the BU `multiparty` GitHub organization, which was central to the trust story. *(Deployment-backed — [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*

## Maturity

**Ongoing, genuinely repeated program — arguably the strongest "production civic MPC" example available.** The same platform has been run six times since 2015 on real payroll data, and the UN's privacy-preserving-techniques wiki classifies its implementation status as production. It has also been reused by other Boston-area non-profits (for example the Greater Boston Chamber of Commerce). This is meaningfully more mature than a one-off study, though it is a periodic batch measurement rather than an always-on service. *(Deployment-backed — [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*

## Privacy Claim

The claimed property is **input privacy via secure computation**: no party — not a competing employer, not the BWWC, not Boston University — learns any individual company's payroll, while the city-wide aggregate is computed correctly. The protected artifact is the **employer-level input**, under a semi-honest threat model with two non-colluding compute domains. *(Deployment-backed — [BU Hariri 2017 announcement](https://www.bu.edu/hic/2017/01/05/mayor-walsh-new-partnership-with-bu/).)*

## Limitations

What MPC did **not** protect, and the practical constraints:

- **The output is not differentially private.** MPC protects the *inputs* during computation; it says nothing about whether the published aggregate itself leaks information. Aggregates over coarse job/gender/race cells across 100+ large employers are low-risk, but the guarantee is about input confidentiality, not output privacy. *(Expert judgment, consistent with the protocol described in the [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*
- **Semi-honest, not malicious-secure.** The deployment assumes the two compute domains do not collude and follow the protocol. A malicious or colluding compute party is outside the threat model. *(Deployment-backed.)*
- **Garbage-in still applies, and is hard to fix.** Because inputs are encrypted/secret-shared, data-entry errors are very difficult to detect or correct after submission. The team had to push validation to the client (browser) side before secret-sharing. *(Deployment-backed — the BU team explicitly cites this as a lesson in the [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*
- **Coverage and selection bias.** Participants are self-selected Compact signers, roughly one in six area employees; the measurement is not a random sample of the regional economy. This is a methodology limit, not a PET failure, but it bounds what the numbers mean. *(Expert judgment, grounded in BWWC's own coverage statements.)*

## Builder Lessons

These are unusually concrete because the BU team published them directly. *(All Deployment-backed — [UN Statistics Wiki](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).)*

- **The bottleneck is rarely the crypto.** The team states plainly that the (in)efficiency of the MPC was inconsequential; the first cycle took nearly two years of discussions with employers, social scientists, and city officials. Runtime was a footnote.
- **MPC can be cheaper than finding a trusted third party.** The BWWC turned to MPC only after failing to recruit anyone willing to be the trusted custodian of competitors' payroll. Secure computation was "quicker, cheaper, and safer" than building that trust relationship.
- **Start small and explainable.** Pick one aggregate everyone wants, choose a semi-honest protocol that is easy to draw on a slide, keep the implementation small enough to audit, and pilot with fictitious or small-cohort data first.
- **Auditable open-source code is a trust instrument.** Making the protocol simple and the code public let IT staff, counsel, and executives verify the claim themselves, which mattered more than performance.
- **Bring usability and human-factors experts in from day one.** Privacy makes errors nearly unrecoverable, so the data-entry experience is a privacy-relevant design surface, not an afterthought.

## What Remains Unclear

- **Exact protocol parameters per cycle** (share counts beyond the two-domain split, any malicious-security hardening added in later years) are not fully specified in the public summaries we reviewed. *(Needs evidence.)*
- **Whether any formal output-privacy mechanism (for example DP on the published aggregates) was ever added** is not established by the sources here; the design we found protects inputs, not outputs. *(Needs evidence.)*
- **The most recent (2025) cycle's participation figures** were referenced by the BWWC but not captured in detail in the sources reviewed for this page. *(Needs evidence.)*

## Sources

- UN GWG on Big Data, Privacy-Preserving Techniques Wiki, [Boston Women's Workforce Council: Measuring salary disparity using secure multi-party computation](https://unstats.un.org/wiki/pages/viewpage.action?pageId=150012020).
- Boston Women's Workforce Council, [Data Privacy / MPC](https://thebwwc.org/mpc) and [Wage Gap Studies data](https://thebwwc.org/wage-gap-studies).
- BU Hariri Institute, [Mayor Walsh and BWWC Release 2016 Gender Wage Gap Report; New Partnership with BU](https://www.bu.edu/hic/2017/01/05/mayor-walsh-new-partnership-with-bu/).
- BU Hariri Institute, [Mayor Walsh and BWWC Release 2017 Wage Gap Report](https://www.bu.edu/hic/2018/01/31/mayor-walsh-bwwc-release-2017-wage-gap-report/).
- BU Hariri Institute, [The Boston Women's Workforce Council Finds a 30% Decline in the Boston Gender Wage Gap](https://www.bu.edu/hic/2023/12/19/boston-womens-workforce-council-finds-30-percent-decline-gender-wage-gap/).
