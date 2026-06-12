# US Census Bureau 2020 Differential Privacy

!!! warning "Read the evidence levels"
    This is the largest production differential privacy deployment to date, and also one of the most publicly contested. Verified facts and disputed criticisms are both labeled below. Reference date: 2026-06-10.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | U.S. Census Bureau, 2020 Decennial Census Disclosure Avoidance System (DAS) |
| Domain | Public sector / official statistics |
| Problem | Publish detailed population tables down to the census-block level while provably limiting what any attacker can reconstruct about individual respondents |
| PETs used | Differential privacy via the TopDown Algorithm (TDA), using zero-concentrated differential privacy (zCDP) for privacy-loss accounting |
| Deployment maturity | Production, single decennial release (one-off cadence, repeats each decade) |
| Source | [Census Bureau working paper: The 2020 Census DAS TopDown Algorithm](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html) |

## What Was Actually Deployed

The Census Bureau replaced its long-standing disclosure-avoidance methods (swapping and suppression) with a formal differential privacy system for the 2020 Decennial Census. The core engine is the **TopDown Algorithm (TDA)**: it ingests the edited confidential census data, generates noisy versions of key queries ("measurements") using zero-concentrated differential privacy, then runs a post-processing optimization that distributes counts top-down through the geographic hierarchy (nation to state to county and on down to block) so that the released tables are internally consistent and non-negative. *(Deployment-backed — [Census working paper CED-WP-2022-002](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*

Scale and timeframe:

- **Geographic reach:** the entire United States, down to the census block, the finest published geography. *(Deployment-backed.)*
- **First production output:** the P.L. 94-171 redistricting data files were released in **August 2021** using the TDA. *(Deployment-backed — Census release schedule and [TDA working paper](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*
- **Privacy-loss budget for redistricting data:** the Bureau set a total of **epsilon = 17.14 for persons and epsilon = 2.47 for housing units** (expressed via the zCDP-to-epsilon conversion the Bureau published). *(Deployment-backed — reported in [Census documentation](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html); note that a single global epsilon is a simplification of the Bureau's per-geography-level allocation.)*

A defining design choice is the use of **invariants**: certain statistics the Bureau decided, as a matter of policy, to release exactly with no noise. State-level total population counts are invariant (a constitutional requirement for apportionment), as are the total number of housing units and group-quarters facilities by type. Everything outside the invariant set is noised. *(Deployment-backed — [TDA working paper](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*

## Maturity

**Production, but with a once-per-decade cadence.** This is not a pilot. The 2020 redistricting and demographic files are the official, legally operative census products. However, "production" here does not mean "continuously operated service." The DAS ran essentially once for the 2020 cycle, after multiple research demonstrations on 2010 data, and will be re-tuned before 2030. That cadence matters: there was effectively one shot to get parameters right, with limited ability to iterate against live feedback. *(Expert judgment, grounded in [Census documentation](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*

## Privacy Claim

The claimed property is **differential privacy with a published, accountable privacy-loss budget**. Concretely, the Bureau accounts for privacy loss using zero-concentrated differential privacy and publishes the total budget and its allocation across geographic levels and query types. The motivating threat is the **database reconstruction theorem**: the Bureau's own internal experiments indicated that the volume of exact tabulations historically published could be combined to reconstruct and re-identify a meaningful share of individual records, which is what formal DP is meant to bound. *(Deployment-backed for the mechanism; the reconstruction motivation is documented by the Bureau and discussed in [the academic literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/).)*

Two honest caveats on the claim itself:

- The guarantee applies to the **noised** statistics. Invariant quantities (for example, state total population) are released exactly and are explicitly **outside** the privacy-loss accounting. *(Deployment-backed.)*
- A single epsilon number is not directly comparable to epsilon values from other systems, because the per-query allocation, the unit of privacy, and the use of invariants all change what the number means. *(Expert judgment.)*

## Limitations

What DP did **not** do, and the criticisms it drew:

- **It did not protect invariants.** State totals and several housing/group-quarters counts are exact by design, so no privacy is claimed for them. *(Deployment-backed.)*
- **Small geographies and small subgroups absorb disproportionate relative error.** Independent analyses found the noise introduces larger *relative* discrepancies for small areas and for some racial and ethnic subgroups and rural populations, even though absolute error is bounded. *(Literature-backed — [Harvard DAS evaluation, Kenny et al.](https://redistrictingonline.org/wp-content/uploads/2021/03/MA-Harvard-DAS-Evaluation-052821.pdf); a peer-reviewed analysis of disproportionate discrepancies appears in [PMC11105149](https://pmc.ncbi.nlm.nih.gov/articles/PMC11105149/).)*
- **Post-processing can introduce bias.** Enforcing non-negativity and hierarchical consistency is not a neutral operation; it can systematically push small counts upward and distort the distribution in ways that are hard to model. *(Literature-backed — discussed by [Kenny et al.](https://redistrictingonline.org/wp-content/uploads/2021/03/MA-Harvard-DAS-Evaluation-052821.pdf) and in [the redistricting case study, PMC8494446](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/).)*
- **Redistricting and Voting Rights Act analysis concerns.** Critics argued the noise could complicate "one person, one vote" compliance and analysis of minority voting power at fine geographies. Advocacy groups raised specific concerns about Latino, Asian American, and Native American counts. *(Literature-backed / advocacy — [Advancing Justice AAJC preliminary report](https://www.advancingjustice-aajc.org/report/preliminary-report-impact-differential-privacy-2020-census-latinos-asian-americans).)*
- **Litigation.** The State of Alabama sued to block the use of differential privacy (and the timing of releases), arguing it impaired the state's ability to draw lawful districts. The differential-privacy theory met substantial skepticism and did not prevail in halting the method. *(Deployment-backed — court filings in [Alabama v. U.S. Dept. of Commerce, M.D. Ala. 3:21-cv-00211](https://storage.courtlistener.com/recap/gov.uscourts.almd.75040/gov.uscourts.almd.75040.27.0.pdf).)*

A fair counter-point: several independent statisticians concluded that for many *aggregate* redistricting uses the practical impact was modest, while agreeing the impact concentrates in the smallest units. The disagreement is largely about whether that concentrated error is tolerable, not about whether it exists. *(Literature-backed — [Kenny et al.](https://redistrictingonline.org/wp-content/uploads/2021/03/MA-Harvard-DAS-Evaluation-052821.pdf).)*

## Builder Lessons

- **Formal privacy forces an explicit, public utility tradeoff.** The Census fight is what honest DP looks like at scale: you must publish the budget, and stakeholders can then argue about it. That transparency is a feature, but be ready for the argument.
- **Invariants are a pragmatic escape hatch with a cost.** Releasing some quantities exactly preserved critical legal correctness, but every invariant is a hole in the guarantee and can leak information that interacts with the noised release. Name your invariants explicitly.
- **Post-processing is part of your privacy and utility story.** Non-negativity and consistency constraints change the error distribution. Do not treat post-processing as a cosmetic final step; analyze its bias.
- **Small cells are where DP hurts most.** If your use case depends on accurate counts for tiny populations, budget, parameterize, and communicate for that case specifically, or reconsider whether the data should be published at that granularity at all.
- **A single epsilon is not a portable quality score.** Document the unit of privacy, the allocation, and the invariants. An epsilon without that context is close to meaningless for comparison.

## What Remains Unclear

- **The exact 2030 parameters and design are not settled** as of the 2026-06-10 reference date; the Bureau has signaled changes after the 2020 experience, but specifics may evolve. *(Needs evidence.)*
- **The "right" epsilon was, and remains, a policy judgment, not a derived constant.** There is no consensus figure; the 17.14 / 2.47 split reflects the Bureau's negotiated balance, not an objective optimum. *(Expert judgment.)*
- **Real-world harm from the residual error is genuinely contested.** Studies disagree on how much the documented small-area distortions changed actual districting or funding outcomes, partly because counterfactuals are hard to construct. *(Literature-backed that the dispute exists; the magnitude of practical harm is Needs evidence.)*

## Sources

- U.S. Census Bureau, [The 2020 Census Disclosure Avoidance System TopDown Algorithm](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html) (working paper, 2022).
- Kenny, Kuriwaki, McCartan, Rosenman, Simko, Imai, [The Impact of the U.S. Census Disclosure Avoidance System on Redistricting and Voting Rights Analysis](https://redistrictingonline.org/wp-content/uploads/2021/03/MA-Harvard-DAS-Evaluation-052821.pdf).
- [The use of differential privacy for census data and its impact on redistricting](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/) (PMC8494446).
- [The 2020 US Census Differential Privacy Method Introduces Disproportionate Discrepancies](https://pmc.ncbi.nlm.nih.gov/articles/PMC11105149/) (PMC11105149).
- Asian Americans Advancing Justice AAJC, [Preliminary Report: Impact of Differential Privacy and the 2020 Census on Latinos, Asian Americans and Redistricting](https://www.advancingjustice-aajc.org/report/preliminary-report-impact-differential-privacy-2020-census-latinos-asian-americans).
- [Alabama v. U.S. Dept. of Commerce, M.D. Ala., No. 3:21-cv-00211, court filing](https://storage.courtlistener.com/recap/gov.uscourts.almd.75040/gov.uscourts.almd.75040.27.0.pdf).
