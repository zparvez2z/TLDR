---
source_url: https://scikit-learn.org/stable/modules/feature_selection.html
author: scikit-learn Developers
date: 29-07-2026
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
- **Filter method**: selects features using statistical tests before training the main model.
- **Wrapper method**: trains models repeatedly to test feature subsets.
- **Embedded method**: selects features as part of model training.
- **RFE**: recursive feature elimination; repeatedly removes the least useful features.
- **L1 regularization**: can push some feature weights to zero, effectively selecting features.

## Why it matters

Feature selection can help when a dataset has too many columns, noisy features, sparse features, or duplicated information. It can also make models easier to explain.

However, removing features too aggressively can hurt performance if useful signals are removed.

## Common approaches

### Filter methods

Use statistics to rank features before the main model is trained.

Examples: variance threshold, chi-square tests, mutual information.

### Wrapper methods

Train models with different feature subsets and compare performance.

Example: recursive feature elimination.

### Embedded methods

Let the model choose features during training.

Examples: L1-regularized linear models, tree-based feature importance.

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

## Related notes

- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Regularization](overfitting-l2-regularization.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://scikit-learn.org/stable/modules/feature_selection.html