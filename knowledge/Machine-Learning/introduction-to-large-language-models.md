---
source_url: https://developers.google.com/machine-learning/crash-course/llm
author: Google Developers
date: 17-07-2026
source_last_updated: 2026-01-09
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, llm, language-models, transformers, tokens, prompt-engineering]
---

# Introduction to Large Language Models

## TL;DR

A large language model is a model trained to predict text. By learning patterns from huge amounts of language data, it can generate, summarize, translate, classify, and reason over text-like inputs.

LLMs are advanced neural networks, but their core idea is still prediction from data.

## Core idea

A language model predicts likely next tokens based on context.

```text
context → probability distribution over next token → generated text
```

Large language models scale this idea with massive datasets, many parameters, and Transformer architectures that use self-attention to consider broad context.

## Simple example

Input context:

```text
The capital of Germany is
```

A language model assigns high probability to:

```text
Berlin
```

It does not look up the answer like a database by default. It predicts text based on learned patterns.

## Key terms

- **Token**: a piece of text, often a word part rather than a full word.
- **Context**: the text the model uses to make the next prediction.
- **Language model**: a model that predicts token sequences.
- **N-gram**: an ordered sequence of words or tokens used in older language-model approaches.
- **Large language model**: a scaled-up language model with many parameters and broad training data.
- **Parameter**: a learned value inside the model.
- **Transformer**: the architecture behind most modern LLMs.
- **Self-attention**: lets the model weigh relationships between tokens in the context.
- **Prompt**: the instruction or input given to the model.
- **Fine-tuning**: additional training for a specific task or behavior.
- **Distillation**: training a smaller model to imitate a larger one.

## Why it matters

LLMs are important because language is a common interface for knowledge work. They can help with writing, coding, summarization, search, tutoring, extraction, and many other tasks.

But they also have limitations. They can produce confident wrong answers, reflect bias in data, misunderstand context, or fail on tasks that require exact reasoning.

## How LLMs relate to earlier ML topics

LLMs build on many previous ideas:

- **features and labels**: training still depends on examples;
- **loss**: training reduces prediction error;
- **neural networks**: LLMs are deep neural networks;
- **embeddings**: tokens are represented as vectors;
- **classification/evaluation**: outputs still need evaluation;
- **generalization**: the model must work beyond memorized examples.

## Common beginner mistakes

- Thinking LLMs are databases.
- Assuming fluent text means the answer is correct.
- Ignoring prompt quality and context limits.
- Forgetting that LLMs can hallucinate.
- Treating all LLM outputs as equally reliable.
- Starting with LLMs before understanding basic ML concepts.

## When to use LLMs

LLMs are useful when:

- the input or output is language-like;
- you need summarization, drafting, classification, extraction, or explanation;
- the task benefits from flexible natural language understanding;
- exact deterministic rules are hard to write.

Be careful when:

- factual accuracy is critical;
- legal, medical, financial, or safety decisions are involved;
- the answer must be exactly reproducible;
- private or sensitive data is involved;
- the model output will be used without human review.

## Mental model

An LLM is a very powerful text prediction engine. It can behave like a writer, assistant, tutor, or coder, but underneath it is still predicting likely token sequences from context.

## Verification notes

- Verified against the original Google Developers Introduction to Large Language Models page on 2026-08-22.
- Source confirms language models, tokens, n-grams, context, recurrent neural networks, whole-context evaluation by LLMs, self-attention, parameters, fine-tuning, distillation, and key LLM problems.
- The Germany/Berlin example is adapted for personal learning.

## Related notes

- [Neural Networks](neural-networks-google-ml-crash-course.md)
- [Embeddings](embeddings-ml-crash-course.md)
- [Classification](classification-binary-thresholds-and-metrics.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Machine Learning Crash Course Roadmap](machine-learning-crash-course-google-developers.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/llm