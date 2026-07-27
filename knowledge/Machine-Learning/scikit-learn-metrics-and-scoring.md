---
source_url: https://scikit-learn.org/stable/modules/model_evaluation.html
author: Unknown
date: 27-07-2026
---

# 3.4. Metrics and scoring: quantifying the quality of predictions — scikit-learn 1.9.0 documentation

This guide explains how to evaluate model predictions in scikit-learn and how to choose appropriate scoring functions. It distinguishes between prediction (probabilistic or point estimates) and decision making, recommending strictly consistent scoring functions aligned with the target functional. The page lists consistent scoring rules for common functionals (mean, median, quantiles) across classification and regression, and illustrates their use with a practical example. It also overviews scikit-learn’s scoring APIs, including estimator score methods, the scoring parameter in model-selection tools, and standalone metric functions.
- Guidance on choosing a scoring function that matches the ultimate goal and target functional (consistency as the key principle)
- Distinction between predicting and decision making; use of thresholds and confusion-matrix-derived measures for classification decisions
- Examples of strictly consistent scoring functions: Brier score, log loss, zero-one loss (consistent but not strictly), MSE, MAE, pinball loss (quantiles), and Poisson/Gamma/Tweedie deviance
- Recommendation to use the same strictly consistent scoring function for training and evaluation when possible
- Overview of scoring interfaces: estimator.score, the scoring parameter for cross-validation and model selection, and sklearn.metrics functions; Dummy estimators for baselines
- References to foundational work (Gneiting, Raftery, Fissler) on proper and consistent scoring rules