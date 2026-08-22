---
source_url: https://developers.google.com/machine-learning/crash-course/numerical-data
author: Google Developers
date: 25-08-2025
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, data-preparation, numerical-data, feature-engineering, normalization]
---

# Working with Numerical Data

## TL;DR

Numerical data is data that has meaningful numeric value, such as age, price, distance, count, or temperature. Machine learning models often need numerical features to be explored, cleaned, scaled, transformed, or binned before training.

Good numerical features can improve a model more than changing the algorithm.

## Core idea

A model learns from numbers, but not every number is immediately useful. Numerical data often needs preparation.

Common preparation steps:

```text
raw numbers → explore visually and mathematically → handle outliers → normalize or bin → model input
```

## Simple example

The original source uses examples such as temperature, weight, and animal counts, and it warns that postal codes are numbers but should usually be treated as categories.

For a personal learning example, suppose we want to predict apartment rent.

Useful numerical features:

- apartment size in square meters
- distance from city center in kilometers
- number of rooms
- building age
- floor number

Before training, we may need to handle missing values, remove impossible values, normalize large ranges, or group noisy values into bins.

## Key terms

- **Numerical feature**: a feature where numeric operations are meaningful.
- **Feature vector**: the group of feature values given to a model for one example.
- **Outlier**: a value that is unusually far from the normal range.
- **Normalization/scaling**: changing numeric ranges so features are easier for the model to use.
- **Binning**: converting numeric ranges into groups, such as age 0–18, 19–35, 36–60.
- **Continuous feature**: a numeric feature that can take many ordered values.

## Why it matters

Models do not understand numbers the way humans do. A model only sees values and patterns. Bad numerical features can mislead the model, while clean and meaningful numerical features can make learning much easier.

For example, a value like `999999` might mean missing data, not a real measurement. If you do not clean it, the model may learn a false pattern.

## What makes a good numerical feature

A good numerical feature is usually:

- clearly defined;
- available at prediction time;
- measured consistently;
- not full of missing or impossible values;
- related to the target;
- transformed if the raw scale is hard to learn from.

## Common beginner mistakes

- Treating every number as truly numerical. A postal code is a number, but mathematically it behaves like a category.
- Forgetting to apply the same transformation to training, validation, and test data.
- Leaving impossible values in the dataset.
- Scaling after splitting incorrectly, causing data leakage.
- Ignoring outliers before training.

## When to use transformations

Use scaling when features have very different ranges.

Use binning when exact numeric values are noisy but ranges are meaningful.

Use outlier handling when rare extreme values distort the model.

Use visualization and basic statistics before deciding how to transform the feature.

## Mental model

Numerical data preparation is like cleaning and shaping raw ingredients before cooking. The model can only learn well if the inputs are usable.

## Verification notes

- Verified against the original Google Developers Working with Numerical Data page on 2026-08-22.
- Source confirms feature vectors, visual/mathematical data exploration, outlier identification, normalization, binning, and good continuous numerical features.
- The apartment-rent example is adapted for personal learning.

## Related notes

- [Categorical Data](working-with-categorical-data-google-ml-crash-course.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)
- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/numerical-data