---
source_url: https://github.com/donnemartin/system-design-primer#cap-theorem
author: Donne Martin
date: 12-07-2026
---

# GitHub - donnemartin/system-design-primer: Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. · GitHub

The CAP theorem explains the inherent trade-offs in distributed systems among Consistency, Availability, and Partition Tolerance. In the presence of a network partition, a system can guarantee either consistency or availability, but not both. Partition tolerance is non-negotiable for distributed systems, so practical designs gravitate toward CP (consistency + partition tolerance) or AP (availability + partition tolerance) strategies. Real-world systems often provide tunable behavior to balance user experience, performance, and data correctness across different operations.

- Partition tolerance is mandatory; during a partition you must choose consistency (CP) or availability (AP).
- Consistency: every read reflects the latest write (or returns an error); Availability: every request receives a non-error response, not necessarily the latest data; Partition tolerance: the system continues operating despite network failures.
- CP systems maintain strong consistency by sacrificing availability when partitions occur.
- AP systems remain available during partitions, accepting temporary inconsistencies (often converging via eventual consistency).
- The choice depends on product requirements; systems may offer tunable consistency per operation or endpoint.
- Related sections in the primer expand on consistency patterns (weak, eventual, strong) and availability patterns (fail-over, replication).