---
source_url: https://scikit-learn.org/stable/modules/feature_extraction.html
author: scikit-learn Developers
date: 30-07-2026
difficulty: Intermediate
tags: [machine-learning, feature-extraction, text-vectorization, tf-idf, bag-of-words]
---

# Feature Extraction

## TL;DR

Feature extraction converts raw data into numerical features that a model can learn from. It is especially important for text, images, dictionaries, and other data that is not already in clean numeric table form.

Feature extraction creates features. Feature selection chooses among existing features.

## Core idea

Models need numerical input. Feature extraction turns raw objects into vectors.

```text
raw text / image / dictionary → numerical feature vector → model
```

For text, this often means converting words into counts, TF-IDF values, or embeddings.

## Simple example

Suppose we want to classify emails as spam or not spam.

Raw text:

```text
Win money now
```

A simple Bag-of-Words extractor might create features like:

```text
win: 1
money: 1
now: 1
meeting: 0
invoice: 0
```

Now the model can learn from the numbers.

## Key terms

- **Feature extraction**: creating numerical features from raw data.
- **Vectorization**: converting data into vectors.
- **Bag-of-Words**: represents text by word counts, ignoring word order.
- **TF-IDF**: gives higher weight to terms that are important in a document but not common everywhere.
- **DictVectorizer**: converts dictionaries of feature values into matrices.
- **FeatureHasher**: maps features into a fixed number of buckets using hashing.
- **Sparse matrix**: stores mostly-zero data efficiently.
- **Hashing trick**: fast feature mapping with possible collisions.

## Why it matters

Most real-world data is not model-ready. Text, categories, logs, events, and metadata need to be transformed before learning can happen.

Good feature extraction can make a simple model effective. Poor feature extraction can hide useful patterns from the model.

## Common approaches

### Dictionary features

Useful when each example is represented as key-value pairs.

Example:

```text
{"city": "Heilbronn", "rooms": 2, "furnished": true}
```

### Text features

Common tools:

- token counts;
- Bag-of-Words;
- TF-IDF;
- n-grams;
- embeddings.

### Hashing features

Useful for very large or streaming feature spaces where storing a full vocabulary is expensive.

Trade-off: hashing is fast, but less interpretable because original feature names may not be recoverable.

## Common beginner mistakes

- Confusing feature extraction with feature selection.
- Forgetting that Bag-of-Words ignores word order.
- Creating huge dense matrices instead of sparse matrices.
- Using hashing without understanding collisions.
- Fitting text vectorizers on the full dataset before splitting, causing leakage.
- Treating TF-IDF as always better than simple counts.

## When to use it

Use feature extraction when raw input is not already clean numeric features.

It is especially useful for:

- text classification;
- search and information retrieval;
- categorical dictionaries;
- logs and event data;
- large sparse feature spaces;
- natural language processing pipelines.

## Mental model

Feature extraction is translation. It translates messy real-world information into numbers a model can understand.

## Related notes

- [Feature Selection](feature-selection-scikit-learn-user-guide.md)
- [Categorical Data](working-with-categorical-data-google-ml-crash-course.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Embeddings](embeddings-ml-crash-course.md)

## Source

Original source: https://scikit-learn.org/stable/modules/feature_extraction.html