---
source_url: https://developers.google.com/machine-learning/crash-course/linear-regression
author: Google Developers
date: 09-12-2025
source_last_updated: 2025-12-09
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, supervised-learning, regression, loss, gradient-descent]
---

# Linear Regression

## TL;DR

Linear regression is a supervised learning method used to predict a number. It learns a straight-line relationship between input features and a continuous label.

Use this note to understand the first simple model in the ML learning path.

## Core idea

Linear regression assumes the prediction can be built from weighted input features plus a bias term.

```text
prediction = bias + weight1 × feature1 + weight2 × feature2 + ...
```

The model starts with imperfect weights. During training, it adjusts those weights to reduce prediction error.

## Simple example

The original source explains linear regression with car fuel efficiency: car weight is used as a feature, and miles per gallon is the label.

For a personal learning example, suppose we want to predict apartment rent.

Features:

- apartment size
- number of rooms
- distance from city center
- building age

Label:

- monthly rent

A linear regression model might learn that larger apartments usually cost more, apartments closer to the city center usually cost more, and older buildings may affect price differently depending on the data.

## Key terms

- **Continuous label**: a numeric answer, such as price, temperature, salary, or rent.
- **Weight**: how strongly one feature affects the prediction.
- **Bias**: the starting value of the prediction before feature effects are added.
- **Loss**: a number that measures how wrong the prediction is.
- **Gradient descent**: the training method that adjusts weights step by step to reduce loss.
- **Learning rate**: controls how large each training update is.

## Why it matters

Linear regression is the simplest way to learn the full supervised learning cycle:

```text
features → model → prediction → loss → weight update → better prediction
```

Many later topics, including logistic regression and neural networks, build on this same idea.

## When to use it

Linear regression is useful when:

- the target is numeric;
- you need a simple baseline model;
- the relationship is roughly linear;
- interpretability matters.

It may not work well when:

- relationships are highly nonlinear;
- important features are missing;
- there are many extreme outliers;
- the target is a category rather than a number.

## Common beginner mistakes

- Using linear regression for classification problems.
- Thinking a low training loss always means a good model.
- Forgetting to evaluate on validation or test data.
- Ignoring feature scale when optimization behaves badly.
- Assuming linear regression is always too simple; it is often a strong baseline.

## Mental model

Think of linear regression as fitting the best straight line through data points. The line will not pass perfectly through every point, but it tries to minimize the overall error.

## Verification notes

- Verified against the original Google Developers Linear Regression page on 2026-08-22.
- Source confirms the linear regression equation, bias, weights, features, labels, training, loss, gradient descent, hyperparameter tuning, and multiple-feature models.
- The apartment-rent example is adapted for personal learning; the source uses car fuel efficiency as its main example.

## Related notes

- [Introduction to Machine Learning](introduction-to-machine-learning-google-for-developers.md)
- [Logistic Regression](logistic-regression-google-ml-crash-course.md)
- [Classification](classification-binary-thresholds-and-metrics.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/linear-regression