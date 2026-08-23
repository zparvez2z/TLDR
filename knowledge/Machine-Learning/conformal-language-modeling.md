---
source_url: https://arxiv.org/html/2306.10193
author: Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi Jaakkola, Regina Barzilay
date: 04-05-2026
source_type: research_paper
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original arXiv HTML paper; this note summarizes the paper's method and guarantees for personal learning.
difficulty: Advanced
tags: [machine-learning, llm, conformal-prediction, uncertainty, hallucination, evaluation]
---

# Conformal Language Modeling

## TL;DR

This paper adapts conformal prediction to language models. Instead of returning only one generated answer, the method builds a set of candidate answers with a statistical guarantee that at least one acceptable answer is included with high probability.

It is about uncertainty, reliability, and reducing hallucination risk in generative language outputs.

## Problem

Language models generate open-ended text from a huge output space. Standard conformal prediction is difficult because we cannot enumerate all possible outputs.

Also, one generated answer can mix correct and incorrect parts. A long answer may contain some valid sentences and some hallucinated ones.

## Core idea

The method samples candidate outputs from a language model and uses a calibrated stopping rule.

```text
sample outputs → keep acceptable/diverse candidates → stop when coverage guarantee is met
```

The goal is not to prove that every candidate is correct. The goal is to produce a set that likely contains at least one acceptable response.

## Method

The paper introduces:

- a calibrated stopping rule for deciding when enough candidates have been sampled;
- a rejection rule for removing low-quality, redundant, or weak candidates;
- conformal guarantees for the final candidate set;
- component-level analysis to identify correct parts of long outputs, such as phrases or sentences.

## Evidence

The paper evaluates the method on tasks such as open-domain question answering, text summarization, and radiology report generation.

The results show that desired coverage levels can often be achieved with a limited number of samples.

## Why it matters

This is useful because LLMs often give one fluent answer even when uncertainty is high. A conformal approach can expose uncertainty more explicitly by returning a reliable set of candidates or identifying which parts of an answer are more trustworthy.

## Limitations

- The method depends on calibration data and admission functions that define what counts as acceptable.
- Returning a set of answers may be less convenient than returning one answer.
- More sampling increases computation cost.
- Formal guarantees depend on assumptions behind conformal prediction and the calibration setup.
- This is not a complete solution to hallucination.

## My takeaway

Conformal language modeling is a way to make LLM output less overconfident. Instead of pretending one answer is certainly correct, it gives a controlled way to represent uncertainty.

## Related notes

- [LLM Evaluation Metrics](llm-evaluation-metrics-everything-you-need.md)
- [Evaluation Is All You Need](evaluation-is-all-you-need-strategic-overclaiming-llm-capabilities.md)
- [Introduction to Large Language Models](introduction-to-large-language-models.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)

## Source

Original source: https://arxiv.org/html/2306.10193
