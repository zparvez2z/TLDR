---
source_url: https://en.wikipedia.org/wiki/Neural_architecture_search
author: Wikipedia contributors
date: 2025-07-01
source_type: encyclopedia
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the Wikipedia article; this note is a general concept overview and should later be strengthened with a primary survey source.
difficulty: Intermediate
tags: [machine-learning, neural-architecture-search, automl, deep-learning, model-design]
category_review: keep_in_machine_learning_as_automl-concept-note
source_quality_note: Wikipedia is useful for orientation, but a stronger source would be a NAS survey paper.
---

# Neural Architecture Search

## TL;DR

Neural Architecture Search (NAS) automates the design of neural-network architectures. Instead of manually choosing layers and connections, NAS searches through possible architectures and evaluates which ones work best.

NAS is a subfield of AutoML.

## Core idea

NAS usually has three main parts:

```text
search space → search strategy → performance estimation
```

- **Search space** defines what kinds of architectures can be considered.
- **Search strategy** decides how to explore possible architectures.
- **Performance estimation** estimates how good an architecture is without always fully training every candidate from scratch.

## Simple example

Suppose we want to design an image-classification model.

Instead of manually deciding:

- number of layers;
- convolution sizes;
- skip connections;
- pooling choices;
- channel sizes;

NAS tries many possible designs and searches for one that performs well under the chosen constraints.

## Common search strategies

### Reinforcement learning

A controller proposes architectures and receives rewards based on validation performance.

### Evolutionary search

Architectures are mutated and selected over generations, similar to evolutionary algorithms.

### Bayesian optimization

A surrogate model predicts which architecture candidates are promising, reducing unnecessary evaluations.

### Differentiable / one-shot NAS

A large supernetwork shares weights across many candidate architectures, reducing the cost of evaluating each candidate separately.

## Why it matters

NAS can discover architectures that are competitive with manually designed networks. It can also optimize for practical constraints such as accuracy, latency, memory, or model size.

This matters for deployment because the best model is not always the most accurate one. Sometimes the best model is the one that balances accuracy with speed and resource usage.

## Limitations

- NAS can be computationally expensive.
- Results depend heavily on the chosen search space.
- Search results may not transfer well across datasets or hardware.
- Benchmarks and weight-sharing methods can introduce bias.
- Wikipedia is not a primary source, so this note should eventually be verified against a NAS survey paper.

## My takeaway

NAS is AutoML applied to model architecture design. The key question is not only “Can we find a good network?” but also “Can we search efficiently and evaluate fairly?”

## Related notes

- [Automated Machine Learning](automated-machine-learning-automl.md)
- [Neural Networks](neural-networks-google-ml-crash-course.md)
- [Model Selection and Evaluation](model-selection-and-evaluation-in-scikit-learn.md)

## Source

Original source: https://en.wikipedia.org/wiki/Neural_architecture_search
