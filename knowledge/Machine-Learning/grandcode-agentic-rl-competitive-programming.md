---
source_url: https://arxiv.org/html/2604.02721v1
author: Xiaoya Li, Xiaofei Sun, Guoyin Wang, Songqiao Su
date: 11-07-2026
---

# GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Reinforcement Learning

The paper introduces GrandCode, a multi-agent reinforcement learning system that surpasses top human performers in live Codeforces competitive programming contests. The system orchestrates specialized agents for hypothesis generation, solution synthesis, summarization, and adversarial test case generation, and improves them via post-training and test-time reinforcement learning. A key algorithmic contribution is Agentic GRPO, which combines immediate reward updates with delayed correction to address off-policy drift and long-horizon credit assignment in multi-stage agent rollouts. GrandCode achieved first place in three consecutive live Codeforces rounds in March 2026, demonstrating state-of-the-art performance in real competitive settings.
- Multi-agent architecture with modules for hypothesis proposal, main solving, summarization, and test generation in an agentic verification-and-refinement loop.
- Agentic GRPO: a GRPO variant integrating immediate rewards and delayed correction for robust credit assignment under asynchronous, multi-stage rollouts.
- Difficulty-based routing and length penalties, plus orchestration strategies among main, hypothesis, and summary policies.
- Adversarial and difference-driven test case generation, solution-attack techniques, and large-size test cases to stress robustness.
- Combined post-training RL and online test-time RL, including best-of-N reward smoothing and live-contest strategies balancing direct generation and test-time adaptation.
- Strong empirical results: first place in Codeforces Rounds 1087, 1088, and 1089 (March 2026) under standard live contest conditions.
- Infrastructure for asynchronous training, pipelined attention mixtures, batching with balanced difficulty/length, and expert routing for stability and load balancing.
- Built on Qwen 3.5 and leverages additional models/data sources; includes supervised fine-tuning, continued training on noisy data, and specialized summarization models.