# FL + Differential Privacy

## Goal

Train across silos while bounding the influence of individual records or participants.

## Actors

Participants, coordinator, privacy accountant, model evaluators, and model users.

## Data Flow

Local training clips updates, adds noise locally or centrally, aggregates updates, and tracks privacy spend across rounds.

## Trust Boundaries

Raw data remains local. The privacy accountant must cover all training releases, evaluation releases, and tuning loops.

## PET Stack

Federated learning, DP-SGD or participant-level DP, secure aggregation, privacy accounting, and memorization auditing.

## Deployment Notes

Publish the privacy unit, clipping strategy, noise scale, accounting assumptions, and utility impact.

## Tradeoffs

DP improves formal privacy but can reduce model quality, especially for small sites, rare classes, and non-IID data.

## Failure Modes

Unaccounted hyperparameter tuning, weak epsilon, local records duplicated across sites, and unclear privacy unit.
