---
source_url: https://arxiv.org/html/2604.02176v3
author: Hongyuan Adam Lu, Z.L., Victor Wei, Zefan Zhang, Zhao Hong, Qiqi Xiang, Bowen Cao, Wai Lam
date: 11-07-2026
---

# Adam’s Law: Textual Frequency Law on Large Language Models

The paper introduces the Textual Frequency Law (TFL), which posits that among paraphrases with the same meaning, higher sentence-level frequency should be preferred for both prompting and fine-tuning large language models (LLMs). Because most LLM training datasets are closed, the authors estimate sentence-level frequency from online corpora and paraphrase inputs toward more frequent expressions. They further propose Textual Frequency Distillation (TFD) to refine frequency estimates using LLM-generated story completions and Curriculum Textual Frequency Training (CTFT) to fine-tune models in increasing frequency order. Experiments on a curated Textual Frequency Paired Dataset (TFPD) across math reasoning, machine translation, commonsense reasoning, and agentic tool calling demonstrate consistent gains, with high-frequency partitions outperforming low-frequency ones and sometimes surpassing ground-truth data.
- Textual Frequency Law (TFL): prioritize high-frequency paraphrases for better LLM performance in prompting and fine-tuning.
- Frequency estimation via online resources; inputs are paraphrased to more frequent expressions.
- Textual Frequency Distillation (TFD): use LLM story completions to adjust and improve frequency estimates.
- Curriculum Textual Frequency Training (CTFT): fine-tune models in increasing order of sentence-level frequency.
- Empirical findings: high-frequency partitions beat low-frequency and can outperform ground-truth; CTFT improves translation; positive correlation between frequency and performance.
- Theoretical and analytical components include token- and sentence-level results under Zipf’s law, semi-log linear relationships, and loss monotonicity.
- Resources: curated TFPD dataset and code repository (https://github.com/HongyuanLuke/frequencylaw).