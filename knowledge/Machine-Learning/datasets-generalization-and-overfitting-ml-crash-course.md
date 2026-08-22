---
source_url: https://developers.google.com/machine-learning/crash-course/overfitting
author: Google Developers
date: 03-12-2025
source_last_updated: 2025-12-03
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, overfitting, generalization, datasets, validation]
---

# Datasets, Generalization, and Overfitting

## TL;DR

A model is useful only if it performs well on new data, not just on the data it saw during training. Overfitting happens when a model memorizes training data too closely and fails to generalize.

This note explains why data quality, dataset splitting, validation, regularization, early stopping, and loss curves matter.

## Core idea

Good machine learning is not only about choosing an algorithm. It is also about building a reliable dataset and checking whether the model generalizes.

```text
training data → model learns
validation/test data → check if learning transfers to new examples
```

If training performance is good but validation performance is bad, the model may be overfitting.

## Simple example

Suppose a model predicts apartment rent.

If the model memorizes exact apartments from the training data, it may perform very well during training. But when a new apartment appears, it may predict badly because it did not learn the general pattern.

A good model should learn patterns such as:

- bigger apartments usually cost more;
- location affects rent;
- condition and age matter;
- similar apartments should have similar prices.

It should not simply memorize individual examples.

## Key terms

- **Generalization**: performing well on new, unseen data.
- **Overfitting**: learning training data too specifically, including noise.
- **Underfitting**: model is too simple and misses important patterns.
- **Training set**: data used to train the model.
- **Validation set**: data used to tune model choices.
- **Test set**: data used for final evaluation.
- **Data leakage**: when information from validation/test data accidentally influences training.
- **Loss curve**: a plot showing how loss changes during training.
- **Regularization**: reducing overfitting by controlling model complexity.

## Why it matters

A model that only works on training data is not useful. Real ML systems must handle new users, new products, new apartments, new emails, or new situations.

This is why validation and test data are essential.

## How to reduce overfitting

Common methods:

- use more representative data;
- clean unreliable or incorrect data;
- split data correctly into training, validation, and test sets;
- reduce model complexity;
- use regularization;
- use early stopping;
- avoid data leakage;
- evaluate with the right metric.

## Dataset quality checklist

Before trusting a model, check:

- Are labels correct?
- Are important features missing?
- Are there duplicates?
- Are there impossible values?
- Is the dataset representative of future data?
- Are classes imbalanced?
- Were transformations learned only from training data?

## Common beginner mistakes

- Measuring only training performance.
- Using the test set many times during tuning.
- Splitting data after preprocessing in a way that causes leakage.
- Ignoring label quality.
- Thinking more complex models are always better.
- Not checking whether validation and test data reflect the real problem.

## Mental model

Training is like practicing with example questions. Generalization is whether you can solve new questions on the exam. Overfitting is memorizing the practice answers without understanding the topic.

## Verification notes

- Verified against the original Google Developers Datasets, Generalization, and Overfitting page on 2026-08-22.
- Source confirms data quality importance, dataset construction, feature engineering, unreliable data, direct vs derived labels, training/validation/test splits, overfitting, regularization, early stopping, and loss-curve interpretation.
- The apartment-rent example is adapted for personal learning.

## Related notes

- [Regularization](overfitting-l2-regularization.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/overfitting