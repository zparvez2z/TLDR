---
source_url: https://developers.google.com/machine-learning/crash-course/categorical-data
author: Unknown
date: 25-08-2025
---

# Working with categorical data | Machine Learning | Google for Developers

This module explains how to identify and represent categorical features so they can be used effectively in machine learning models. It contrasts categorical data with numerical data, emphasizing when seemingly numeric fields (such as postal codes) should be treated as categories. The course covers encoding methods—especially one-hot encoding and hashing—along with common pitfalls like high cardinality and unseen categories. It also introduces feature crosses to capture interactions between categorical features.
- Distinguish categorical data (finite set of values) from true numerical data (supports meaningful multiplication).
- Use one-hot encoding to transform categories into model-trainable vectors; consider hashing for high-cardinality features.
- Treat certain integer fields (for example, postal codes or binned values) as categorical to avoid misleading numeric relationships.
- Anticipate issues such as sparsity, unseen categories, and memory/compute costs with large vocabularies.
- Create feature crosses to model interactions between categorical features and improve predictive power.