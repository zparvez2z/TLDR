---
source_url: https://developers.google.com/machine-learning/intro-to-ml
author: Google Developers
date: 25-08-2025
difficulty: Beginner
tags: [machine-learning, fundamentals, supervised-learning, features, labels]
---

# Introduction to Machine Learning

## TL;DR

Machine learning is a way to build systems that learn patterns from data instead of being programmed only with fixed rules. A model is trained using examples, then it uses what it learned to make predictions on new data.

This is the first real concept note in the ML learning path.

## Core idea

Traditional programming usually works like this:

```text
Rules + Data → Answer
```

Machine learning works more like this:

```text
Data + Examples of correct answers → Learned model
Learned model + New data → Prediction
```

Instead of writing every rule by hand, we give the computer examples. The model learns patterns from those examples.

## Simple example

Suppose we want to predict apartment rent.

**Features** are the input information:

- apartment size
- city
- distance from city center
- number of rooms
- building age

**Label** is the answer we want the model to learn:

- monthly rent

During training, the model sees many apartments with their real rents. After training, it can estimate the rent for a new apartment.

## Key terms

- **Feature**: an input value used by the model, such as size, age, or location.
- **Label**: the correct answer in the training data, such as the real rent or the correct class.
- **Model**: the learned pattern that maps features to predictions.
- **Training**: the process of teaching the model from examples.
- **Prediction**: the model's output for new data.
- **Evaluation**: checking how well the model performs.
- **Metric**: a number used to measure performance, such as accuracy, precision, recall, or error.

## Main types of machine learning

### Supervised learning

The model learns from examples that already have correct answers.

Example: predicting house prices from past house sale data.

### Unsupervised learning

The model looks for patterns in data without given answers.

Example: grouping customers by similar behavior.

### Reinforcement learning

The model learns by taking actions and receiving rewards or penalties.

Example: a game-playing agent learning which moves lead to winning.

## Why it matters

This topic gives you the vocabulary needed for almost every later ML topic. Linear regression, logistic regression, classification, neural networks, and LLMs all depend on the same basic ideas: data, features, labels, models, training, prediction, and evaluation.

## Common beginner mistakes

- Thinking ML is magic. It is pattern learning from examples.
- Thinking more data always fixes the problem. Bad data can still produce a bad model.
- Confusing features and labels. Features are inputs; labels are the answers used during training.
- Ignoring evaluation. A model is only useful if it works well on new data, not only on training data.

## When to use machine learning

Machine learning is useful when:

- rules are hard to write manually;
- you have enough useful examples;
- patterns in past data can help with future predictions;
- mistakes can be measured and improved.

Machine learning may not be a good choice when:

- the rule is simple and clear;
- there is not enough data;
- the cost of wrong predictions is too high without human review;
- the data does not represent the real problem.

## Related notes

- [Machine Learning Crash Course Roadmap](machine-learning-crash-course-google-developers.md)
- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Logistic Regression](logistic-regression-google-ml-crash-course.md)
- [Classification](classification-binary-thresholds-and-metrics.md)

## Source

Original source: https://developers.google.com/machine-learning/intro-to-ml
