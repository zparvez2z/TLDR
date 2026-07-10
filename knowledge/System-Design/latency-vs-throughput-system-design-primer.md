---
source_url: https://github.com/donnemartin/system-design-primer#latency-vs-throughput
author: Donne Martin
date: 10-07-2026
---

# GitHub - donnemartin/system-design-primer: Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. · GitHub

This section clarifies the difference between latency (how long a single operation takes) and throughput (how many operations a system can complete per unit time). It emphasizes that optimizing for one often impacts the other, and effective designs balance user-perceived responsiveness with system-wide capacity. The content outlines common strategies and trade-offs engineers use to tune systems depending on product goals and workload patterns.
- Latency: time to complete one request; Throughput: requests processed per unit time.
- Low latency does not imply high throughput, and high throughput can come with higher per-request latency.
- Reduce latency with caching, minimizing synchronous dependencies, reducing contention, and doing work in parallel when beneficial.
- Increase throughput with batching, asynchronous processing, queueing with worker pools, and efficient I/O and serialization.
- Key trade-offs: batching boosts throughput but can increase latency; replication can reduce read latency but add write overhead; apply back pressure to keep latency bounded under load.
- Choose targets and SLAs based on the use case (e.g., interactive UX favors latency; analytics pipelines often favor throughput).