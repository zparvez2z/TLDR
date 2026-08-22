---
source_url: https://developers.google.com/machine-learning/crash-course/neural-networks
author: Google Developers
date: 15-07-2026
difficulty: Intermediate
tags: [machine-learning, neural-networks, deep-learning, nonlinear-models, backpropagation]
---

# Neural Networks

## TL;DR

Neural networks are models that learn complex, nonlinear patterns by combining many simple computation units across layers. They are useful when linear models are too limited.

Neural networks still follow the same ML loop: features, predictions, loss, training, and evaluation.

## Core idea

A neural network transforms input features through layers.

```text
input features → hidden layer(s) → output prediction
```

Each layer learns intermediate representations. Earlier layers learn simpler patterns, and later layers combine them into more useful signals.

## Simple example

Suppose we want to predict whether an image contains a cat.

A simple linear model may struggle because the relationship between pixels and "cat" is very complex.

A neural network can learn patterns in stages:

```text
edges → shapes → fur/ears/eyes → cat-like object
```

The model does not need humans to manually write every visual rule.

## Key terms

- **Neuron/node**: a computation unit that combines inputs and produces an output.
- **Layer**: a group of nodes.
- **Hidden layer**: a layer between input and output.
- **Activation function**: adds nonlinearity so the network can learn complex patterns.
- **Weights and biases**: learned parameters of the network.
- **Forward pass**: computing predictions from inputs.
- **Backpropagation**: calculating how to adjust weights to reduce loss.
- **Deep learning**: neural networks with multiple layers.

## Why it matters

Neural networks can learn patterns that are hard to express manually. They are important for image recognition, speech, language models, recommendations, and many modern AI systems.

But they are not magic. They need data, careful training, evaluation, and regularization.

## When to use it

Neural networks are useful when:

- relationships are nonlinear;
- input data is complex, such as images, audio, text, or high-dimensional signals;
- there is enough data and compute;
- simpler models do not perform well enough;
- learned representations are useful.

They may not be the best first choice when:

- the dataset is small;
- interpretability is very important;
- a simple model already works well;
- training resources are limited.

## Common beginner mistakes

- Starting with neural networks before building a simple baseline.
- Thinking more layers always means better performance.
- Ignoring overfitting.
- Forgetting to scale or preprocess inputs.
- Using the training score as proof that the network works.
- Not understanding that neural networks can be difficult to debug.

## Mental model

A neural network is a stack of learned transformations. Each layer reshapes the data into a representation that makes the final prediction easier.

## Related notes

- [Linear Regression](linear-regression-google-ml-crash-course.md)
- [Logistic Regression](logistic-regression-google-ml-crash-course.md)
- [Overfitting and Generalization](datasets-generalization-and-overfitting-ml-crash-course.md)
- [Regularization](overfitting-l2-regularization.md)
- [Embeddings](embeddings-ml-crash-course.md)

## Source

Original source: https://developers.google.com/machine-learning/crash-course/neural-networks