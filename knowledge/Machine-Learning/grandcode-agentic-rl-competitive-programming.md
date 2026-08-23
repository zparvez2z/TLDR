---
source_url: https://arxiv.org/html/2604.02721v1
author: Xiaoya Li, Xiaofei Sun, Guoyin Wang, Songqiao Su, Chris Shum, Jiwei Li
source_date: 03-04-2026
date: 11-07-2026
source_type: research_paper
source_version: arXiv v1
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original arXiv HTML paper; this note summarizes the agentic RL system, evaluation claims, and caution points for personal learning.
difficulty: Advanced
tags: [machine-learning, llm-agents, reinforcement-learning, code-generation, competitive-programming, evaluation]
category_review: keep_in_machine_learning_as_agentic-code-note
---

# GrandCode: Agentic RL for Competitive Programming

## TL;DR

GrandCode is a multi-agent reinforcement-learning system for competitive programming. It combines specialized agents for solving, hypothesis generation, summarization, and test-case generation, then improves them through post-training and online test-time RL.

The paper’s strongest claim is that GrandCode ranked first in three live Codeforces rounds in March 2026.

## Problem

Competitive programming is difficult for AI systems because problems require:

- long-horizon reasoning;
- algorithm design;
- proof-like thinking;
- edge-case handling;
- efficient implementation;
- testing under strict time limits.

Single-pass code generation often fails because the model may produce plausible but incorrect solutions.

## Method

The system uses an agentic loop rather than one model call.

```text
hypothesis → solution → tests → feedback → refinement
```

Major components include:

- a **hypothesis model** that proposes structural ideas;
- a **main solver** that writes and reasons through solutions;
- a **summary model** that compresses long reasoning context;
- a **test-case generator** that searches for adversarial or edge cases;
- online and offline reinforcement-learning strategies.

The paper introduces **Agentic GRPO**, a reinforcement-learning variant designed for multi-stage agent rollouts with delayed rewards and off-policy drift.

## Evidence

The paper reports that GrandCode placed first in Codeforces Rounds 1087, 1088, and 1089 under live contest conditions. It also describes multiple system components: difficulty-based routing, adversarial test generation, test-time strategies, post-training, summarization, and RL infrastructure.

## Why it matters

This note is important for understanding agentic AI beyond simple prompting. GrandCode is an example of an AI system that combines:

- reasoning;
- verification;
- test generation;
- memory compression;
- reinforcement learning;
- orchestration across specialized modules.

## Limitations and caution

- The results are very strong, so reproducibility and independent verification matter.
- Competitive programming is a narrow but demanding domain; success there does not automatically imply general software-engineering reliability.
- System complexity is high, which makes attribution difficult: gains may come from model quality, orchestration, test-time compute, data, or RL.
- The note should be treated as a research summary, not proof that all coding tasks are solved.

## My takeaway

The main lesson is that strong code performance increasingly comes from systems, not only base models. Test generation, refinement loops, and reward design can be as important as the model itself.

## Related notes

- [InCoder-32B](incoder-32b-code-foundation-model-for-industrial-scenarios.md)
- [Reasoning Language Models](reasoning-language-models-a-blueprint.md)
- [Evaluation Is All You Need](evaluation-is-all-you-need-strategic-overclaiming-llm-capabilities.md)

## Source

Original source: https://arxiv.org/html/2604.02721v1
