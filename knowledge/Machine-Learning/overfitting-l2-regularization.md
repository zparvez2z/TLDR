---
source_url: https://developers.google.com/machine-learning/crash-course/overfitting/regularization
author: Unknown
date: 09-04-2026
---

# Overfitting: L2 regularization | Machine Learning | Google for Developers

L2 regularization reduces overfitting by adding a penalty proportional to the squared magnitude of model weights to the training objective. The regularization rate (lambda) scales this penalty, with higher values leading to simpler models and lower values increasing the risk of overfitting. Early stopping is an alternative that halts training based on validation performance rather than explicitly penalizing complexity. Achieving good generalization requires tuning both the regularization rate and the learning rate, which influence weights in opposite directions.

- L2 penalizes large weights most strongly; small weights contribute little, encouraging weights toward (but not exactly) zero.
- Training minimizes loss plus lambda times model complexity (loss + λ·complexity).
- High lambda strengthens regularization, typically yielding a near-normal weight histogram centered at 0 and reducing overfitting risk.
- Low lambda weakens regularization, often producing flatter weight histograms and higher overfitting risk.
- The ideal regularization rate is data-dependent and must be tuned using validation data.
- Early stopping can lower test loss even if training loss rises, but it is quick rather than optimal compared to tuning lambda.
- Learning rate and regularization rate must be balanced: high learning rates pull weights away from zero, while high regularization pushes them toward zero; changing one often requires retuning the other.