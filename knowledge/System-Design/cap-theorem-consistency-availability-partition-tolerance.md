---
source_url: https://github.com/donnemartin/system-design-primer#cap-theorem
author: Donne Martin and contributors
date: 12-07-2026
source_type: open_source_guide_section
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original System Design Primer CAP theorem section; this note summarizes the CAP trade-off for beginner learning.
difficulty: Beginner
tags: [system-design, cap-theorem, consistency, availability, partition-tolerance]
---

# CAP Theorem

## TL;DR

CAP theorem says that during a network partition, a distributed system must choose between consistency and availability.

Partition tolerance is not optional for real distributed systems because networks can fail.

## Core idea

CAP stands for:

```text
C = Consistency
A = Availability
P = Partition tolerance
```

The source defines the guarantees like this:

- **Consistency**: every read receives the most recent write or an error.
- **Availability**: every request receives a response, but not necessarily the latest data.
- **Partition tolerance**: the system continues operating despite network failures that split nodes apart.

When a partition happens, the system usually behaves more like CP or AP.

## CP systems

A CP system prefers consistency during a partition.

It may reject, delay, or fail some requests rather than return stale or conflicting data.

Good fit for:

- payments;
- inventory correctness;
- account balances;
- permission changes;
- systems where wrong data is dangerous.

Trade-off:

```text
better correctness during failures → lower availability
```

## AP systems

An AP system prefers availability during a partition.

It keeps responding, even if some responses might use stale data. The system may repair or reconcile differences later.

Good fit for:

- feeds;
- comments;
- likes;
- caching;
- analytics;
- recommendation updates.

Trade-off:

```text
better availability during failures → temporary inconsistency
```

## What CAP does not mean

CAP does not mean you permanently choose only two letters and ignore the third.

In normal operation, systems can often provide useful levels of consistency and availability. CAP becomes most important when there is a partition or failure.

Many real systems also tune guarantees by operation. For example, account creation might be strongly consistent, while a feed counter may be eventually consistent.

## Common beginner mistakes

- Thinking CAP applies only to databases. It applies broadly to distributed systems.
- Forgetting that partitions are real network failures, not just theoretical cases.
- Saying a system is simply "CP" or "AP" without explaining the operation and failure mode.
- Confusing eventual consistency with unreliable data.
- Ignoring business requirements when choosing a trade-off.

## Mental model

During a network split, a system faces a question:

```text
Should I answer now, or should I avoid answering until I can be sure the data is correct?
```

That is the CAP trade-off.

## Related notes

- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [Message Queues](what-is-a-message-queue.md)

## Source

Original source: https://github.com/donnemartin/system-design-primer#cap-theorem
