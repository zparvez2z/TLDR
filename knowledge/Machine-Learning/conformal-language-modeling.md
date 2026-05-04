---
source_url: https://arxiv.org/html/2306.10193
author: Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi Jaakkola, Regina Barzilay
date: 04-05-2026
---

# Conformal Language Modeling

The paper presents a novel approach to conformal prediction specifically tailored for language models (LMs), allowing the construction of prediction sets with rigorous performance guarantees. Instead of enumerating the vast output space of LMs, the method calibrates a stopping rule for sampling LM outputs until at least one acceptable response is covered with high probability. A simultaneous rejection rule is used to remove low-quality candidates, maintaining both accuracy and precision in the output set. The approach also enables identification of correct individual components within generated responses, such as phrases or sentences, and is applicable to various LM APIs. Empirical evaluations demonstrate robust coverage across tasks including open-domain question answering, text summarization, and radiology report generation.