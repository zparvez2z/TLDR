---
source_url: https://arxiv.org/html/2401.14016v3
author: Jiuzhou Han, Wray Buntine, Ehsan Shareghi
date: 02-05-2026
---

# Towards Uncertainty-Aware Language Agent

This paper proposes the Uncertainty-Aware Language Agent (UALA), a novel framework that integrates uncertainty quantification into language agents to improve reasoning and decision-making processes. UALA dynamically balances the use of the language model's internal knowledge and external tools based on estimated uncertainty, leading to improved task performance and reduced reliance on external resources. Extensive experiments across multiple tasks and language model sizes demonstrate significant gains over existing methods like ReAct. The study also reveals that verbalized confidence by LLMs is a poor uncertainty proxy, and uncertainty-based approaches outperform agent fine-tuning with limited data.

Key points and takeaways:
- UALA is the first language agent framework integrating uncertainty estimation into reasoning trajectories.
- It enables a plug-and-play approach for various uncertainty measurement techniques.
- The framework significantly improves performance and reduces external API calls and tokens.
- Uncertainty calibration correlates with answer correctness, validating uncertainty measurements.
- Verbalized confidence from LLMs is unreliable for uncertainty quantification.
- Leveraging uncertainty yields better performance improvements than fine-tuning under data constraints.