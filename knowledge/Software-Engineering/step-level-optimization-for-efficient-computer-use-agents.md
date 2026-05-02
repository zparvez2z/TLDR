---
source_url: https://arxiv.org/html/2604.27151v1
author: Unknown
date: 02-05-2026
---

# Step-level Optimization for Efficient Computer-use Agents

This paper addresses the inefficiency of uniformly allocating expensive large-model compute in computer-use agents interacting with GUIs. It proposes an event-driven, step-level cascade framework that uses lightweight monitors to detect elevated risk and selectively escalate to stronger models only when necessary. The approach reduces computational cost and latency while maintaining comparable success rates by differentiating routine steps from high-risk moments like progress stalls and semantic drift. Experiments demonstrate significant savings in inference cost and time on realistic computer-use benchmarks without architectural changes to base agents.

- Computer-use agents incur high costs due to running large models at every interaction step.
- Failures concentrate in a small number of high-risk steps: progress stalls and semantic drift.
- An event-driven cascade runs a small policy by default and escalates based on two monitors: Stuck and Milestone.
- The method reduces large-model usage by up to 74.6% and latency by 45.8% while preserving task success.
- The framework is modular and can be added without retraining or modifying existing agents.