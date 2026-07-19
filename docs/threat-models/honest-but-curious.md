# Honest-But-Curious

An honest-but-curious party follows the protocol but tries to learn extra information from messages, metadata, or outputs.

## Practical Example

A federated learning coordinator aggregates updates correctly but inspects individual updates for signals about a hospital's patient population.

## Good Fit

This model is useful for early designs, mutually governed collaborations, and systems where protocol deviation is unlikely.

It is also useful as a narrow review step: first ask whether a party can learn too
much while following the rules, then separately ask whether the rules are
enforceable.

## Limits

It does not cover malformed inputs, poisoning, selective aborts, query abuse, or compromised participants.

## PET Implications

MPC, PSI, HE, secure aggregation, and clean rooms often start here. Add stronger controls when incentives are not aligned.

## Review Questions

- What messages, outputs, logs, and metadata does the curious party see?
- Can the party repeat the protocol with slightly changed inputs or cohorts?
- Does the claim still hold if the party combines protocol views with auxiliary data?
- Which controls become mandatory if this party stops following the protocol?
