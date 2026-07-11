---
source_url: https://github.com/donnemartin/system-design-primer#availability-vs-consistency
author: Unknown
date: 11-07-2026
---

# GitHub - donnemartin/system-design-primer: Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. · GitHub

This section explains the core trade-off between making a distributed system always respond (availability) and ensuring every read returns the most recent write (consistency), especially under network partitions. It shows how replication strategies, synchronous vs asynchronous writes, and quorum-based reads/writes influence latency, fault tolerance, and data freshness. The guide connects these choices to the CAP theorem and highlights practical techniques to tune guarantees for different workloads. It emphasizes selecting the right balance based on product requirements and expected failure modes.
- Availability: every request gets a response, but data may be stale; Consistency: every read reflects the latest write (in CAP sense)
- Network partitions force a trade-off: you cannot have both perfect availability and strong consistency simultaneously (CAP)
- Quorum strategy: choose read quorum R and write quorum W over N replicas (e.g., R + W > N) to balance consistency, availability, and latency
- Synchronous replication and majority writes improve consistency but increase latency and reduce availability; asynchronous replication improves availability at the cost of staleness (eventual consistency)
- Reading from replicas boosts availability and throughput but risks stale reads; reading from the leader strengthens read-after-write behavior
- Use-case guidance: AP (more availability) for feeds, timelines, caches; CP (more consistency) for financial transactions, inventory, and correctness-critical operations
- Be explicit about client-visible guarantees (e.g., read-after-write, monotonic reads) and failure behaviors (e.g., during leader failover)