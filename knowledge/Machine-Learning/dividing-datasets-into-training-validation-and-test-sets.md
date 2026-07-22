---
source_url: https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets
author: Unknown
date: 03-12-2025
---

# Datasets: Dividing the original dataset | Machine Learning | Google for Developers

This page explains why machine learning models must be evaluated on data different from the training data and recommends splitting datasets into training, validation, and test sets. The validation set supports iterative model development and hyperparameter tuning, while the test set is reserved for final evaluation. Reusing the same validation or test sets too often can degrade their reliability, so periodically refreshing them with new data is advised. It also emphasizes removing duplicates between training and evaluation sets and ensuring that evaluation data is statistically significant and representative of both the overall dataset and real-world conditions.
- Use three subsets: training (fit the model), validation (tune and iterate), and test (final, unbiased evaluation).
- Do not evaluate on training examples; always test on different data to assess generalization.
- Avoid overusing the same validation/test sets; refresh them to maintain trustworthy assessments.
- Remove any duplicates from validation/test that also appear in training to prevent data leakage.
- Ensure test sets are large enough, representative of the dataset distribution, and aligned with real-world data the model will encounter.
- Address mismatches between training/testing data and real-world data to achieve satisfactory production performance.