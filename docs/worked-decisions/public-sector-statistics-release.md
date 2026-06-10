# Worked Decision: Publishing Population Statistics Safely

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Figures are illustrative and labeled. Validate the privacy unit, budget, and small-cell behavior against the real tabulation plan and legal mandate before publication.

A public-sector agency must publish population statistics — counts and cross-tabulations by geography, age, and other attributes — for transparency, funding allocation, and research. The classic failure is publishing many overlapping tables, including small cells (e.g., "3 residents of a rare category in a small area"), and enabling re-identification by differencing those tables. The decision is how to publish *useful* statistics while making a *defensible* statement that individuals cannot be re-identified.

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | A population register or survey with per-person attributes; the agency will publish aggregate tabulations, often many, at varying geographic granularity. |
| Parties | The releasing agency, the public and researchers (data users), the individuals counted, and oversight bodies that may mandate both publication *and* confidentiality. |
| Constraints | Publication is often legally mandated, but so is confidentiality. Many tables are released and can be combined; small cells and differencing across tables are the core attack. Outputs are permanent once published. Utility must remain high enough for funding and research uses. |
| What success looks like | Statistics accurate enough for their public purpose, a documented and defensible privacy guarantee, controlled behavior on small cells, and a privacy budget that is owned and accounted for across the whole release — not improvised table by table. |

!!! note "The attack is differencing, not a single table"
    No single published table needs to be obviously revealing. Re-identification comes from *combining* many tables and exploiting small cells. The privacy design must reason about the whole release, not each table in isolation.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| Centralized differential privacy | The agency holds the data and adds calibrated noise to published statistics under a global privacy budget — the modern standard for defensible official statistics. The natural fit. |
| Small-cell suppression / thresholding | Withholding or coarsening cells below a minimum count. Long-standing practice; useful *alongside* DP, weak on its own. |
| Privacy budget accounting | Tracking total budget spent across all released tabulations so the guarantee holds for the whole release, not per table. The discipline that makes DP meaningful here. |
| Federated analytics / MPC | If the population data are split across agencies that cannot pool, these compute aggregates without centralizing. A different topology, kept for completeness. |
| DP query interface (alternative to bulk tables) | Serve statistics on demand with per-query DP and budget limits, instead of (or alongside) publishing fixed tables. |

## 3. Rejected Options

| Rejected option | Why rejected |
| --- | --- |
| **Publish raw tabulations with no protection** | The default historical practice and the source of the differencing/small-cell re-identification problem. Releasing many overlapping tables, including tiny cells, with no formal protection is rejected — it is exactly the failure mode this decision exists to prevent. |
| **Small-cell suppression alone** | Suppression and rounding help but do not provide a formal guarantee, and a determined analyst can often back out suppressed cells by differencing the surrounding published totals. Useful as a supporting control, rejected as the *sole* protection. |
| **Classic de-identification of microdata** | Releasing "anonymized" person-level records is repeatedly shown vulnerable to linkage. For a public statistical release, this is weaker than aggregate DP and ships individual records unnecessarily. Rejected. |
| **DP applied per table without a global budget** | The trap of adding DP "after launch" with no budget owner or accounting: independently noising each of many tables does not bound total leakage once an attacker combines them. DP without composition accounting gives a false sense of safety. Rejected — DP must be budgeted across the whole release. |
| **An arbitrarily large privacy budget for utility's sake** | A budget set so loose that noise is negligible technically "uses DP" while providing little real protection. Choosing the budget for utility optics rather than a defensible privacy unit is rejected. |

## 4. Final Recommendation

A centralized DP release with disciplined accounting:

1. **Define the privacy unit explicitly** — typically per person (or per household, if mandated). This is the foundation of any defensible claim.
2. **Adopt centralized differential privacy** for published statistics, with noise calibrated to the privacy unit and the sensitivity of each tabulation.
3. **Account for the privacy budget across the entire release.** Track total budget spent over all tables so the guarantee covers the combined publication, not each table alone. Name a **budget owner**.
4. **Keep small-cell suppression / coarsening as a supporting control**, especially for the most granular geographies — defense in depth alongside DP, not a substitute.
5. **Consider a DP query interface** for specialized or research demand, with per-query budget limits, instead of publishing ever more fixed tables.

Publish the privacy parameters and accounting approach so the guarantee is auditable. For the underlying mechanism family, see [DP Synthetic Data Release](../pet-patterns/dp-synthetic-data-release.md) (related DP tooling) and the broader [Benchmark Scorecards](../benchmarks/scorecards.md) for utility framing.

!!! tip "Budget first, tables second"
    Decide the total privacy budget and the privacy unit *before* deciding how many tables to publish. The number and granularity of releases must fit inside the budget — not the other way around.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | An external analyst combining published tables (and external data) to re-identify individuals via differencing and small cells; a curious researcher pushing a query interface to its limits. |
| Trust boundaries | The agency is trusted with the raw data (centralized DP). The boundary that matters is the *publication boundary* — once statistics are out, protection cannot be added retroactively. |
| What this design protects | With centralized DP and global budget accounting, the formal influence of any single individual on the *entire set* of published statistics is bounded. Suppression adds defense in depth for the smallest cells. |
| What is **not** protected | DP bounds individual influence but does **not** make outputs exact; users must accept noise. It does **not** protect against an attacker with auxiliary data drawing population-level inferences that are not about any one person. If the **budget is set too loosely** or accounting is wrong, the practical guarantee weakens sharply. Suppression alone is **differenceable**. Permanent publication means errors cannot be recalled. See [Inference Attacks](../threat-models/inference-attacks.md). |

!!! warning "Composition is where DP releases live or die"
    A correctly noised single table means little if dozens more are published against the same people without a shared budget. The guarantee is a property of the *whole release*. If you cannot account for total budget across all tabulations, you do not have the guarantee you think you have.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Privacy (formal) | Total privacy budget across the full release, and the privacy unit it protects | Needs evidence — must be set, owned, and reported |
| Composition correctness | Whether budget accounting actually covers all published tabulations and query access | Expert judgment (2026-06-10): the most common gap; audit it |
| Utility | Accuracy of key statistics vs. their public purpose (funding thresholds, research validity) | Expert judgment (2026-06-10): expect visible noise at fine geographies; quantify against use needs |
| Small-cell behavior | Re-identification risk at the smallest geographies/categories before and after suppression | Needs evidence — risk concentrates here |
| Differencing resistance | Whether combining released tables can recover suppressed or individual values | Needs evidence — red-team the release |
| Cost / effort | Tooling and methodological effort; stakeholder education on noisy outputs | Expert judgment (2026-06-10): communication and accounting effort often exceed the math |
| Permanence handling | Process to prevent erroneous or over-budget releases before they go public | Expert judgment (2026-06-10): a pre-publication gate is essential |

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| Population data are split across agencies that cannot pool | Move to **federated analytics or MPC** to compute aggregates without centralizing, then apply DP to the released results. |
| Users only need specific statistics on demand | Replace bulk table publication with a **DP query interface** under a budget cap — fewer tables, controlled composition. |
| Utility at fine geographies is unacceptable under a defensible budget | Coarsen geography/categories or reduce the number of releases to fit the budget; do not inflate the budget to rescue granularity. |
| Legal mandate fixes both the tables and the budget | Treat both as hard constraints and optimize utility within them; document any unavoidable residual risk. |
| Auxiliary-data linkage risk proves higher than assumed | Tighten the budget and strengthen suppression; revisit which attributes are published at all. |
| Stakeholders cannot accept noisy outputs | Invest in education and clear documentation of why exact publication is unsafe; exact tables are not a safe option here. |

!!! note "The honest summary"
    Safe statistical publication is a *composition* problem: the guarantee must hold across every table you release, not one at a time. Centralized DP with a named budget owner and real accounting provides a defensible claim; suppression is helpful backup, not the guarantee. Decide the budget and privacy unit before you decide how much to publish.
