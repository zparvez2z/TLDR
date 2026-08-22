---
source_url: https://developers.google.com/machine-learning/crash-course/logistic-regression
author: Google Developers
date: 25-08-2025
difficulty: Beginner
tags: [machine-learning, supervised-learning, classification, logistic-regression, probability]
---

# Logistic Regression

## TL;DR

Logistic regression is used for classification problems where the model predicts a probability. Instead of predicting a number like rent or temperature, it predicts how likely something is to belong to a class.

It is the bridge between linear regression and classification.

## Core idea

Logistic regression starts with a linear model, then passes the result through a sigmoid function so the output becomes a probability between 0 and 1.

```text
linear score → sigmoid → probability
```

Example output:

```text
0.91 = likely positive
0.12 = likely negative
```

The probability is not yet the final class. A later classification threshold turns it into a decision.

## Simple example

Suppose we want to predict whether an email is spam.

Features:

- number of suspicious words
- sender reputation
- number of links
- whether the email has attachments

Label:

- spam or not spam

The logistic regression model might output:

```text
Probability of spam = 0.87
```

If our threshold is 0.50, we classify it as spam.

## Key terms

- **Binary classification**: a problem with two possible classes, such as yes/no or spam/not spam.
- **Probability**: the model's confidence that an example belongs to the positive class.
- **Logit**: the raw linear score before the sigmoid function.
- **Sigmoid**: a function that squashes values into the 0 to 1 range.
- **Log loss**: a loss function used to train probability-based classifiers.
- **Threshold**: the cutoff used to convert probability into a class decision.

## Why it matters

Logistic regression is one of the most important baseline models for classification. It is simple, fast, interpretable, and often surprisingly effective.

It also teaches a key ML idea: models can predict probabilities first, and decisions can be made later depending on the cost of mistakes.

## When to use it

Logistic regression is useful when:

- the target is a class, especially binary;
- you need a simple and explainable classifier;
- the relationship between features and class probability is not too complex;
- you want a strong baseline before trying neural networks or tree models.

It may not work well when:

- the boundary between classes is highly nonlinear;
- important feature interactions are missing;
- the dataset is extremely imbalanced without proper handling;
- probability calibration is poor.

## Common beginner mistakes

- Thinking logistic regression predicts a final class directly. It predicts a probability first.
- Using the default threshold of 0.50 without thinking about false positives and false negatives.
- Confusing linear regression and logistic regression because both use weighted features.
- Evaluating only with accuracy when the dataset is imbalanced.
- Ignoring regularization and overfitting.

## Mental model

Think of logistic regression as a scoring system. It adds evidence from features, converts the score into a probability, then lets you choose how confident the model must be before saying yes.

## Related notes

- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Classification](classification-binary-thresholds-and-metrics.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Regularization](overfitting-l2-regularization.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/logistic-regression