---
source_url: https://developers.google.com/machine-learning/crash-course/overfitting/regularization
author: Google Developers
date: 09-04-2026
difficulty: Beginner
tags: [machine-learning, regularization, l2, overfitting, generalization]
---

# Regularization: L2 and Early Stopping

## TL;DR

Regularization helps a model generalize by discouraging it from becoming too complex. L2 regularization does this by penalizing large weights during training.

Regularization is one of the main tools for reducing overfitting.

## Core idea

A model can fit training data too closely by giving very large importance to specific features. L2 regularization adds an extra penalty for large weights.

```text
training objective = prediction loss + regularization penalty
```

The model is no longer rewarded only for fitting the training data. It is also encouraged to stay simpler.

## Simple example

Suppose an apartment rent model learns that one rare feature has a huge effect:

```text
has_blue_door → rent increases by €900
```

Maybe this pattern happened by accident in the training data. Regularization discourages very large weights like this unless the feature is truly useful.

## Key terms

- **Regularization**: techniques that reduce overfitting by controlling model complexity.
- **L2 regularization**: penalizes the squared size of weights.
- **Lambda / regularization rate**: controls how strong the penalty is.
- **Weight magnitude**: how large the learned feature weights are.
- **Early stopping**: stopping training when validation performance stops improving.
- **Generalization**: performing well on unseen data.

## Why it matters

Without regularization, a flexible model can memorize noise. With too much regularization, the model may become too simple and underfit.

The goal is balance:

```text
too little regularization → overfitting
too much regularization → underfitting
right amount → better generalization
```

## L2 regularization intuition

L2 regularization pushes weights toward smaller values. It usually does not force weights exactly to zero, but it reduces extreme weights.

This can make the model more stable and less sensitive to noise in individual features.

## Early stopping intuition

Early stopping watches validation performance during training. If validation performance stops improving, training stops before the model memorizes too much training noise.

It is fast and practical, but it is not the same as carefully tuning regularization.

## Common beginner mistakes

- Thinking regularization always improves a model.
- Using a high regularization rate without checking validation performance.
- Forgetting that learning rate and regularization can interact.
- Looking only at training loss.
- Treating early stopping as a perfect replacement for good validation and tuning.

## When to use it

Use regularization when:

- validation performance is worse than training performance;
- the model has many features or parameters;
- feature weights become very large;
- the model behaves unstably on new data;
- you want better generalization.

## Mental model

Regularization is like telling the model: "Fit the data, but do not make the explanation unnecessarily complicated."

## Related notes

- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Logistic Regression](logistic-regression-google-ml-crash-course.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/overfitting/regularization