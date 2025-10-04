---
source_url: https://www.aleksagordic.com/blog/matmul
author: Aleksa Gordić
date: 29-09-2025
---

# Inside NVIDIA GPUs: Anatomy of high performance matmul kernels

This article provides a deep dive into the hardware and software techniques used to create state-of-the-art matrix-multiplication (matmul) kernels on NVIDIA GPUs, focusing on the Hopper H100 architecture. It begins by explaining the fundamentals of GPU architecture, including memory hierarchies (global memory, shared memory, L1/L2 cache) and compute units like streaming multiprocessors and Tensor Cores. The post then transitions to the CUDA programming model and the role of GPU assembly languages like PTX and SASS, demonstrating how low-level optimizations can yield significant performance gains. The author walks through the evolution of matmul kernels, from a naïve implementation to a near-SOTA synchronous kernel using warp-tiling, and finally to a fully asynchronous SOTA kernel on Hopper that leverages Tensor Cores, TMA for data movement, and advanced pipelining and scheduling techniques like Hilbert curves.

*   **GPU Architecture:** A solid mental model of the hardware, particularly the memory hierarchy (DRAM vs. SRAM, caches) and compute units (SMs, Tensor Cores), is essential for writing high-performance kernels.
*   **Low-Level Optimization:** Understanding PTX and SASS assembly allows programmers to verify compiler output and unlock performance that isn't accessible through CUDA C++ alone.
*   **Warp-Tiling:** This technique involves breaking the matmul computation into smaller blocks that fit into shared memory (SMEM), which dramatically reduces slow global memory (GMEM) traffic and improves arithmetic intensity.
*   **Hopper Architecture Features:** Modern GPUs like the H100 offer features like the Tensor Memory Accelerator (TMA) for asynchronous data transfers and specialized `wgmma` instructions for Tensor Cores, which abstract away much of the complexity of older methods and deliver order-of-magnitude performance improvements.
*   **Advanced Optimization Techniques:** Achieving peak performance requires sophisticated strategies such as pipelining data movement and computation, using persistent kernels to hide store latency, and employing cluster-level execution with space-filling curves for scheduling to maximize data reuse and minimize memory traffic.