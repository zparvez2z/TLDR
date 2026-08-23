---
source_url: https://www.aleksagordic.com/blog/matmul
author: Aleksa Gordić
date: 29-09-2025
source_type: technical_blog
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original blog post; this note summarizes the GPU architecture and matmul-kernel optimization path for personal learning.
difficulty: Advanced
tags: [machine-learning, gpu-programming, cuda, matrix-multiplication, tensor-cores, performance]
category_review: keep_in_machine_learning_as_ai-systems-note
---

# Inside NVIDIA GPUs: High-Performance Matmul Kernels

## TL;DR

This article explains how high-performance matrix multiplication kernels are built on NVIDIA GPUs, especially Hopper H100. It connects GPU hardware, memory hierarchy, CUDA programming, PTX/SASS, warp tiling, Tensor Cores, TMA, and asynchronous pipelines.

This is not a beginner ML note. It belongs in the ML section because modern neural networks and Transformers spend much of their compute inside matrix multiplications.

## Problem

Matrix multiplication is one of the most important operations in deep learning. Training and inference for Transformers depend heavily on matmuls in attention projections, MLP layers, and output projections.

The problem is that a naive GPU matmul does not automatically reach high performance. The kernel must carefully use the GPU memory hierarchy and compute units.

## Core idea

Fast GPU kernels are built by reducing slow memory traffic and keeping specialized compute units busy.

```text
slow global memory → shared memory/registers → Tensor Cores → high throughput
```

The article builds the explanation step by step:

1. Understand NVIDIA GPU architecture.
2. Understand CUDA execution and memory hierarchy.
3. Understand PTX/SASS and what the compiler generates.
4. Build better matmul kernels using tiling.
5. Use Hopper features such as Tensor Cores, WGMMA, and TMA.
6. Overlap data movement and computation with asynchronous pipelines.

## Key technical ideas

- **Global memory (GMEM)** is large but slow compared with on-chip memory.
- **Shared memory (SMEM)** is programmer-managed on-chip memory used to reduce repeated global-memory access.
- **Registers** are the fastest storage and are private to threads.
- **Streaming multiprocessors (SMs)** execute warps and contain Tensor Cores, CUDA cores, schedulers, registers, and shared memory.
- **Tensor Cores** accelerate matrix operations and are essential for modern deep-learning throughput.
- **Warp tiling** breaks the computation into smaller pieces that fit better into fast memory.
- **TMA** on Hopper supports asynchronous memory movement between global and shared memory.
- **Pipelining** overlaps memory transfer and computation so the hardware is less idle.

## Why it matters for ML

A model architecture may look mathematical at a high level, but its real cost depends on hardware execution. Understanding matmul kernels helps explain:

- why GPUs are efficient for deep learning;
- why memory movement can bottleneck training and inference;
- why Tensor Cores matter;
- why low-level kernels can strongly affect model speed;
- why libraries such as CUDA, Triton, and cuBLAS are important.

## Practical takeaway

For most ML users, the goal is not to write custom SASS kernels. The value is understanding the performance mental model:

```text
Deep learning speed = arithmetic work + memory movement + scheduling efficiency
```

Better kernels reduce unnecessary memory traffic and keep the compute units busy.

## Common beginner mistakes

- Thinking GPU speed comes only from having many cores.
- Ignoring memory hierarchy and data movement.
- Treating matrix multiplication as a solved black box.
- Forgetting that kernel performance depends on hardware generation.
- Assuming CUDA C++ code always maps to optimal low-level instructions.

## Limitations

This is a highly technical blog post, not a peer-reviewed ML paper. It is best used as an advanced systems note for understanding performance, not as a source for ML theory.

## Related notes

- [Neural Networks](neural-networks-google-ml-crash-course.md)
- [Introduction to Large Language Models](introduction-to-large-language-models.md)
- [InCoder-32B](incoder-32b-code-foundation-model-for-industrial-scenarios.md)

## Source

Original source: https://www.aleksagordic.com/blog/matmul
