---
source_url: https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses
author: Unknown
date: 24-07-2026
---

# Categorical data: Feature crosses | Machine Learning | Google for Developers

Feature crosses combine two or more categorical or bucketed features by taking their Cartesian product, enabling linear models to capture nonlinear interactions. They are analogous to polynomial transforms for numerical data but operate on categorical inputs, producing new sparse features that represent feature interactions. Effective crosses often rely on domain expertise, while neural networks can automatically learn useful combinations during training. Overuse, especially with high-cardinality sparse inputs, can cause combinatorial explosion and increase computational cost.