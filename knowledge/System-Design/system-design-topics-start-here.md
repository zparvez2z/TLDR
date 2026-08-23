---
source_url: https://github.com/donnemartin/system-design-primer#system-design-topics-start-here
author: Donne Martin and contributors
date: 08-07-2026
source_type: open_source_guide_section
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original System Design Primer start-here section; this note summarizes the recommended entry point and learning flow.
difficulty: Beginner
tags: [system-design, learning-path, scalability, architecture, interview-prep]
---

# System Design Topics: Start Here

## TL;DR

This section of the System Design Primer is the entry point for learning scalable system design. It tells you where to begin before diving into individual topics.

The most important message is: system design is a set of trade-offs. You should first understand the big ideas, then study components such as DNS, CDNs, load balancers, caches, databases, queues, and communication protocols.

## Core idea

A good system design learning path starts broad:

```text
scalability basics → high-level trade-offs → core building blocks → practice designs
```

The source recommends starting with scalability resources, then moving into core trade-offs:

```text
Performance vs Scalability
Latency vs Throughput
Availability vs Consistency
```

After those, the learner can go deeper into concrete system components.

## What this section points to

The start-here section connects to:

- scalability introduction material;
- performance vs scalability;
- latency vs throughput;
- availability vs consistency and CAP theorem;
- consistency and availability patterns;
- DNS, CDNs, load balancers, reverse proxies, application layers, databases, caches, queues, and communication protocols;
- exercises, interview practice, Anki flashcards, and appendix material.

## Why it matters

Without a starting path, system design can become random. One day you read about databases, the next day about CDNs, then queues, then CAP theorem, without understanding how they connect.

This section gives a learning order so the rest of the primer is easier to follow.

## Suggested beginner order

1. Understand what scalability means.
2. Learn performance vs scalability.
3. Learn latency vs throughput.
4. Learn availability vs consistency.
5. Learn CAP theorem.
6. Study DNS and HTTP.
7. Study CDNs, caching, and load balancing.
8. Study queues and asynchronous processing.
9. Practice full system design questions.

## Common beginner mistakes

- Starting with advanced diagrams before understanding the core trade-offs.
- Thinking there is one correct architecture for every system.
- Ignoring requirements and traffic assumptions.
- Memorizing components without knowing when to use them.
- Forgetting that every component has operational cost and failure modes.

## Mental model

This note is the front door to system design. It tells you the first concepts to learn before entering the bigger architecture topics.

## Related notes

- [The System Design Primer](system-design-primer.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)
- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [CAP Theorem](cap-theorem-consistency-availability-partition-tolerance.md)

## Source

Original source: https://github.com/donnemartin/system-design-primer#system-design-topics-start-here
