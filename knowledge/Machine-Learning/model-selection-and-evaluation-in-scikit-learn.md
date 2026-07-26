---
source_url: https://scikit-learn.org/stable/model_selection.html
author: Unknown
date: 26-07-2026
---

# 3. Model selection and evaluation — scikit-learn 1.9.0 documentation

This scikit-learn User Guide chapter explains core techniques for evaluating and selecting machine learning models. It covers cross-validation strategies and how to compute robust performance metrics, along with statistical significance via permutation tests. It provides practical methods for hyperparameter tuning, including grid search, randomized search, and successive halving, as well as guidance on decision-threshold tuning for classifiers. The chapter also details the scoring API, a wide range of evaluation metrics, and tools like validation and learning curves for diagnosing model behavior.
- Cross-validation fundamentals: computing cross-validated metrics, choosing iterators (e.g., KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit), and shuffling considerations.
- Model selection with CV: GridSearchCV, RandomizedSearchCV, and successive halving (HalvingGridSearchCV/HalvingRandomSearchCV), plus tips to improve efficiency and avoid overfitting.
- Alternatives to brute-force parameter search and practical advice for effective hyperparameter optimization.
- Decision threshold tuning for classification to align with precision/recall or cost objectives.
- Scoring API overview and metric selection guidance for classification, multilabel ranking, regression, and clustering; using dummy estimators for baselines.
- Validation and learning curves to visualize bias-variance trade-offs and data sufficiency.
- Permutation test score to assess the statistical significance of model performance.