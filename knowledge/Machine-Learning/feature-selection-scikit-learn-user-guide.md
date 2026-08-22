---
source_url: https://scikit-learn.org/stable/modules/feature_selection.html
author: scikit-learn Developers
date: 29-07-2026
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original scikit-learn documentation; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, feature-selection, dimensionality-reduction, regularization, scikit-learn]
---

# Feature Selection

## TL;DR

Feature selection removes irrelevant, redundant, or weak features before or during modeling. The goal is to make models simpler, faster, easier to understand, and sometimes more accurate.

Feature selection is different from feature extraction: selection chooses from existing features; extraction creates new features.

## Core idea

More features are not always better. Too many weak or noisy features can make a model harder to train and easier to overfit.

```text
many raw features → select useful features → train simpler model
```

## Simple example

Suppose we predict apartment rent with 200 features.

Some useful features:

- apartment size
- city
- distance from city center
- number of rooms

Some weak or noisy features:

- random listing ID
- color of the website button
- duplicated city code
- fields with the same value for every apartment

Feature selection tries to remove the useless or redundant features.

## Key terms

- **Irrelevant feature**: a feature that does not help prediction.
- **Redundant feature**: a feature that repeats information already present elsewhere.
- **Dimensionality**: the number of features.
- **VarianceThreshold**: removes features with variance below a threshold.
- **Univariate feature selection**: selects features using statistical tests.
- **RFE**: recursive feature elimination; repeatedly removes the least useful features.
- **SelectFromModel**: selects features based on model-estimated importance.
- **L1 regularization**: can push some feature weights to zero, effectively selecting features.

## Why it matters

Feature selection can help when a dataset has too many columns, noisy features, sparse features, or duplicated information. It can also make models easier to explain.

However, removing features too aggressively can hurt performance if useful signals are removed.

## Common approaches

### Low-variance filtering

Remove features that barely change across samples.

### Univariate selection

Use statistical scores such as chi-square, F-tests, or mutual information to select useful features.

### Recursive feature elimination

Train a model, remove weak features, and repeat.

### Model-based selection

Use feature weights or feature importances from a model to choose features.

## Common beginner mistakes

- Selecting features using the full dataset before cross-validation, causing leakage.
- Removing features only because they look unimportant without validation.
- Using classification feature scores for regression tasks, or regression scores for classification tasks.
- Thinking feature selection always improves performance.
- Confusing feature selection with feature extraction.
- Ignoring domain knowledge.

## When to use it

Use feature selection when:

- there are many features;
- training is slow;
- the model overfits;
- interpretability matters;
- many features are noisy, duplicated, or irrelevant;
- you want a smaller model.

Avoid aggressive feature selection when data is limited and you are unsure which features matter.

## Mental model

Feature selection is like packing for a trip. You do not want to carry everything; you want the items that are actually useful.

## Verification notes

- Verified against the original scikit-learn Feature Selection documentation on 2026-08-22.
- Source confirms feature selection/dimensionality reduction, low-variance removal, univariate selection, recursive feature elimination, model-based selection, and L1-based feature selection.
- The apartment-rent example is adapted for personal learning.

## Related notes

- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Regularization](overfitting-l2-regularization.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://scikit-learn.org/stable/modules/feature_selection.html