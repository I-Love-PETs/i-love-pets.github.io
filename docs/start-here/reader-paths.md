# Reader Paths

This page gives a short, ordered reading sequence for five common intents. Follow the path that matches your immediate goal; you can branch to related sections at any point.

---

## I need to choose a PET

You have a real system, a data constraint, and a privacy requirement. You need a shortlist of candidates with reasons to accept or reject each.

1. [What Are PETs?](what-are-pets.md) — one-page orientation on what PETs do and do not guarantee.
2. [PET Taxonomy](pet-taxonomy.md) — families, properties, and relationships between PETs.
3. [Choose a PET](../pet-compass/choose-a-pet.md) — the primary guided chooser; answers depend on data movement and adversary.
4. [By Data Movement](../pet-compass/by-data-movement.md) — filter by where data lives and moves.
5. [By Threat Model](../pet-compass/by-threat-model.md) — filter by who must not learn what.
6. [Decision Tree](../pet-compass/decision-tree.md) — a readable branching checklist to confirm or challenge your shortlist.

---

## I need to design an architecture

You have a PET candidate and need to produce a defensible system design with actors, data flows, trust boundaries, and failure modes.

1. [What Are PETs?](what-are-pets.md) — confirm your candidate fits the protection goal.
2. [PET Architectures: Overview](../pet-architectures/index.md) — the catalogue of reference architectures.
3. Pick the architecture closest to your design (for example, [FL + Secure Aggregation](../pet-architectures/fl-secure-aggregation.md), [MPC Analytics Pipeline](../pet-architectures/mpc-analytics-pipeline.md), or [Confidential RAG](../pet-architectures/confidential-rag.md)).
4. [Threat Models: Overview](../threat-models/index.md) — map your adversary assumptions to the standard models.
5. [Benchmarks: Overview](../benchmarks/index.md) — decide what to measure before you build.

---

## I need to evaluate a claim

A paper, vendor, or colleague is making a privacy claim. You need to decide whether it is credible and what it actually protects.

1. [Glossary](glossary.md) — resolve any terms you are uncertain about.
2. [Evidence Policy](../project-standards/evidence-policy.md) — the standard of evidence this guide uses; apply the same bar to external claims.
3. [Claim Register](../project-standards/claim-register.md) — the live register of tracked claims; check whether the claim has already been assessed.
4. [Threat Models: Overview](../threat-models/index.md) — identify the adversary the claim assumes and what it does not cover.
5. [By Threat Model](../pet-compass/by-threat-model.md) — check whether the chosen PET matches the stated threat.

---

## I need a research problem

You want a concrete open problem with a clear gap, current workaround, success criteria, and a plausible first contribution.

1. [Fix My Itch: Overview](../fix-my-itch/index.md) — the full index of open problems by PET family.
2. [Good First Research Problems](../fix-my-itch/good-first-research-problems.md) — entry-level problems with lower coordination cost.
3. [Industry Pain Points](../fix-my-itch/industry-pain-points.md) — problems that practitioners have explicitly flagged as blockers.
4. [Benchmarks Needed](../fix-my-itch/benchmarks-needed.md) — measurement gaps where a new benchmark would have high impact.
5. Browse the PET-specific problem lists (e.g., [Federated Learning](../fix-my-itch/federated-learning.md), [Differential Privacy](../fix-my-itch/differential-privacy.md), [MPC](../fix-my-itch/mpc.md)) to find the family that interests you.

---

## I need evidence from deployments

You want to understand how a PET has performed in production, what the maturity level is, and what caveats remain unresolved.

1. [Evidence Policy](../project-standards/evidence-policy.md) — understand how deployment evidence is graded before reading the entries.
2. [Deployments: Overview](../deployments/index.md) — the full index of deployment write-ups, filtered by domain.
3. Browse by domain: [Healthcare](../deployments/healthcare.md), [Finance](../deployments/finance.md), [Advertising](../deployments/advertising.md), [Public Sector](../deployments/public-sector.md).
4. [Claim Register](../project-standards/claim-register.md) — cross-reference specific deployment claims that are under review.
5. [Benchmarks: Scorecards](../benchmarks/scorecards.md) — compare deployments on privacy, utility, and cost dimensions.
