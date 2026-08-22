---
source_url: https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses
author: Google Developers
date: 24-07-2026
source_last_updated: 2025-08-25
verified_against_source: true
verified_date: 2026-08-22
verification_scope: Checked against the original Google Developers page; examples are simplified for personal learning.
difficulty: Beginner
tags: [machine-learning, categorical-data, feature-crosses, feature-engineering, linear-models]
---

# Categorical Data: Feature Crosses

## TL;DR

A feature cross combines two or more categorical or bucketed features into a new feature. It helps a model learn interactions between features that might be difficult for a simple linear model to learn otherwise.

Feature crosses can be powerful, but they can also create very large sparse feature spaces.

## Core idea

A feature cross is created by taking combinations of feature values.

```text
feature A × feature B → new crossed feature
```

For example:

```text
city × property_type
```

could create crossed features such as:

```text
Heilbronn_apartment
Heilbronn_room
Stuttgart_apartment
Stuttgart_room
```

This lets a model learn that the meaning of one feature may depend on another feature.

## Simple example

Suppose we want to predict apartment rent.

Separately, these features are useful:

- city
- apartment type

But their combination may be more useful:

```text
city = Munich + apartment_type = studio
city = Heilbronn + apartment_type = WG room
```

The rent pattern for a studio in Munich may be very different from a WG room in Heilbronn. A feature cross helps the model represent that interaction.

## Key terms

- **Feature cross**: a synthetic feature created by combining two or more categorical or bucketed features.
- **Cartesian product**: all possible combinations of values from crossed features.
- **Feature interaction**: when the effect of one feature depends on another feature.
- **Sparse feature**: a feature representation with many zeros.
- **Bucketed feature**: a numerical feature converted into ranges, then treated like a category.
- **Synthetic feature**: a new feature created from existing features.

## Why it matters

Linear models are simple and useful, but they may miss interactions between features. Feature crosses let linear models represent some nonlinear behavior without changing the model family.

The official Google lesson compares this idea to polynomial transforms: polynomial transforms combine numerical features, while feature crosses combine categorical or bucketed features.

## When to use feature crosses

Use feature crosses when:

- domain knowledge suggests a useful interaction;
- two categorical features together are more meaningful than either alone;
- a linear model is too simple without interactions;
- bucketed numerical features should interact with categories.

Examples:

```text
city × property_type
country × language
device_type × browser
age_bucket × product_category
```

## Common beginner mistakes

- Crossing too many features without a reason.
- Crossing high-cardinality sparse features and creating a huge feature space.
- Assuming all feature combinations have enough training examples.
- Creating crosses without checking validation performance.
- Forgetting that neural networks can sometimes learn useful feature combinations automatically.

## Practical warning

Crossing two sparse features can create an even larger sparse feature. For example, crossing a 100-value feature with a 200-value feature can produce up to 20,000 crossed feature values.

That can increase memory use, training cost, and overfitting risk.

## Mental model

A feature cross is like saying: "Do not look at these features separately only. Also look at what happens when they appear together."

## Related notes

- [Working with Categorical Data](working-with-categorical-data-google-ml-crash-course.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Neural Networks](neural-networks-google-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses
