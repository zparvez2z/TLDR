---
source_url: https://scikit-learn.org/stable/model_selection.html
author: scikit-learn Developers
date: 26-07-2026
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original scikit-learn documentation; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, model-selection, cross-validation, hyperparameter-tuning, evaluation]
---

# Model Selection and Evaluation

## TL;DR

Model selection is the process of choosing the model, settings, and evaluation method that work best on unseen data. The main goal is not to get the best training score, but to choose a model that generalizes.

Use this note as the practical workflow for comparing and tuning models.

## Core idea

A reliable ML workflow separates training from evaluation.

```text
split data → choose metric → train model → validate → tune → test once
```

The validation process helps you choose between models. The test set should be used only near the end to estimate final performance.

## Simple example

Suppose we want to choose a rent prediction model.

Candidate models:

- linear regression
- random forest
- gradient boosting

We use cross-validation to compare them fairly. Then we tune hyperparameters, such as tree depth or regularization strength. Finally, we test the selected model on data it has not seen during tuning.

## Key terms

- **Model selection**: choosing the best model or model configuration.
- **Hyperparameter**: a setting chosen before training, such as learning rate, tree depth, or regularization strength.
- **Cross-validation**: splitting data into several train/validation folds to estimate performance more reliably.
- **Grid search**: trying many predefined hyperparameter combinations.
- **Randomized search**: sampling hyperparameter combinations randomly.
- **Successive halving**: an efficient search method that gives more resources to promising candidates.
- **Validation curve**: shows how performance changes with one hyperparameter.
- **Learning curve**: shows how performance changes as training data increases.
- **Baseline model**: a simple model used as a reference point.

## Why it matters

A model that looks best on one random split may not really be best. Cross-validation reduces dependence on one lucky or unlucky split.

Model selection also prevents you from choosing a model based only on intuition. It makes model choice measurable.

## Practical workflow

1. Define the real goal.
2. Choose the right metric.
3. Create train/validation/test splits.
4. Start with a simple baseline.
5. Compare a few model families.
6. Tune hyperparameters using cross-validation.
7. Inspect learning curves and validation curves.
8. Evaluate the final model on the test set.
9. Document the result and limitations.

## Common beginner mistakes

- Tuning on the test set repeatedly.
- Choosing the model with the best training score.
- Trying complex models before building a baseline.
- Comparing models with different data splits.
- Optimizing the wrong metric.
- Forgetting that cross-validation costs more computation.

## When to use it

Use model selection whenever you have more than one possible model, preprocessing pipeline, metric, or hyperparameter setting.

It is especially important when:

- the dataset is small;
- model performance is close between options;
- hyperparameters strongly affect results;
- you need confidence that the model will generalize.

## Mental model

Model selection is like testing several study strategies before an exam. You do not choose the strategy that only worked once by luck; you choose the one that works consistently across practice tests.

## Verification notes

- Verified against the original scikit-learn Model Selection and Evaluation documentation on 2026-08-22.
- Source confirms cross-validation, hyperparameter tuning, decision-threshold tuning, metrics/scoring, validation curves, and learning curves.
- The rent-prediction example is adapted for personal learning.

## Related notes

- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Regularization](overfitting-l2-regularization.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)

## Source

Original source: https://scikit-learn.org/stable/model_selection.html