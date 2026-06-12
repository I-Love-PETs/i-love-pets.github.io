# Deployment Deep Dives

!!! warning "Deeper studies, same evidence discipline"
    These pages go further than the per-domain deployment summaries. Each one drills into a single named deployment, asks what was *actually* shipped, and separates verified facts from marketing language and open questions. Treat every claim by its labeled evidence level, not by the prestige of the organization behind it.

The [Deployments overview](../index.md) tracks PET deployments as a broad evidence base. This section zooms in. We pick four widely cited deployments that builders are repeatedly pointed to, and we interrogate each one against the same six questions:

1. **What was actually deployed** — system, parties, scale, timeframe.
2. **Maturity** — pilot, one-off study, production, or ongoing program. Be precise.
3. **Privacy claim** — the specific privacy property that was actually claimed.
4. **Limitations** — what the PET did *not* protect, and known criticisms.
5. **Builder lessons** — transferable, practical takeaways.
6. **What remains unclear** — open questions and unverified figures.

## Evidence Levels

Each major claim on these pages carries one of four labels. Today's reference date is 2026-06-10.

| Label | Meaning |
| --- | --- |
| Deployment-backed | Confirmed by primary deployment documentation, official reports, or the deploying party itself |
| Literature-backed | Supported by peer-reviewed papers or technical analyses, including independent ones |
| Expert judgment | A reasonable inference from how the technology works, not a directly sourced fact |
| Needs evidence | A figure or claim we could not verify against a primary source |

## Why These Four

The four studies were chosen because they span very different PET families, threat models, and maturity levels. Reading them side by side is more instructive than any single example.

| Deep dive | PET family | Maturity | Why it is worth studying |
| --- | --- | --- | --- |
| [US Census Differential Privacy](us-census-dp.md) | Differential privacy | Production, one release per decade | The largest-scale production DP deployment, with rich public criticism of the utility tradeoff |
| [Boston Wage-Gap MPC](boston-wage-gap-mpc.md) | Secure multi-party computation | Ongoing program, repeated since 2015 | A rare long-running civic MPC deployment where the hard part was trust and usability, not crypto |
| [Ads Data Hub & Clean Rooms](ads-data-hub-clean-rooms.md) | Aggregation plus query controls (clean room) | Commercial production | A dominant commercial pattern that is often loosely called "privacy-preserving" |
| [MELLODDY Federated Learning](melloddy-fl.md) | Federated learning plus secure aggregation | Completed consortium project | The largest cross-pharma FL experiment, instructive about what FL alone does and does not protect |

## How To Read These Pages

- A deployment existing is not the same as a deployment being independently evaluated.
- "Privacy-preserving" is a claim, not a proof. Always find the named protected artifact: inputs, outputs, identifiers, model updates, or none of them.
- One-off studies and decade-scale releases teach different lessons than always-on production systems. Maturity changes the engineering problem.
- External citations on these pages are evidence for you to check, not endorsements.
