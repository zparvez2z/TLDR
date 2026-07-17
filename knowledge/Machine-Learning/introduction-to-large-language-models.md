---
source_url: https://developers.google.com/machine-learning/crash-course/llm
author: Unknown
date: 17-07-2026
---

# Introduction to Large Language Models | Machine Learning | Google for Developers

This Google ML Crash Course module introduces language models and large language models (LLMs), explaining how they estimate token and sequence probabilities to power tasks like text generation, translation, and summarization. It covers tokens and subword tokenization, n-gram language models and their sparsity trade-offs, and the importance of context in prediction. The module traces the progression from n-grams to recurrent neural networks and to Transformer-based LLMs that leverage self-attention to consider entire sequences. It also outlines how LLMs are created, the role of parameters, and practical techniques such as fine-tuning, distillation, and prompt engineering, while highlighting common challenges of LLMs.
- Language models predict the likelihood of tokens or sequences, enabling applications like generation, translation, and summarization.
- Tokens (often subwords) are the atomic units; tokenization is language-specific and affects model inputs and context handling.
- N-grams provide local context but face sparsity; RNNs extend context but have limitations, motivating Transformers and self-attention.
- LLMs use self-attention to evaluate whole-context information and scale with parameters and data.
- Fine-tuning adapts models to specific tasks; distillation compresses models for efficiency; prompt engineering guides model outputs.
- The module identifies key challenges with LLMs and emphasizes understanding context, parameters, and training strategies.