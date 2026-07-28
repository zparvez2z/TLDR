---
source_url: https://scikit-learn.org/stable/modules/preprocessing.html
author: Unknown
date: 28-07-2026
---

# 8.3. Preprocessing data — scikit-learn 1.9.0 documentation

The scikit-learn preprocessing module provides utilities and transformers to convert raw feature vectors into forms better suited for machine learning estimators. It emphasizes feature scaling and standardization, offering methods tailored for dense, sparse, and outlier-prone data. The guide also covers normalization, kernel matrix centering, and various feature engineering transforms, all following the fit/transform API for seamless use in Pipelines. Practical notes and examples highlight when and how to use each scaler or transformer, and common pitfalls such as centering sparse data.
- Standardization with StandardScaler (optionally disabling centering or scaling) to promote stable learning for many estimators.
- Scaling to fixed ranges using MinMaxScaler and unit-max scaling with MaxAbsScaler, particularly useful for sparse or zero-centered data.
- Guidance for sparse inputs: avoid centering; use MaxAbsScaler or StandardScaler with with_mean=false; RobustScaler can transform (not fit) on sparse data.
- RobustScaler for datasets with outliers; consider PCA with whiten=True to reduce feature correlation.
- KernelCenterer to center Gram/kernel matrices without explicit feature mapping, preserving kernel algebra.
- Normalization and non-linear transforms (e.g., QuantileTransformer, PowerTransformer, FunctionTransformer) to address skewed distributions.
- Feature engineering tools such as KBinsDiscretizer, PolynomialFeatures, and SplineTransformer for discretization and interaction terms.
- Categorical encoding options (e.g., OneHotEncoder, OrdinalEncoder, LabelEncoder) compatible with the Pipeline API.
- Fit on training data and apply the same learned transformation to test data; inspect transformer attributes to understand learned parameters.
- Avoid breaking sparsity and excessive memory usage by choosing appropriate scalers and sparse matrix formats (CSR/CSC).