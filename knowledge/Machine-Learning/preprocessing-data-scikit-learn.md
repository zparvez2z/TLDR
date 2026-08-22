---
source_url: https://scikit-learn.org/stable/modules/preprocessing.html
author: scikit-learn Developers
date: 28-07-2026
source_version: scikit-learn 1.9.0
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original scikit-learn documentation; examples are simplified for personal learning.
difficulty: Intermediate
tags: [machine-learning, preprocessing, scaling, normalization, pipeline, data-preparation]
---

# Preprocessing Data

## TL;DR

Preprocessing turns raw data into a form that models can learn from more effectively. It includes scaling, standardization, normalization, encoding, binning, and feature transformations.

Good preprocessing must be learned from training data only, then applied consistently to validation, test, and future data.

## Core idea

Raw features often have different scales, formats, distributions, or meanings. Preprocessing makes them more usable.

```text
raw data → fitted transformer on training data → transformed data → model
```

The important rule:

```text
fit preprocessing on training data only
apply the same transformation to validation/test/new data
```

## Simple example

Suppose we predict apartment rent.

Raw features:

- size in square meters
- distance in kilometers
- building age
- city
- furnished/unfurnished

Preprocessing may include:

- scaling numerical features;
- encoding city as categorical data;
- creating distance bands;
- keeping the same transformation inside a pipeline.

## Key terms

- **Standardization**: transforms values to have roughly zero mean and unit variance.
- **Min-max scaling**: scales values into a fixed range.
- **Robust scaling**: scaling method less sensitive to outliers.
- **Normalization**: rescales individual samples, often to unit length.
- **Transformer**: an object that learns a transformation and applies it.
- **Pipeline**: connects preprocessing and modeling steps safely.
- **Data leakage**: when validation/test information influences training.

## Why it matters

Many algorithms are sensitive to feature scale. A feature measured in euros may dominate a feature measured from 0 to 1, even if it is not more important.

Preprocessing also prevents accidental leakage. For example, if you calculate scaling values using the full dataset before splitting, the model indirectly sees information from validation/test data.

## Common preprocessing tasks

- scale numeric features;
- normalize samples;
- transform skewed distributions;
- create polynomial or interaction features;
- bin continuous values;
- preserve sparse matrices when needed;
- combine preprocessing with a model in a pipeline.

## Common beginner mistakes

- Fitting scalers before splitting the data.
- Applying different transformations to train and test data.
- Centering sparse matrices and accidentally using too much memory.
- Scaling labels when only features should be scaled.
- Forgetting that tree-based models often need less scaling than linear models or neural networks.
- Treating preprocessing as a minor detail when it can strongly affect performance.

## When to use it

Use preprocessing whenever raw data is messy, differently scaled, sparse, skewed, incomplete, or not directly model-ready.

It is especially important for:

- linear models;
- logistic regression;
- SVMs;
- neural networks;
- distance-based models such as k-nearest neighbors;
- pipelines used in production.

## Mental model

Preprocessing is the bridge between real-world messy data and model-ready input. The model can only learn from the data representation you give it.

## Verification notes

- Verified against the original scikit-learn Preprocessing documentation on 2026-08-22.
- Source confirms that `sklearn.preprocessing` provides utility functions and transformer classes that change raw feature vectors into representations more suitable for downstream estimators.
- Source confirms standardization, scaling, robust handling of outliers, normalizers, and the importance of feature scale for many estimators.
- The apartment-rent example is adapted for personal learning.

## Related notes

- [Numerical Data](working-with-numerical-data-google-ml-crash-course.md)
- [Categorical Data](working-with-categorical-data-google-ml-crash-course.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Model Selection](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://scikit-learn.org/stable/modules/preprocessing.html