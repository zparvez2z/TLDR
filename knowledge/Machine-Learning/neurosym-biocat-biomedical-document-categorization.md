---
source_url: https://arxiv.org/html/2411.00041v1
author: Parvez Zamil, Gollam Rabby, Md. Sadekur Rahman, Sören Auer
date: 04-08-2025
---

# NeuroSym-BioCAT: Leveraging Neuro-Symbolic Methods for Biomedical Scholarly Document Categorization and Question Answering

The paper introduces NeuroSym-BioCAT, a novel approach for improving information retrieval from the vast collection of biomedical scholarly documents. This method integrates an optimized topic modeling framework (OVB-LDA with BI-POP CMA-ES) for document categorization with a fine-tuned MiniLM model for precise answer extraction. The study evaluates this approach against established methods and finds that it performs competitively, particularly when focusing only on document abstracts. This suggests that smaller, domain-specific models can be highly effective, challenging the idea that only large, resource-intensive models are suitable for complex biomedical text analysis.

Key Points:
* A novel neuro-symbolic method is proposed, combining optimized topic modeling for document categorization and advanced machine learning for answer extraction.
* The method is evaluated across three configurations: scholarly document abstract retrieval, golden scholarly documents abstract, and golden snippets, demonstrating superior performance over existing methods.
* The research shows that a distilled model (MiniLM), when fine-tuned on domain-specific data, can effectively extract answers, particularly from concise scholarly abstracts.
* Findings suggest that future biomedical information retrieval could efficiently focus on abstracts, reducing reliance on computationally intensive models and full-text analysis.