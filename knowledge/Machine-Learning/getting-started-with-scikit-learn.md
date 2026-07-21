---
source_url: https://scikit-learn.org/stable/getting_started.html
author: Unknown
date: 21-07-2026
---

# Getting Started — scikit-learn 1.9.0 documentation

This guide introduces the core concepts and workflow of scikit-learn, an open-source machine learning library. It explains how estimators are fitted with data (X, y) and used to predict on new data. The guide covers transformers for preprocessing, the use of ColumnTransformer for column-wise operations, and how to chain steps with Pipelines to avoid data leakage. It also demonstrates model evaluation with train/test splits and cross-validation, and shows how to tune hyperparameters using automated search. Additional resources point to the User Guide, API Reference, and examples for deeper learning.
- Estimators: fit/predict API; X shaped (n_samples, n_features) and 1D y; supports NumPy arrays and sparse matrices.
- Transformers and preprocessing: transform API; use ColumnTransformer for applying different transformations to different features.
- Pipelines: chain preprocessing and estimators with a unified fit/predict API; helps prevent data leakage; prefer searching over pipelines during CV.
- Model evaluation: use train_test_split, cross_validate, custom scorers, and flexible data splitting strategies.
- Hyperparameter search: RandomizedSearchCV (and related tools) to find best parameters (e.g., n_estimators, max_depth) via cross-validation.
- Next steps: consult the User Guide, API Reference, examples, and external learning resources.