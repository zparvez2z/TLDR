# Machine Learning Learning Path

This page is the study guide for the Machine Learning section of TLDR.

The goal is not to read random notes. The goal is to move step by step: first understand the basic ML vocabulary, then simple models, then data preparation, then model quality, and finally more advanced topics like neural networks, embeddings, and large language models.

## How to use this path

Read the notes in order if you are learning from the beginning. Use the groups below if you want to revise a specific area.

A simple study loop:

```text
Read one note → understand the example → remember the common mistakes → connect it to the next note
```

---

## 1. Start here

These notes explain what machine learning is and how the rest of the section is organized.

1. [Machine Learning Crash Course Roadmap](machine-learning-crash-course-google-developers.md)  
   Use this as the map for the full ML foundation path.

2. [Introduction to Machine Learning](introduction-to-machine-learning-google-for-developers.md)  
   Learn the core vocabulary: features, labels, model, training, prediction, evaluation, and metrics.

---

## 2. First supervised learning models

These notes explain the first model types and how predictions are made.

3. [Linear Regression](linear-regression-google-ml-crash-course.md)  
   Predict numeric values such as price, rent, temperature, or demand.

4. [Logistic Regression](logistic-regression-google-ml-crash-course.md)  
   Predict probabilities for binary outcomes, such as spam/not spam or churn/not churn.

5. [Classification](classification-binary-thresholds-and-metrics.md)  
   Convert probabilities into class decisions and understand classification errors.

Recommended order:

```text
Linear Regression → Logistic Regression → Classification
```

---

## 3. Data preparation

These notes explain how raw data becomes useful model input.

6. [Working with Numerical Data](working-with-numerical-data-google-ml-crash-course.md)  
   Learn how to clean, scale, bin, and transform numeric features.

7. [Working with Categorical Data](working-with-categorical-data-google-ml-crash-course.md)  
   Learn how to represent categories such as city, product type, or user group.

8. [Preprocessing Data](preprocessing-data-scikit-learn.md)  
   Learn practical preprocessing tools such as scaling, normalization, encoding, and transformations.

9. [Feature Selection](feature-selection-scikit-learn-user-guide.md)  
   Learn how to remove weak, irrelevant, or redundant features.

10. [Feature Extraction](scikit-learn-feature-extraction.md)  
    Learn how to turn raw inputs such as text or dictionaries into numeric features.

Recommended order:

```text
Numerical Data → Categorical Data → Preprocessing → Feature Selection → Feature Extraction
```

---

## 4. Model quality and generalization

These notes explain how to know whether a model is actually good.

11. [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)  
    Learn why a model can perform well on training data but fail on new data.

12. [Regularization](overfitting-l2-regularization.md)  
    Learn how to reduce overfitting by controlling model complexity.

13. [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)  
    Learn how to choose the right measurement for the problem.

14. [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)  
    Learn how to compare models, tune hyperparameters, and test fairly.

Recommended order:

```text
Overfitting → Regularization → Metrics → Model Selection
```

---

## 5. Advanced foundations

These notes introduce more powerful model types and modern ML ideas.

15. [Neural Networks](neural-networks-google-ml-crash-course.md)  
    Learn how layered models capture nonlinear patterns.

16. [Embeddings](embeddings-ml-crash-course.md)  
    Learn how items, words, or categories can be represented as dense vectors.

17. [Introduction to Large Language Models](introduction-to-large-language-models.md)  
    Learn how language models predict tokens and why LLMs are powerful but imperfect.

Recommended order:

```text
Neural Networks → Embeddings → LLM Introduction
```

---

## Suggested beginner route

For a beginner, the most important path is:

```text
ML Roadmap
→ Introduction to ML
→ Linear Regression
→ Logistic Regression
→ Classification
→ Numerical Data
→ Categorical Data
→ Overfitting
→ Regularization
→ Metrics and Scoring
→ Model Selection
→ Neural Networks
→ Embeddings
→ LLM Introduction
```

## Suggested practical scikit-learn route

For practical model building with scikit-learn:

```text
Preprocessing Data
→ Feature Selection
→ Feature Extraction
→ Metrics and Scoring
→ Model Selection and Evaluation
```

## Suggested LLM foundation route

For understanding LLMs from ML basics:

```text
Introduction to ML
→ Classification
→ Neural Networks
→ Embeddings
→ LLM Introduction
```

---

## What is not covered deeply yet

The foundation path is now strong, but the section can still be improved with deeper notes on:

- train/validation/test split examples;
- confusion matrix examples;
- hands-on scikit-learn pipelines;
- decision trees and ensemble methods;
- clustering and dimensionality reduction;
- real ML project workflow;
- model deployment and monitoring.

## Maintenance note

When adding new Machine Learning notes, connect them to this page if they are part of the main learning path. Research papers and advanced topics can stay outside the beginner path unless they help explain a core concept.
