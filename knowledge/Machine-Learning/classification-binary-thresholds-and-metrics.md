---
source_url: https://developers.google.com/machine-learning/crash-course/classification
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, classification, threshold, confusion-matrix, precision, recall]
---

# Classification: Thresholds and Metrics

## TL;DR

Classification turns model scores or probabilities into class decisions. The most important idea is that the threshold controls the trade-off between different kinds of mistakes.

This note explains how to evaluate classification models using confusion matrices and metrics such as accuracy, precision, recall, F1, ROC, and AUC.

## Core idea

A classification model often produces a probability first.

```text
Probability of positive class = 0.73
```

A threshold converts that probability into a label.

```text
If probability >= threshold → predict positive
If probability < threshold → predict negative
```

Changing the threshold changes the model's behavior.

## Simple example

The original source uses spam/not-spam as an example of turning a probability into a category.

For a personal learning example, suppose a model predicts whether a patient needs extra medical review.

- A low threshold catches more risky cases but creates more false alarms.
- A high threshold creates fewer false alarms but may miss real risky cases.

The best threshold depends on the cost of each mistake.

## Confusion matrix

A confusion matrix compares predictions with reality.

| Case | Meaning |
| --- | --- |
| True Positive (TP) | Model predicted positive, and it was positive. |
| False Positive (FP) | Model predicted positive, but it was negative. |
| True Negative (TN) | Model predicted negative, and it was negative. |
| False Negative (FN) | Model predicted negative, but it was positive. |

## Key metrics

- **Accuracy**: overall percentage of correct predictions.
- **Precision**: when the model predicts positive, how often it is right.
- **Recall**: out of all real positives, how many the model catches.
- **F1 score**: combines precision and recall into one number.
- **ROC curve**: shows performance across many thresholds.
- **AUC**: summarizes how well the model separates positive and negative examples.

## Why it matters

Classification is not only about getting a high score. It is about choosing the right kind of error for the real problem.

For spam detection, false positives are annoying because good emails may be hidden. For disease detection, false negatives can be dangerous because sick patients may be missed.

## When to use each metric

Use **accuracy** when classes are balanced and mistakes have similar cost.

Use **precision** when false positives are expensive.

Example: only flagging a transaction as fraud when the model is highly confident.

Use **recall** when false negatives are expensive.

Example: detecting dangerous medical or security cases.

Use **F1** when you need a balance between precision and recall.

Use **AUC** when you want to compare ranking/separation quality across thresholds.

## Common beginner mistakes

- Using accuracy on imbalanced datasets.
- Forgetting that the threshold is adjustable.
- Treating precision and recall as independent; improving one often reduces the other.
- Choosing a metric before understanding the real-world cost of mistakes.
- Reporting only one metric when the problem needs several.

## Mental model

Classification is decision-making under uncertainty. The model gives a probability, but humans choose the threshold based on the situation.

## Verification notes

- Verified against the original Google Developers Classification page on 2026-08-22.
- Source confirms thresholds, binary classification, metrics, ROC, AUC, and the introduction to multi-class classification.
- The medical-review example is adapted for personal learning; the source uses spam/not-spam as its main example.

## Related notes

- [Logistic Regression](logistic-regression-google-ml-crash-course.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/classification