---
source_url: https://scikit-learn.org/stable/modules/model_evaluation.html
author: scikit-learn Developers
date: 27-07-2026
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original scikit-learn documentation; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, metrics, scoring, evaluation, classification, regression]
---

# Metrics and Scoring

## TL;DR

Metrics measure how good a model's predictions are. The right metric depends on the real problem, the type of prediction, and the cost of mistakes.

A model is only as useful as the evaluation method used to judge it.

## Core idea

Different ML tasks need different metrics.

```text
classification → accuracy, precision, recall, F1, ROC AUC, log loss
regression → MAE, MSE, RMSE, R²
ranking/probability → log loss, Brier score, AUC, calibration-related metrics
```

Choosing the wrong metric can make a bad model look good.

## Simple example

Suppose a fraud model checks 10,000 transactions, but only 50 are actually fraud.

A model that predicts "not fraud" for everything gets very high accuracy:

```text
9,950 / 10,000 = 99.5% accuracy
```

But it catches zero fraud cases. Accuracy is misleading here. Recall, precision, F1, and business cost are more useful.

## Key terms

- **Metric**: a number used to evaluate performance.
- **Scoring function**: a function used by tools such as cross-validation or grid search to compare models.
- **Accuracy**: fraction of correct predictions.
- **Precision**: how many predicted positives are actually positive.
- **Recall**: how many real positives are found.
- **F1 score**: balance between precision and recall.
- **Log loss**: measures quality of predicted probabilities.
- **Brier score**: evaluates probability predictions for classification.
- **MAE**: average absolute error for regression.
- **MSE/RMSE**: squared-error based regression metrics that punish large errors more.
- **Baseline**: a simple reference model used to judge whether your model is actually useful.

## Why it matters

Metrics shape model behavior. If you optimize the wrong metric, the model may improve on paper but fail in practice.

For example:

- A medical screening model may prioritize recall.
- A spam filter may need a balance between precision and recall.
- A price prediction model may care about average error in euros.
- A recommendation model may care about ranking quality.

## Practical metric selection

Ask these questions first:

1. Is the target numeric or categorical?
2. Are classes balanced or imbalanced?
3. Which mistake is more expensive?
4. Do we need hard decisions or calibrated probabilities?
5. Will the metric be used for training, model selection, or reporting?

## Common beginner mistakes

- Using accuracy for imbalanced classification.
- Comparing models with different metrics.
- Optimizing one metric but reporting another.
- Ignoring business or real-world cost.
- Forgetting to compare against a simple baseline.
- Treating probability quality and decision quality as the same thing.

## When to use common metrics

Use **accuracy** for balanced classification with similar mistake costs.

Use **precision** when false positives are expensive.

Use **recall** when false negatives are expensive.

Use **F1** when precision and recall both matter.

Use **log loss** or **Brier score** when probability quality matters.

Use **MAE** when you want an easy-to-understand average error.

Use **RMSE** when large errors should be punished more strongly.

## Mental model

A metric is the scoreboard. Before training harder, make sure you are playing the right game.

## Verification notes

- Verified against the original scikit-learn Metrics and Scoring documentation on 2026-08-22.
- Source confirms choosing scoring functions based on the goal, separating prediction from decision-making, consistent scoring functions, scoring APIs, metric functions, cross-validation scoring, classification metrics, regression metrics, and dummy estimators.
- The fraud example is adapted for personal learning.

## Related notes

- [Classification](classification-binary-thresholds-and-metrics.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Logistic Regression](logistic-regression-google-ml-crash-course.md)

## Source

Original source: https://scikit-learn.org/stable/modules/model_evaluation.html