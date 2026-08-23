---
source_url: https://github.com/donnemartin/system-design-primer#latency-vs-throughput
author: Donne Martin and contributors
date: 10-07-2026
source_type: open_source_guide_section
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original System Design Primer section; this note explains the difference between per-operation time and total capacity.
difficulty: Beginner
tags: [system-design, latency, throughput, performance, scalability]
---

# Latency vs Throughput

## TL;DR

Latency is how long one operation takes. Throughput is how many operations a system completes per unit of time.

Good system design usually aims for high throughput while keeping latency acceptable for the product.

## Core idea

The source defines the distinction simply:

```text
latency = time to perform one action
throughput = number of actions per unit time
```

These two goals can conflict. A system might process many requests per second but make individual users wait longer, or it might respond quickly to one user but not handle many users at once.

## Simple example

Imagine a food delivery app.

Latency:

```text
How long does one order search take?
```

Throughput:

```text
How many order searches can the system process per second?
```

Batching can improve throughput, but it may increase latency because each request waits for a batch.

## Key terms

- **Latency**: time between request and response for one operation.
- **Throughput**: amount of work completed per unit time.
- **Tail latency**: slowest portion of requests, such as p95 or p99 latency.
- **Batching**: grouping work together to process more efficiently.
- **Back pressure**: slowing or rejecting incoming work when the system is overloaded.
- **Queueing delay**: extra waiting time caused by work piling up.

## Why it matters

Different systems optimize for different goals.

Interactive systems usually care about low latency:

- login;
- search;
- checkout;
- chat;
- API responses.

Batch systems often care more about throughput:

- analytics jobs;
- log processing;
- video encoding;
- bulk imports;
- scheduled reports.

## Common trade-offs

- Batching can increase throughput but add waiting time.
- Caching can reduce latency and increase throughput, but adds invalidation complexity.
- Parallelism can reduce latency for some tasks but can also increase resource contention.
- Queues can smooth load but can add delay.
- Replication can improve read latency but add consistency trade-offs.

## Common beginner mistakes

- Treating throughput and latency as the same thing.
- Reporting only average latency and ignoring p95 or p99 latency.
- Improving throughput by batching without checking user-visible delay.
- Ignoring overload behavior.
- Designing for peak traffic without understanding normal traffic.

## Mental model

Latency asks: "How long does one request wait?"

Throughput asks: "How much work can the system finish per second, minute, or hour?"

## Related notes

- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [Load Balancing](what-is-load-balancing-how-load-balancers-work.md)
- [Message Queues](what-is-a-message-queue.md)

## Source

Original source: https://github.com/donnemartin/system-design-primer#latency-vs-throughput
