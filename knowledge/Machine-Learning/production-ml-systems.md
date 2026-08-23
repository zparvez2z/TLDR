---
source_url: https://developers.google.com/machine-learning/crash-course/production-ml-systems
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Google Developers Production ML Systems module; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, production-ml, mlops, monitoring, deployment]
---

# Production ML Systems

## TL;DR

A production ML system is much more than a trained model. The model is only one small part of a larger ecosystem that includes data collection, feature extraction, data verification, serving infrastructure, monitoring, and process management.

This note explains what changes when ML moves from a notebook or experiment into a real product.

## Core idea

In production, the question is not only:

```text
Does the model work?
```

The better question is:

```text
Can the whole ML system keep working reliably with real data, real users, and changing conditions?
```

A production ML system includes many supporting components around the model.

## Simple example

Suppose we build a rent prediction model.

In a notebook, we may only train and test the model once.

In production, we need to answer questions like:

- How is new apartment data collected?
- Are features calculated the same way during training and serving?
- How often should the model be retrained?
- Is prediction latency acceptable?
- Are predictions getting worse over time?
- What happens if input data is missing or wrong?
- How do we test a new model before giving it to users?

## Key terms

- **Production ML**: running an ML model as part of a real system or product.
- **Training**: building the model from data.
- **Inference/serving**: using the model to make predictions.
- **Static training**: training the model occasionally or manually.
- **Dynamic training**: retraining the model automatically or frequently.
- **Static inference**: precomputing predictions and serving them later.
- **Dynamic inference**: computing predictions on demand.
- **Monitoring**: tracking data, predictions, system health, and performance over time.
- **Train-serving skew**: mismatch between training-time and serving-time data or transformations.

## Why it matters

A model can perform well during development but fail in production because the surrounding system is weak.

Common production problems include:

- input data changes;
- data pipelines break;
- features are calculated differently in training and serving;
- model quality slowly degrades;
- latency is too high;
- users behave differently than expected;
- no one notices when predictions become unreliable.

## Important design choices

### Static vs dynamic training

Static training is simpler and easier to control. Dynamic training keeps models fresher but requires more automation and monitoring.

### Static vs dynamic inference

Static inference can be faster at serving time because predictions are precomputed. Dynamic inference can use the newest user or context data but may increase latency and complexity.

### Testing and monitoring

Production ML needs more than model metrics. It needs unit tests, integration tests, deployment checks, canary releases, data monitoring, model monitoring, and alerting.

## Common beginner mistakes

- Thinking deployment means only uploading the model file.
- Ignoring data pipelines and feature consistency.
- Not monitoring prediction quality after deployment.
- Retraining automatically without validating the new model.
- Forgetting that real-world data changes over time.
- Testing only the model and not the whole system.

## When to use this thinking

Use production ML thinking whenever a model will affect real users, business decisions, automation, or repeated workflows.

Even a simple model needs production thinking if it will be used continuously.

## Mental model

A trained model is like an engine. A production ML system is the whole car: engine, fuel, dashboard, brakes, sensors, maintenance, and driver safety.

## Related notes

- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)
- [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Automated Machine Learning](automated-machine-learning-automl.md)
- [Fairness](ml-fairness-crash-course-module.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/production-ml-systems
