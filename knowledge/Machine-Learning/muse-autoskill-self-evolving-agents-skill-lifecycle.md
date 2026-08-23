---
source_url: https://arxiv.org/html/2605.27366v2
author: Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang
date: 21-07-2026
source_type: research_paper
source_version: arXiv v2
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original arXiv HTML paper; this note summarizes the framework, experiments, and limitations for personal learning.
difficulty: Advanced
tags: [machine-learning, llm-agents, skills, agent-memory, self-improvement, evaluation]
---

# MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

## TL;DR

MUSE-Autoskill is a framework for LLM agents that treats skills as long-lived, reusable, testable assets. Instead of using skills as static prompt snippets, MUSE creates, stores, evaluates, refines, and reuses skills across tasks.

The main idea is that agents can improve over time by turning experience into managed skills.

## Problem

LLM agents often need reusable skills to solve complex tasks involving tools, code, files, and multi-step workflows. But many skill-generation systems treat skills as isolated artifacts.

The paper identifies practical gaps:

- skills may be created outside the real runtime context;
- skills often lack structured memory from past use;
- skills may not be tested or refined systematically;
- long-horizon tasks can overflow or lose important context;
- skills are not always transferable between agents.

## Method

MUSE-Autoskill introduces a skill lifecycle with five main stages:

```text
creation → memory → management → evaluation → refinement
```

The framework includes:

- **on-demand skill creation** inside the agent loop;
- **skill-level memory** that stores experience for individual skills;
- **short-term and long-term memory** for task context;
- **skill retrieval and management** through a catalog;
- **unit-test-driven evaluation** for code-backed skills;
- **runtime feedback** to trigger refinement;
- **context compression** for long-horizon tasks;
- **cross-agent skill transfer** so skills created by one agent can help another.

## Evidence

The paper evaluates MUSE-Autoskill on SkillsBench and SkillLearnBench.

Reported findings include:

- MUSE performs strongly compared with Hermes, Codex, and Claude Code under the paper's settings.
- Human skills improve all compared agents.
- MUSE-created skills improve performance and show better stability in the reported experiments.
- Some MUSE-created skills transfer to other agents, such as Hermes.
- The results support the idea that skills can act as reusable infrastructure rather than one-time outputs.

## Why it matters

This paper is useful because it gives a concrete architecture for self-improving agents.

For a personal knowledge base, the key lesson is:

```text
Agent improvement should not only happen inside the model.
It can also happen through external, reusable, testable skills.
```

This connects directly to software engineering ideas: modularity, testing, memory, documentation, and reuse.

## Limitations and cautions

- The results depend on the chosen benchmarks and agent backends.
- Skill creation and evaluation can add cost and complexity.
- A generated skill may still encode wrong assumptions if evaluation is weak.
- Transfer across agents is promising but not guaranteed for every environment.
- Managing many skills requires good retrieval, naming, testing, and versioning.

## My takeaway

MUSE-Autoskill is important because it reframes skills as a lifecycle-managed asset. A strong agent system needs more than prompts and tools; it needs a way to remember what worked, test it, refine it, and reuse it safely.

## Related notes

- [SkillClaw](skillclaw-collective-skill-evolution-agentic-evolver.md)
- [Towards Uncertainty-Aware Language Agent](towards-uncertainty-aware-language-agent.md)
- [Step-Level Optimization for Efficient Computer-Use Agents](step-level-optimization-efficient-computer-use-agents.md)
- [A Survey of Context Engineering for Large Language Models](survey-of-context-engineering-for-llms.md)

## Source

Original source: https://arxiv.org/html/2605.27366v2
