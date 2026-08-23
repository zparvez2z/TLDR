---
source_url: https://arxiv.org/html/2507.13334v2
author: Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Baolong Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi Li, Duzhen Zhang, Chenlin Zhou, Jiayi Mao, Tianze Xia, Jiafeng Guo, Shenghua Liu
date: 21-07-2025
source_version: arXiv v2
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original arXiv HTML paper; this note summarizes the paper's taxonomy and main claims for personal learning.
difficulty: Advanced
tags: [machine-learning, llm, context-engineering, rag, memory-systems, agents]
---

# A Survey of Context Engineering for Large Language Models

## TL;DR

Context engineering is the systematic design and management of the information given to an LLM at inference time. This survey argues that LLM performance depends heavily on context, not only on the model itself.

The paper organizes context engineering into foundational components and system implementations.

## Problem

Prompt engineering is too narrow for modern LLM systems. Real systems often need retrieval, memory, tool calls, structured data, long-context processing, and multi-agent coordination.

The problem is that these methods are often studied separately. This makes it harder to understand how they connect.

## Core idea

The paper treats context engineering as a full system design problem:

```text
user/task → retrieve/generate context → process/manage context → LLM → output/action
```

The context is not just the prompt text. It can include documents, memory, tools, examples, structured data, intermediate reasoning, and other agents' messages.

## Main taxonomy

The paper divides context engineering into three foundational components:

1. **Context retrieval and generation**  
   Finding or creating useful information for the model, including prompting, RAG, and dynamic context assembly.

2. **Context processing**  
   Handling long context, structured information, self-refinement, and multimodal context.

3. **Context management**  
   Managing memory, compression, context windows, and optimization over time.

It then shows how these components appear in larger systems:

- Retrieval-Augmented Generation (RAG)
- Memory systems
- Tool-integrated reasoning
- Multi-agent systems

## Why it matters

A strong model can still fail if it receives weak, messy, missing, or poorly organized context. Context engineering is therefore a practical skill for building reliable LLM applications.

For example, a RAG system is not only about retrieving documents. It also needs to decide which documents matter, how to format them, how much to include, and how to manage context limits.

## Key takeaway

The paper's most useful idea is that context should be designed like architecture, not like a single prompt.

```text
Prompt engineering = writing better instructions
Context engineering = designing the full information environment around the model
```

## Limitations

- This is a survey, not a single controlled experiment.
- The field is changing quickly, so the taxonomy may need updates.
- Many techniques are system-dependent and may not transfer directly across models or products.
- The paper identifies a gap between understanding complex contexts and generating equally complex long outputs, but solving that gap remains future work.

## My takeaway

For practical LLM projects, context engineering is one of the most important topics after basic prompt design. It connects RAG, memory, tools, agents, and long-context systems into one framework.

## Related notes

- [Introduction to Large Language Models](introduction-to-large-language-models.md)
- [LLM Evaluation Metrics](llm-evaluation-metrics-everything-you-need.md)
- [Reasoning Language Models: A Blueprint](reasoning-language-models-a-blueprint.md)
- [Production ML Systems](production-ml-systems.md)

## Source

Original source: https://arxiv.org/html/2507.13334v2
