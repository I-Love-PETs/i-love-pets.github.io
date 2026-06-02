# Private LLM Fine-Tuning

## Problem

A team wants to adapt a language model using sensitive examples, traces, or documents.

## When To Use

Use this pattern when fine-tuning data is sensitive and the adapted model may be shared, queried broadly, or deployed by a third party.

## When Not To Use

Avoid fine-tuning when retrieval, prompting, redaction, or smaller task-specific models can meet the need with lower privacy risk.

## Typical Architecture

Prepare and minimize training data, train with privacy controls, audit memorization, evaluate utility, and constrain deployment access.

## Threat Model

Attackers may query the model, inspect weights, infer membership, or extract memorized training text.

## Privacy Properties

DP-SGD can bound record influence. TEEs can protect training execution. Neither removes the need to audit outputs and memorization.

## Tools And Building Blocks

DP-SGD, data redaction, confidential training, secure aggregation, evaluation harnesses, canary tests, and model access controls.

## Common Failure Modes

Training-data memorization, weak DP accounting, overbroad data collection, untested extraction risk, and unclear retention.

## Open Research Problems

DP for LLM utility, privacy auditing, memorization detection, and composable guarantees across RAG plus fine-tuning.

## Related Pages

Federated RAG, DP for LLMs, membership inference.
