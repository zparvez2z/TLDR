---
source_url: https://scikit-learn.org/stable/getting_started.html
author: scikit-learn Developers
date: 21-07-2026
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original scikit-learn Getting Started documentation; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, scikit-learn, estimators, transformers, pipelines, cross-validation]
---

# Getting Started with scikit-learn

## TL;DR

scikit-learn is a Python machine learning library for supervised and unsupervised learning. Its main workflow is simple: choose an estimator, fit it on data, use it to predict, and evaluate the result.

Use this note to understand the basic scikit-learn workflow before using more advanced tools.

## Core idea

Most scikit-learn objects follow a consistent API.

```text
estimator.fit(X, y) → estimator.predict(new_X)
```

For preprocessing, transformers follow a similar pattern:

```text
transformer.fit(X_train) → transformer.transform(X)
```

This consistency makes it easier to combine preprocessing, models, evaluation, and tuning.

## Simple example

Suppose we want to classify Iris flowers.

The data is usually represented as:

```text
X = feature matrix
rows = samples
columns = features

y = target labels
```

A basic workflow is:

```text
load data → split data → preprocess → fit model → predict → evaluate
```

In scikit-learn, this workflow is often wrapped in a `Pipeline` so preprocessing and modeling stay together.

## Key terms

- **Estimator**: a scikit-learn object that learns from data, such as a classifier or regressor.
- **fit**: trains or learns from data.
- **predict**: produces predictions for new data.
- **X**: the feature matrix, usually shaped as `(n_samples, n_features)`.
- **y**: the target values or labels.
- **Transformer**: an object that changes data, usually with `fit` and `transform`.
- **Pipeline**: chains preprocessing and model steps together.
- **Cross-validation**: evaluates a model across several train/test splits.
- **Hyperparameter search**: tries different model settings to find better performance.

## Why it matters

scikit-learn is practical because the same basic pattern works across many models and tools. Once you understand `fit`, `predict`, `transform`, and `Pipeline`, the library becomes much easier to use.

The official guide also emphasizes that fitting a model does not prove it will work on unseen data. You must evaluate it using tools such as train/test splits or cross-validation.

## Practical workflow

1. Choose the task: classification, regression, clustering, or preprocessing.
2. Prepare `X` and `y`.
3. Split the data into training and test sets.
4. Put preprocessing and model steps into a `Pipeline`.
5. Fit the pipeline on training data.
6. Predict on validation/test data.
7. Evaluate with a suitable metric.
8. Tune hyperparameters with cross-validation when needed.

## Common beginner mistakes

- Forgetting that `X` should usually be two-dimensional.
- Mixing up features `X` and target labels `y`.
- Fitting preprocessing on the full dataset before splitting.
- Using `predict` before `fit`.
- Evaluating only on training data.
- Tuning a model without cross-validation.
- Searching hyperparameters on a model alone instead of searching over the full pipeline.

## When to use it

Use scikit-learn when you need classic machine learning workflows such as:

- classification;
- regression;
- clustering;
- preprocessing;
- feature extraction;
- model selection;
- cross-validation;
- hyperparameter search.

It is especially useful for tabular data and practical ML experiments.

## Mental model

scikit-learn is like a toolbox with a common handle. Many tools are different internally, but you use them with the same basic commands: `fit`, `transform`, `predict`, and `score`.

## Related notes

- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)

## Source

Original source: https://scikit-learn.org/stable/getting_started.html
