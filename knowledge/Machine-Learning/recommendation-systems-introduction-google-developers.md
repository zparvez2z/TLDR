---
source_url: https://developers.google.com/machine-learning/recommendation
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Google Developers Recommendation Systems introduction; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, recommendation-systems, embeddings, candidate-generation, ranking]
---

# Recommendation Systems: Introduction

## TL;DR

Recommendation systems help users find useful items from a large set of options. They are used in search, shopping, video platforms, music apps, social feeds, job platforms, and many other products.

A typical recommender does not simply choose one item directly. It often uses a pipeline: generate candidates, score them, and re-rank the final results.

## Core idea

Recommendation systems narrow a huge item space into a small useful list.

```text
many possible items → candidate generation → scoring → re-ranking → final recommendations
```

The goal is to show items that are relevant, useful, and likely to match the user's context or interests.

## Simple example

Suppose a movie platform has 100,000 movies.

The system cannot deeply score every movie for every user in real time. Instead, it may:

1. generate a few hundred candidate movies;
2. score them based on user history, item features, and similarity;
3. re-rank them to balance quality, diversity, freshness, or business rules;
4. show the top recommendations.

## Key terms

- **Recommendation system**: a system that suggests useful items to users.
- **Candidate generation**: quickly finds a smaller set of possible recommendations.
- **Scoring**: estimates how good each candidate is for the user or query.
- **Re-ranking**: adjusts the scored list using extra rules or goals.
- **Content-based filtering**: recommends items similar to what the user liked before.
- **Collaborative filtering**: recommends based on patterns from similar users or items.
- **Matrix factorization**: learns user and item representations from interaction data.
- **Embedding**: a vector representation of users, queries, or items.

## Why it matters

Recommendation systems are important because users often face too many choices. A good recommender reduces search effort and helps users discover relevant items.

From an ML point of view, recommender systems are also useful because they combine many ideas:

- embeddings;
- ranking;
- classification or regression;
- user behavior data;
- large-scale retrieval;
- evaluation beyond simple accuracy.

## Main approaches

### Content-based filtering

Uses item information, such as genre, keywords, topic, category, or description.

Example: recommending action movies because the user watched many action movies.

### Collaborative filtering

Uses behavior patterns from many users.

Example: users who liked movie A also often liked movie B.

### Deep-learning recommenders

Use neural networks and embeddings to represent users, items, or queries and learn more complex recommendation patterns.

## Common beginner mistakes

- Thinking recommendation is only classification. Many recommenders are ranking or retrieval systems.
- Ignoring candidate generation and focusing only on final scoring.
- Using only clicks as a signal without considering bias or accidental clicks.
- Measuring only short-term engagement and ignoring user satisfaction.
- Forgetting cold-start problems for new users or new items.
- Ignoring diversity, freshness, and fairness in the final list.

## When to use recommendation systems

Use a recommendation system when:

- users choose from many possible items;
- past behavior or item similarity can help future suggestions;
- ranking the best few options matters;
- personalization improves the experience.

It may be less useful when:

- there are very few items;
- user preferences are not available;
- recommendations require strict expert judgment;
- bad recommendations can cause serious harm.

## Mental model

A recommendation system is a smart filter. It starts with too many options and gradually narrows them down to a useful ranked list.

## Related notes

- [Embeddings](embeddings-ml-crash-course.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Neural Networks](neural-networks-google-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/recommendation
