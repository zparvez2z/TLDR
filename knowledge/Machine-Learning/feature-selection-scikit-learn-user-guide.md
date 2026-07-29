---
source_url: https://scikit-learn.org/stable/modules/feature_selection.html
author: Unknown
date: 29-07-2026
---

# 1.13. Feature selection — scikit-learn 1.9.0 documentation

scikit-learn's feature_selection module provides tools to reduce dimensionality and improve model performance by removing irrelevant or redundant features. It covers filter methods like VarianceThreshold, univariate statistical tests, wrapper methods such as recursive feature elimination (RFE/RFECV), and model-based selection via SelectFromModel, including L1-regularized models. The guide explains appropriate scoring functions for regression and classification, handling of sparse matrices, and thresholding heuristics for selecting features. These techniques can be combined with hyperparameter search and cross-validation to find the optimal subset of features.
- VarianceThreshold removes features below a variance threshold (default: zero variance); boolean-feature example uses variance p*(1−p).
- Univariate selectors: SelectKBest, SelectPercentile, GenericUnivariateSelect with scoring functions (regression: r_regression, f_regression, mutual_info_regression; classification: chi2, f_classif, mutual_info_classif); chi2 requires non-negative features; do not mix regression scores with classification tasks.
- Sparse data compatibility: chi2 and mutual information functions operate on sparse matrices without densifying.
- RFE iteratively removes least important features; RFECV selects the optimal number of features via cross-validation and a chosen scorer.
- SelectFromModel uses feature importances (coef_, feature_importances_, or callable) with numeric thresholds or heuristics ("mean", "median", or scaled forms like "0.1*mean") and optional max_features.
- L1-based selection via Lasso (regression) and LogisticRegression/LinearSVC (classification): smaller C yields sparser logistic/SVM models; larger alpha yields sparser Lasso; notes on conditions for exact recovery and tuning alpha via cross-validation.