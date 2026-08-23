# Machine Learning Learning Path

This page is the study guide for the Machine Learning section of TLDR.

The Machine Learning folder now contains **42 source-reviewed notes**. The goal of this page is to make those notes usable as a learning path instead of leaving them as a flat list of files.

Use this page in two ways:

1. Follow the beginner path if you are learning machine learning step by step.
2. Jump to the applied or research sections if you already know the basics.

```text
Current status: 42 ML notes, 42 source-reviewed, 0 unverified notes
Last learning-path update: 2026-08-23
```

---

## How to study from this folder

A good study loop is:

```text
Read one note → understand the example → check common mistakes → connect it to the next note
```

Do not read the research papers first. Build the foundation first, then move to LLMs, agents, and specialized AI systems.

---

## Recommended beginner route

This is the best route if you want to learn ML in a clean order:

```text
Machine Learning Crash Course Roadmap
→ Introduction to Machine Learning
→ Getting Started with scikit-learn
→ Linear Regression
→ Logistic Regression
→ Classification
→ Dividing Datasets
→ Metrics and Scoring
→ Overfitting and Generalization
→ Regularization
→ Numerical Data
→ Categorical Data
→ Feature Crosses
→ Preprocessing Data
→ Feature Selection
→ Feature Extraction
→ Model Selection and Evaluation
→ Neural Networks
→ Embeddings
→ Introduction to Large Language Models
```

---

## 1. Start here

These notes explain the overall map and basic vocabulary.

1. [Machine Learning Crash Course Roadmap](machine-learning-crash-course-google-developers.md)  
   Use this as the map for the core Google ML Crash Course topics.

2. [Introduction to Machine Learning](introduction-to-machine-learning-google-for-developers.md)  
   Learn the basic vocabulary: features, labels, model, training, prediction, evaluation, and metrics.

3. [Getting Started with scikit-learn](getting-started-with-scikit-learn.md)  
   Learn the practical scikit-learn workflow: estimators, `fit`, `predict`, transformers, pipelines, and cross-validation.

---

## 2. Core supervised learning

These notes explain the first model types and how predictions become decisions.

4. [Linear Regression](linear-regression-google-ml-crash-course.md)  
   Predict continuous numeric values such as price, rent, temperature, or demand.

5. [Logistic Regression](logistic-regression-google-ml-crash-course.md)  
   Predict probabilities for binary classification problems.

6. [Classification: Thresholds and Metrics](classification-binary-thresholds-and-metrics.md)  
   Convert probabilities into class decisions and understand false positives, false negatives, precision, recall, ROC, and AUC.

Recommended order:

```text
Linear Regression → Logistic Regression → Classification
```

---

## 3. Evaluation and generalization

These notes explain how to know whether a model is actually useful on new data.

7. [Dividing Datasets into Training, Validation, and Test Sets](dividing-datasets-into-training-validation-and-test-sets.md)  
   Learn why training, validation, and test sets should have different jobs.

8. [Metrics and Scoring](scikit-learn-metrics-and-scoring.md)  
   Learn how to choose the right metric for classification, regression, probability quality, and model selection.

9. [Datasets, Generalization, and Overfitting](datasets-generalization-and-overfitting-ml-crash-course.md)  
   Learn why a model can perform well on training data but fail on unseen examples.

10. [Regularization: L2 and Early Stopping](overfitting-l2-regularization.md)  
    Learn how to reduce overfitting by controlling model complexity.

11. [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)  
    Learn cross-validation, hyperparameter tuning, validation curves, learning curves, and final testing.

Recommended order:

```text
Dividing Datasets → Metrics → Overfitting → Regularization → Model Selection
```

---

## 4. Data preparation and features

These notes explain how raw data becomes useful model input.

12. [Working with Numerical Data](working-with-numerical-data-google-ml-crash-course.md)  
    Learn how to clean, scale, bin, and transform numerical features.

13. [Working with Categorical Data](working-with-categorical-data-google-ml-crash-course.md)  
    Learn how to represent categories without inventing false numeric meaning.

14. [Categorical Data: Feature Crosses](categorical-data-feature-crosses.md)  
    Learn how feature crosses help simple models capture interactions between categorical or bucketed features.

15. [Preprocessing Data](preprocessing-data-scikit-learn.md)  
    Learn scaling, normalization, encoding, transformations, and safe use of pipelines.

16. [Feature Selection](feature-selection-scikit-learn-user-guide.md)  
    Learn how to remove weak, irrelevant, or redundant features.

17. [Feature Extraction](scikit-learn-feature-extraction.md)  
    Learn how to turn raw text, dictionaries, and other objects into numeric feature vectors.

Recommended order:

```text
Numerical Data → Categorical Data → Feature Crosses → Preprocessing → Feature Selection → Feature Extraction
```

---

## 5. Applied ML topics

These notes connect the foundations to real ML products and practical ML workflows.

18. [Recommendation Systems: Introduction](recommendation-systems-introduction-google-developers.md)  
    Learn candidate generation, scoring, ranking, embeddings, collaborative filtering, and matrix factorization.

19. [Production ML Systems](production-ml-systems.md)  
    Learn why production ML is more than a model: data pipelines, serving, monitoring, testing, and train-serving skew.

20. [Automated Machine Learning (AutoML)](automated-machine-learning-automl.md)  
    Learn what AutoML can automate and why human understanding of data and metrics still matters.

21. [Fairness in Machine Learning](ml-fairness-crash-course-module.md)  
    Learn why model evaluation should include bias and fairness checks, not only accuracy or loss.

22. [Neural Architecture Search](neural-architecture-search.md)  
    Learn how AutoML can search over neural network architectures using search spaces, strategies, and performance estimation.

---

## 6. Neural networks and LLM foundations

These notes introduce modern deep learning and language-model concepts.

23. [Neural Networks](neural-networks-google-ml-crash-course.md)  
    Learn how layers, activations, weights, biases, forward passes, and backpropagation work conceptually.

24. [Embeddings](embeddings-ml-crash-course.md)  
    Learn how items, words, users, or categories can be represented as dense vectors.

25. [Introduction to Large Language Models](introduction-to-large-language-models.md)  
    Learn tokens, context, next-token prediction, transformers, self-attention, prompts, fine-tuning, and limitations.

Recommended order:

```text
Neural Networks → Embeddings → LLM Introduction
```

---

## 7. LLM evaluation, reasoning, and context research

These are advanced notes. Read them after the foundation path.

26. [LLM Evaluation Metrics](llm-evaluation-metrics-everything-you-need.md)  
    Practitioner guide to traditional NLP metrics, LLM-as-a-judge evaluation, faithfulness, relevance, and context quality.

27. [A Survey of Context Engineering for Large Language Models](survey-of-context-engineering-for-llms.md)  
    Survey of context retrieval, generation, processing, management, RAG, memory systems, tools, and multi-agent context use.

28. [Reasoning Language Models: A Blueprint](reasoning-language-models-a-blueprint.md)  
    Research blueprint for reasoning structures, search, reinforcement learning, test-time compute, and agentic reasoning.

29. [Evaluation Is All You Need: Strategic Overclaiming of LLM Reasoning Capabilities](evaluation-is-all-you-need-strategic-overclaiming-llm-capabilities.md)  
    Research note on how benchmark-design choices can change reasoning-model scores and create misleading claims.

30. [Tracing the “Thoughts” of a Language Model](tracing-thoughts-language-model.md)  
    Interpretability note on tracing internal concepts and information flow inside language models.

31. [Conformal Language Modeling](conformal-language-modeling.md)  
    Research note on uncertainty, candidate answer sets, coverage guarantees, and reducing hallucination risk.

32. [Adam’s Law: Textual Frequency Law on Large Language Models](adams-law-textual-frequency-llms.md)  
    Research note on sentence-level textual frequency and its effect on prompting, fine-tuning, and LLM performance.

---

## 8. Agents and multi-agent systems

These notes focus on LLM agents, tool use, skill evolution, and multi-agent collaboration.

33. [MUSE-Autoskill: Self-Evolving Agents](muse-autoskill-self-evolving-agents-skill-lifecycle.md)  
    Research note on skill creation, memory, management, evaluation, refinement, and cross-agent skill transfer.

34. [Large-Scale Study on Multi-Agent AI Systems](large-scale-study-multi-agent-ai-systems.md)  
    Research note on development issues in real open-source multi-agent AI systems.

35. [Step-Level Optimization for Efficient Computer-Use Agents](step-level-optimization-efficient-computer-use-agents.md)  
    Research note on routing between small and large models at risky GUI-action steps.

36. [SkillClaw: Collective Skill Evolution](skillclaw-collective-skill-evolution-agentic-evolver.md)  
    Research note on collecting user-agent trajectories and evolving shared reusable skills.

37. [Towards Uncertainty-Aware Language Agent](towards-uncertainty-aware-language-agent.md)  
    Research note on using uncertainty estimation to decide when an agent should call tools.

38. [Heterogeneous Scientific Foundation Model Collaboration](heterogeneous-scientific-foundation-model-collaboration.md)  
    Research note on connecting LLM agents with domain-specific scientific foundation models.

39. [GrandCode: Agentic RL for Competitive Programming](grandcode-agentic-rl-competitive-programming.md)  
    Research note on multi-agent reinforcement learning for competitive programming.

---

## 9. AI systems and specialized ML notes

These notes are useful but more specialized. They are not required for the beginner path.

40. [Inside NVIDIA GPUs: High-Performance Matmul Kernels](inside-nvidia-gpus-high-performance-matmul-kernels.md)  
    Technical note on GPU architecture and matrix multiplication kernels, important for understanding deep-learning compute.

41. [InCoder-32B: Code Foundation Model for Industrial Scenarios](incoder-32b-code-foundation-model-for-industrial-scenarios.md)  
    Research note on an industrial code foundation model for chip design, GPU optimization, embedded systems, compilers, and 3D modeling.

42. [NeuroSym-BioCAT: Biomedical Document Categorization and Question Answering](neurosym-biocat-biomedical-document-categorization.md)  
    Research note on biomedical document categorization and answer extraction using optimized topic modeling and MiniLM.

---

## Suggested routes by goal

### Learn ML basics

```text
Roadmap → Intro to ML → Linear Regression → Logistic Regression → Classification → Metrics → Overfitting → Regularization
```

### Build practical scikit-learn workflows

```text
Getting Started with scikit-learn → Preprocessing → Feature Selection → Feature Extraction → Model Selection
```

### Understand ML data preparation

```text
Numerical Data → Categorical Data → Feature Crosses → Preprocessing → Feature Extraction
```

### Understand LLMs from ML basics

```text
Neural Networks → Embeddings → LLM Introduction → LLM Evaluation Metrics → Context Engineering
```

### Study LLM agents

```text
LLM Introduction → Context Engineering → Reasoning Language Models → MUSE-Autoskill → SkillClaw → UALA → Eywa
```

### Explore AI systems and infrastructure

```text
Neural Networks → Embeddings → Inside NVIDIA GPUs → InCoder-32B → GrandCode
```

---

## Maintenance rules

When adding a new Machine Learning note:

1. Verify it against the original source before marking it trusted.
2. Add `verified_against_source: true` only after source review.
3. Add the note to this page only if it helps the learning path.
4. Keep beginner notes separate from advanced research notes.
5. Remove or flag any note with a wrong or missing source.

This folder should stay useful for learning, not just collecting links.
