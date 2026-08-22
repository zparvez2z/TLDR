---
source_url: https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets
author: Google Developers
date: 03-12-2025
source_last_updated: 2025-12-03
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, datasets, train-validation-test, generalization, data-leakage]
---

# Dividing Datasets into Training, Validation, and Test Sets

## TL;DR

A model should be evaluated on data it did not train on. The usual split is training data for learning, validation data for tuning, and test data for final evaluation.

The test set should be protected. Using it repeatedly during model development can make it less trustworthy.

## Core idea

A good ML workflow separates learning, tuning, and final checking.

```text
training set → fit the model
validation set → tune and compare models
test set → final check on unseen data
```

This helps estimate whether the model will generalize to new examples.

## Simple example

Suppose we train an apartment rent model.

- The **training set** teaches the model rent patterns.
- The **validation set** helps us choose features, learning rate, model type, or hyperparameters.
- The **test set** is used near the end to check whether the selected model works on unseen data.

If we keep changing the model based on test-set results, the model may slowly fit the test set too. Then the test score becomes too optimistic.

## Key terms

- **Training set**: data used to fit model parameters.
- **Validation set**: data used during development to tune choices.
- **Test set**: data reserved for final evaluation.
- **Generalization**: performance on new, unseen examples.
- **Data leakage**: when information from evaluation data accidentally influences training.
- **Representative data**: data that reflects the real-world problem.
- **Statistical significance**: having enough examples to make evaluation meaningful.

## Why it matters

Testing on training data does not prove that a model works. A model can memorize training examples and still fail on real-world data.

A reliable test set gives stronger evidence that the model can handle new examples.

## Good evaluation workflow

1. Split the original dataset into training, validation, and test sets.
2. Train the model on the training set.
3. Evaluate and tune using the validation set.
4. Iterate: change model, features, or hyperparameters.
5. Use the test set only for final confirmation.
6. Refresh validation/test sets when they have been reused too often.

## What makes a good validation or test set

A good validation or test set should be:

- large enough for meaningful evaluation;
- representative of the whole dataset;
- representative of real-world data;
- free of duplicates from the training set;
- transformed consistently with the training data;
- kept separate from training decisions as much as possible.

## Common beginner mistakes

- Evaluating only on training data.
- Tuning repeatedly on the test set.
- Forgetting that validation and test sets can “wear out” through repeated use.
- Keeping duplicate examples in both training and test sets.
- Splitting randomly when the real-world situation requires time-based or group-based splitting.
- Ignoring mismatch between dataset distribution and real-world data.
- Applying different feature transformations to train, validation, test, and real-world data.

## Practical warning

When you transform a feature in the training set, apply the same transformation to validation, test, and real-world data. Otherwise, model evaluation may not reflect how the model will behave later.

## Mental model

Training data is practice. Validation data is practice feedback. Test data is the final exam. Do not study from the final exam answers.

## Related notes

- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets
