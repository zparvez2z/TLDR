---
source_url: https://github.com/donnemartin/system-design-primer#performance-vs-scalability
author: Donne Martin and contributors
date: 09-07-2026
source_type: open_source_guide_section
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original System Design Primer section; this note summarizes the distinction and practical implications for personal learning.
difficulty: Beginner
tags: [system-design, performance, scalability, latency, throughput]
---

# Performance vs Scalability

## TL;DR

Performance is about how fast a system is for a given task. Scalability is about whether the system can keep acceptable performance as load grows.

A system can be fast for one user but not scalable under heavy traffic.

## Core idea

The source gives a simple distinction:

```text
performance problem → slow for one user
scalability problem → fast for one user, slow under heavy load
```

A scalable system gets more useful capacity when more resources are added. That capacity might mean serving more requests, handling more users, or processing larger datasets.

## Simple example

Imagine a web app search page.

Performance issue:

```text
One user searches → response takes 8 seconds
```

Scalability issue:

```text
One user searches → response is fast
10,000 users search → response becomes very slow
```

The first problem is about single-request speed. The second problem is about behavior under growing load.

## Key terms

- **Performance**: how quickly a system completes work.
- **Scalability**: how well a system handles more work when resources or architecture change.
- **Latency**: time taken for one operation.
- **Throughput**: number of operations completed per unit time.
- **Load**: amount of work placed on the system.
- **Bottleneck**: the part that limits overall performance or scalability.

## Why it matters

Performance tuning and scalability design are related, but they are not the same.

Improving performance might mean:

- optimizing code;
- improving database queries;
- reducing network calls;
- caching expensive results;
- using better algorithms.

Improving scalability might mean:

- horizontal scaling;
- load balancing;
- replication;
- sharding;
- asynchronous processing;
- removing shared bottlenecks.

## Common beginner mistakes

- Saying a system is scalable just because it is fast in a small test.
- Measuring only average latency and ignoring behavior under load.
- Adding servers before finding the bottleneck.
- Thinking scalability always means horizontal scaling.
- Ignoring cost and operational complexity.

## Mental model

Performance asks: "How fast is it now?"

Scalability asks: "Will it stay acceptable when traffic, data, or users grow?"

## Related notes

- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)
- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [System Design Topics: Start Here](system-design-topics-start-here.md)

## Source

Original source: https://github.com/donnemartin/system-design-primer#performance-vs-scalability
