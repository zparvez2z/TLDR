---
source_url: https://github.com/donnemartin/system-design-primer#availability-vs-consistency
author: Donne Martin and contributors
date: 11-07-2026
source_type: open_source_guide_section
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original System Design Primer section; this note summarizes the availability/consistency trade-off and links it to CAP.
difficulty: Beginner
tags: [system-design, availability, consistency, cap-theorem, distributed-systems]
---

# Availability vs Consistency

## TL;DR

Availability means the system keeps responding. Consistency means reads return the latest correct data.

In distributed systems, failures and network partitions can force a trade-off between always responding and always returning the newest data.

## Core idea

The source connects this topic to CAP theorem.

In a distributed system, when a network partition happens, the system must choose between:

```text
consistency → refuse or delay some responses to avoid stale/wrong data
availability → keep responding, even if some data may be stale
```

This does not mean one is always better. The right choice depends on the product.

## Simple example

A social media feed can usually tolerate temporary inconsistency:

```text
A new like or post may appear a few seconds later.
```

A bank transfer usually needs stronger consistency:

```text
The account balance should not be wrong or double-spent.
```

## Key terms

- **Availability**: every request receives a response, even if the response might not contain the latest data.
- **Consistency**: every read receives the most recent write or an error, in the CAP sense.
- **Partition**: a network failure that prevents parts of the system from communicating.
- **Eventual consistency**: replicas may be temporarily different but converge later.
- **Strong consistency**: clients see the latest committed data.
- **Stale read**: a read that returns older data.

## Design choices

Systems can tune this trade-off using:

- leader/follower replication;
- synchronous or asynchronous replication;
- quorum reads and writes;
- read-from-leader vs read-from-replica policies;
- conflict resolution;
- retries and failover behavior;
- per-operation consistency levels.

## When availability matters more

Availability often matters more for:

- feeds;
- timelines;
- product browsing;
- analytics dashboards;
- caches;
- recommendation systems.

Temporary staleness may be acceptable if the user experience stays smooth.

## When consistency matters more

Consistency often matters more for:

- payments;
- inventory reservation;
- account balances;
- permissions;
- medical or safety-critical state;
- order processing.

Wrong data may be more dangerous than a temporary error.

## Common beginner mistakes

- Saying every system must be strongly consistent.
- Saying every system must always be available.
- Ignoring what happens during network failures.
- Forgetting that different operations in the same product can need different guarantees.
- Confusing eventual consistency with no consistency at all.

## Mental model

Availability asks: "Can the system keep answering?"

Consistency asks: "Is the answer definitely up to date?"

## Related notes

- [CAP Theorem](cap-theorem-consistency-availability-partition-tolerance.md)
- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)
- [Message Queues](what-is-a-message-queue.md)

## Source

Original source: https://github.com/donnemartin/system-design-primer#availability-vs-consistency
