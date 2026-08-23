---
source_url: https://developers.google.com/machine-learning/crash-course/automl
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Google Developers AutoML module; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, automl, hyperparameter-tuning, feature-engineering, model-selection]
---

# Automated Machine Learning (AutoML)

## TL;DR

AutoML automates repetitive parts of the machine learning workflow, such as feature engineering, feature selection, algorithm choice, hyperparameter tuning, and evaluation.

AutoML can make model building faster and more accessible, but it does not remove the need to understand the problem, data, metrics, and limitations.

## Core idea

Manual ML often requires many repeated experiments.

```text
choose algorithm → train → tune hyperparameters → evaluate → repeat
```

AutoML automates some of this repeated work.

```text
data + objective → automated search over models/features/settings → candidate model
```

The human still needs to define the problem and judge whether the result is useful and safe.

## Simple example

Suppose we want to predict whether a customer will cancel a subscription.

Manual approach:

- try logistic regression;
- try random forests;
- try gradient boosting;
- tune hyperparameters;
- compare validation metrics;
- repeat with different feature sets.

AutoML approach:

- provide the data and target;
- define the metric;
- let AutoML try multiple model and parameter combinations;
- review the best candidate model;
- validate it carefully before use.

## Key terms

- **AutoML**: tools and processes that automate parts of the ML workflow.
- **Feature engineering**: creating useful input features.
- **Feature selection**: choosing useful features and removing weak ones.
- **Algorithm selection**: choosing which model family to try.
- **Hyperparameter tuning**: searching for good model settings.
- **Validation set**: data used to compare and tune models.
- **Test set**: protected data used for final evaluation.

## Why it matters

AutoML is useful because ML development can involve repetitive work and specialized skills. Automating some of that work can speed up experimentation and help teams build models more easily.

But AutoML is not magic. A model can still fail if:

- the data is poor;
- the target is badly defined;
- the metric is wrong;
- the training data does not match real-world data;
- the model is deployed without testing and monitoring.

## What AutoML can help with

AutoML commonly helps with:

- data engineering tasks;
- feature engineering;
- feature selection;
- selecting an appropriate ML algorithm;
- choosing hyperparameters;
- evaluating metrics using validation and test datasets.

## Common beginner mistakes

- Thinking AutoML replaces ML understanding.
- Trusting the best AutoML score without checking the data and metric.
- Using the test set repeatedly during automated search.
- Ignoring fairness, leakage, and production constraints.
- Deploying the selected model without monitoring.
- Forgetting that AutoML optimizes what you ask it to optimize, not necessarily what you truly need.

## When to use it

AutoML is useful when:

- you need a quick baseline;
- the task is common and well-defined;
- you want to compare many models/settings quickly;
- the team has limited time or ML expertise;
- manual experimentation would be too repetitive.

Be careful when:

- the task is safety-critical;
- the data is messy or biased;
- the metric is hard to define;
- interpretability is important;
- deployment constraints are strict.

## Mental model

AutoML is like an assistant that tries many modeling options for you. It can save time, but you are still responsible for choosing the right goal and checking the result.

## Related notes

- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)
- [Feature Selection](feature-selection-scikit-learn-user-guide.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Production ML Systems](production-ml-systems.md)
- [Fairness](ml-fairness-crash-course-module.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/automl
