---
source_url: https://developers.google.com/machine-learning/crash-course/categorical-data
author: Google Developers
date: 25-08-2025
difficulty: Beginner
tags: [machine-learning, data-preparation, categorical-data, encoding, one-hot-encoding]
---

# Working with Categorical Data

## TL;DR

Categorical data represents values from a limited set of options, such as city, product type, browser, country, or payment method. Models usually cannot use raw category names directly, so categories must be encoded into numbers.

The key is to represent categories without inventing false numeric meaning.

## Core idea

Some values look like numbers but are really categories.

```text
Postal code 74072 is not mathematically larger than postal code 10115 in a meaningful ML sense.
```

Categorical features need encodings such as one-hot encoding, hashing, or embeddings.

## Simple example

Suppose we want to predict apartment rent.

Categorical features:

- city
- neighborhood
- heating type
- building type
- furnished or unfurnished

A model cannot directly learn from the word `Heilbronn`. We need to convert the category into a numerical representation.

## Key terms

- **Categorical feature**: a feature with values from a fixed or limited set.
- **Vocabulary**: the list of known category values.
- **One-hot encoding**: representing one category as a vector with one active value.
- **Sparse vector**: a vector with mostly zeros.
- **High cardinality**: a feature has many possible category values.
- **Hashing**: mapping categories into a fixed number of buckets.
- **Feature cross**: combining two or more categorical features into a new feature.

## Why it matters

Categorical data is common in real datasets. If encoded badly, the model may learn fake relationships.

For example, if cities are encoded as:

```text
Berlin = 1
Hamburg = 2
Munich = 3
```

a model may wrongly assume Munich is numerically greater than Berlin. One-hot encoding avoids that fake order.

## Common encoding options

### One-hot encoding

Best for smaller vocabularies.

Example:

```text
city = Heilbronn → [0, 1, 0, 0]
```

### Hashing

Useful when there are many possible categories or new values appear often.

Trade-off: different categories can collide into the same bucket.

### Embeddings

Useful for very large category spaces where similar categories should have similar learned representations.

## Common beginner mistakes

- Treating IDs, postal codes, or product numbers as normal numerical values.
- Creating huge one-hot vectors for high-cardinality features without considering memory cost.
- Forgetting about unseen categories at prediction time.
- Assuming every category has enough data to learn a reliable pattern.
- Creating feature crosses without checking if they improve validation performance.

## When to use it

Use categorical feature handling whenever the feature represents a type, group, name, label, ID, or membership instead of a measurable quantity.

## Mental model

Categorical encoding translates names into model-readable signals. The goal is to preserve useful identity information without adding fake mathematical meaning.

## Related notes

- [Numerical Data](working-with-numerical-data-google-ml-crash-course.md)
- [Feature Extraction](scikit-learn-feature-extraction.md)
- [Embeddings](embeddings-ml-crash-course.md)
- [Preprocessing Data](preprocessing-data-scikit-learn.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/categorical-data