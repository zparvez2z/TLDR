---
source_url: https://developers.google.com/machine-learning/crash-course/fairness
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Google Developers Fairness module; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, fairness, responsible-ai, bias, evaluation]
---

# Fairness in Machine Learning

## TL;DR

Fairness in machine learning means checking whether data and model predictions may reproduce or amplify harmful human bias. Responsible evaluation requires more than overall accuracy or loss.

Before putting a model into production, you should audit the training data and evaluate predictions for bias.

## Core idea

A model learns from data. If the data reflects biased human decisions, missing groups, measurement problems, or historical unfairness, the model can learn and repeat those patterns.

```text
biased data → biased model behavior → unfair predictions
```

Fairness work tries to identify and reduce these problems before and after training.

## Simple example

Suppose a hiring model is trained on historical hiring decisions.

If past hiring decisions favored one group unfairly, the model may learn that pattern and continue it. Even if the model never directly sees a sensitive attribute, other features may still act as proxies.

A fairness check would ask:

- Are all groups represented in the data?
- Are labels based on fair decisions?
- Does model performance differ across groups?
- Are some groups getting more false positives or false negatives?
- What should be done before deployment?

## Key terms

- **Fairness**: evaluating whether model behavior is appropriate and equitable across groups and contexts.
- **Bias**: systematic unfairness or distortion in data, labels, decisions, or predictions.
- **Responsible AI**: designing, evaluating, and deploying AI systems with attention to harm, reliability, and accountability.
- **Training data audit**: checking data before training for missing, skewed, or biased patterns.
- **Prediction audit**: checking model outputs for unfair differences across groups.
- **Sensitive attribute**: a characteristic such as gender, ethnicity, age, disability, or other protected/context-sensitive attribute.
- **Proxy feature**: a feature that indirectly reveals or correlates with a sensitive attribute.

## Why it matters

A model can have good average performance and still harm specific groups. Overall metrics can hide unequal errors.

For example, a classifier may have high overall accuracy but much worse false-negative rates for one group. Without subgroup evaluation, this problem may remain invisible.

## What to check

Fairness work often includes:

- checking whether the dataset represents the people affected by the model;
- looking for biased labels or historical unfairness;
- evaluating performance by subgroup;
- comparing error types across groups;
- checking whether features act as proxies for sensitive attributes;
- documenting known risks and limitations;
- deciding whether the model should be used at all.

## Common beginner mistakes

- Thinking fairness is only a technical metric.
- Looking only at overall accuracy.
- Assuming removing sensitive attributes automatically makes the model fair.
- Ignoring label bias in historical data.
- Treating fairness as something checked only after deployment.
- Forgetting that fairness decisions require context and human judgment.

## When to use fairness checks

Use fairness checks whenever a model affects people, opportunities, resources, ranking, access, safety, or decisions.

Fairness is especially important for:

- hiring;
- education;
- finance;
- healthcare;
- housing;
- policing/security;
- content ranking;
- recommendation systems.

## Mental model

Fairness work is like inspecting the foundation of a building. Even if the visible structure looks good, hidden bias in the foundation can make the whole system unsafe.

## Related notes

- [Classification](classification-binary-thresholds-and-metrics.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Production ML Systems](production-ml-systems.md)
- [Automated Machine Learning](automated-machine-learning-automl.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/fairness
