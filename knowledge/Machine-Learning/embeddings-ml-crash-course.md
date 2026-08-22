---
source_url: https://developers.google.com/machine-learning/crash-course/embeddings
author: Google Developers
date: 25-08-2025
difficulty: Intermediate
tags: [machine-learning, embeddings, vectors, representation-learning, neural-networks]
---

# Embeddings

## TL;DR

Embeddings are dense vector representations that help models understand similarity between items, words, categories, or users. They replace huge sparse encodings with smaller learned representations.

Embeddings are one of the key ideas behind recommendations, search, NLP, and large language models.

## Core idea

Instead of representing a category as a huge one-hot vector, an embedding represents it as a small list of numbers.

```text
"pizza" → [0.21, -0.44, 0.83, ...]
"burger" → [0.19, -0.40, 0.79, ...]
"airport" → [-0.72, 0.11, -0.36, ...]
```

Similar things should have similar vectors.

## Simple example

Suppose a food recommendation model learns embeddings for food items.

It may learn that:

```text
pizza is closer to burger than to laptop
shawarma is closer to kebab than to ice cream
```

The model is not given these relationships directly. It learns them from patterns in the data.

## Key terms

- **Embedding**: a dense vector representation learned from data.
- **Embedding space**: the vector space where similar items are placed near each other.
- **One-hot encoding**: sparse representation with one active position.
- **Dense vector**: a compact vector where many values carry information.
- **Semantic similarity**: similarity in meaning or behavior.
- **Static embedding**: one fixed vector for each item or word.
- **Contextual embedding**: representation changes depending on context.

## Why it matters

One-hot encoding does not express similarity. For example, one-hot vectors do not know that `king` and `queen` are more related than `king` and `banana`.

Embeddings make similarity learnable and useful.

They can reduce:

- memory usage;
- number of model parameters;
- computation cost;
- need for manual feature crosses.

## Common uses

Embeddings are useful for:

- recommendation systems;
- search ranking;
- text classification;
- language models;
- user/item similarity;
- image and text retrieval;
- categorical features with many possible values.

## Common beginner mistakes

- Thinking embedding dimensions have simple human meanings.
- Assuming similar vectors are always semantically correct.
- Using embeddings without enough training data.
- Forgetting that embeddings can encode bias from the data.
- Confusing one-hot encoding with embeddings.
- Treating embeddings as magic instead of learned numerical representations.

## When to use it

Use embeddings when:

- categories are too many for simple one-hot encoding;
- similarity between items matters;
- the model needs compact representations;
- text, users, products, or items need to be compared;
- neural networks are part of the pipeline.

## Mental model

An embedding is like a map. Items with similar meaning or behavior should appear close together on the map.

## Related notes

- [Categorical Data](working-with-categorical-data-google-ml-crash-course.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Neural Networks](neural-networks-google-ml-crash-course.md)
- [Introduction to Large Language Models](introduction-to-large-language-models.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/embeddings