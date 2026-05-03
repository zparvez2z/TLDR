---
source_url: https://arxiv.org/html/2604.27419v1
author: Qiyao Wang, Haoran Hu, Longze Chen, Hongbo Wang, Hamid Alinejad-Rokny, Yuan Lin, Min Yang
date: 03-05-2026
---

# InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?

This paper introduces InteractWeb-Bench, a novel benchmark designed to evaluate multimodal large language model (MLLM) agents on interactive website generation tasks involving ambiguous, low-quality instructions from non-expert users. The benchmark simulates diverse user behaviors through persona-driven instruction perturbations and provides an interactive environment allowing agents to clarify, implement, verify, and submit steps dynamically. Extensive experiments reveal that current models still largely fall into blind execution, struggling with proactive intent recognition and effective user interaction. The study highlights key insights for improving agent adaptability and aligning generated websites with user intent under realistic, noisy instruction conditions.

Key points and takeaways:
- Existing benchmarks focus on idealized, well-structured instructions, which contrast with the ambiguous, fragmented inputs of real-world low-code users.
- Blind execution describes the failure mode where agents passively execute flawed instructions without clarifying ambiguities, leading to frequent errors and hallucinations.
- InteractWeb-Bench introduces four user personas simulating different types of ambiguous and contradictory requirements to stress test agents.
- The benchmark provides a unified multi-path action space (Clarify, Implement, Verify, Submit) to enable dynamic intent refinement and visual verification.
- Experiments show agents struggle with proactive clarification, over-generate code when underspecified, and fail to leverage GUI-based feedback effectively, exposing limitations in current MLLMs.