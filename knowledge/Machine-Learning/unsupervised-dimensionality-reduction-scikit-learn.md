---
source_url: https://scikit-learn.org/stable/modules/unsupervised_reduction.html
author: scikit-learn developers
date: 25-08-2026
source_type: documentation
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-25
verification_scope: Checked against the original scikit-learn documentation; this note summarizes unsupervised dimensionality reduction, PCA, random projections, feature agglomeration, pipelines, and scaling cautions for personal learning.
difficulty: Intermediate
tags: [machine-learning, scikit-learn, dimensionality-reduction, pca, random-projection, feature-agglomeration]
---

# Unsupervised Dimensionality Reduction

## TL;DR

Unsupervised dimensionality reduction reduces the number of input features before a supervised learning step.

It is useful when a dataset has many features and you want to compress the data, remove noise, or make later modeling easier.

## Core idea

Some datasets have a very large number of features.

```text
many original features → unsupervised reduction → fewer transformed features → supervised model
```

The reduction step does not use the target label directly. It learns a transformation from the structure of the input features.

## Why it matters

Dimensionality reduction can help with:

- reducing the number of features;
- making models faster;
- reducing noise;
- improving visualization;
- simplifying later supervised learning;
- handling high-dimensional data such as text, images, or many engineered features.

It is not guaranteed to improve every model. It is a tool to test, not a magic fix.

## Main methods in the source

### PCA: Principal Component Analysis

`decomposition.PCA` looks for combinations of features that capture much of the variance in the original data.

PCA is useful when many original features are correlated and can be represented with fewer components.

Example mental model:

```text
100 related features → PCA → 10 components that preserve much of the variation
```

### Random projections

The `random_projection` module provides tools that reduce dimensionality using random projection methods.

Random projection can be useful for very high-dimensional data where a cheaper transformation is needed.

### Feature agglomeration

`cluster.FeatureAgglomeration` groups together features that behave similarly using hierarchical clustering.

This is different from clustering samples. Here, the features themselves are grouped.

## Pipelines

scikit-learn notes that unsupervised reduction can be chained with a supervised estimator in a pipeline.

Example structure:

```text
scaler → dimensionality reduction → classifier/regressor
```

This is important because the transformation should be fitted only on the training data during evaluation.

Using a pipeline helps avoid data leakage.

## Scaling caution

Feature agglomeration can behave badly if features have very different scales or statistical properties.

A scaling step such as `StandardScaler` can be useful before feature agglomeration.

## Common beginner mistakes

- Reducing dimensions before splitting data, which can cause leakage.
- Assuming fewer features always means better performance.
- Forgetting that PCA components are combinations of original features and can be harder to interpret.
- Using dimensionality reduction without checking validation performance.
- Forgetting feature scaling before methods that depend on feature distances or similarities.

## Mental model

Dimensionality reduction is like compressing a large map into a smaller map. You keep the most useful structure, but some detail is lost.

## Related notes

- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Feature Selection](feature-selection-scikit-learn-user-guide.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://scikit-learn.org/stable/modules/unsupervised_reduction.html
