---
source_url: https://arxiv.org/html/2604.02176v3
author: Hongyuan Adam Lu, Z.L., Victor Wei, Zefan Zhang, Zhao Hong, Qiqi Xiang, Bowen Cao, Wai Lam
source_date: 28-06-2026
date: 11-07-2026
source_type: research_paper
source_version: arXiv v3
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original arXiv HTML paper; this note summarizes the proposed frequency law, experiments, and limitations for personal learning.
difficulty: Advanced
tags: [machine-learning, llm, textual-frequency, prompting, fine-tuning, data-quality]
category_review: keep_in_machine_learning_as_llm-data-note
---

# Adam’s Law: Textual Frequency Law on Large Language Models

## TL;DR

This paper proposes the Textual Frequency Law: among paraphrases with the same meaning, the more frequent expression may work better for LLM prompting and fine-tuning.

The paper studies textual frequency as a data-quality signal for LLMs.

## Problem

Different prompts can have the same meaning but produce different model performance. The paper asks whether sentence-level textual frequency helps explain this.

Because LLM training data is often closed, the authors estimate textual frequency using online resources and generated corpora rather than direct training-set counts.

## Method

The paper proposes three connected ideas:

1. **Textual Frequency Law (TFL)**: prefer higher-frequency paraphrases when meanings are equivalent.
2. **Textual Frequency Distillation (TFD)**: use LLM-generated story completions to improve frequency estimates.
3. **Curriculum Textual Frequency Training (CTFT)**: fine-tune models in increasing order of sentence-level frequency.

The paper also introduces a Textual Frequency Paired Dataset (TFPD) for experiments.

## Evidence

The paper evaluates the idea on tasks including math reasoning, machine translation, commonsense reasoning, and agentic tool calling. The source reports that higher-frequency partitions often outperform lower-frequency versions and that CTFT helps in fine-tuning settings.

## Why it matters

This note is useful because it treats prompt wording and data wording as measurable signals, not just style choices.

For practical LLM work, the lesson is:

```text
meaning matters, but wording distribution can also matter
```

A model may respond better to common phrasing because it is closer to patterns seen during training.

## Limitations and caution

- The paper’s method depends on frequency estimation, not direct access to closed LLM training data.
- Paraphrasing can cause semantic drift, and the source explicitly notes this risk.
- Higher-frequency wording is not automatically better for every task or domain.
- The idea should be validated with task-specific evaluation before being used as a rule.

## My takeaway

Prompt quality is not only about clarity. It may also depend on how familiar the wording is to the model. However, preserving meaning is more important than blindly making text more common.

## Related notes

- [Introduction to Large Language Models](introduction-to-large-language-models.md)
- [LLM Evaluation Metrics](llm-evaluation-metrics-everything-you-need.md)
- [Evaluation Is All You Need](evaluation-is-all-you-need-strategic-overclaiming-llm-capabilities.md)

## Source

Original source: https://arxiv.org/html/2604.02176v3
