---
source_url: https://github.com/donnemartin/system-design-primer#performance-vs-scalability
author: Unknown
date: 09-07-2026
---

# GitHub - donnemartin/system-design-primer: Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. · GitHub

This section distinguishes performance from scalability in the context of system design. Performance is about how fast a system completes a task for a single user (often measured as latency), while scalability is about maintaining acceptable performance as load increases (often measured via throughput and tail latency). Performance problems are visible even at low load; scalability problems emerge as concurrency, data volume, or request rates grow. The guide outlines typical remedies for each and stresses that improving one does not automatically improve the other.
- Performance: speed of a single task/request; typically measured by latency and response time percentiles.
- Scalability: ability to sustain performance as load grows; assessed via throughput, concurrency handling, and stability of tail latency under load.
- Symptoms: performance issues = slow single-user operations; scalability issues = degradation only under higher load.
- Approaches: performance tuning (algorithms, data structures, caching, I/O optimization, vertical scaling) vs scalability techniques (horizontal scaling, load balancing, replication, sharding, stateless services).
- Metrics and tests: track latency percentiles, throughput, saturation; do capacity planning and load testing to expose scaling limits.
- Trade-offs: added complexity, cost, operational overhead, and possible consistency/availability impacts when scaling out.
- Key takeaway: Adding resources to reduce latency for a fixed workload improves performance; adding resources to handle more load at similar latency improves scalability.