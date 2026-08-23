---
source_url: https://aws.amazon.com/what-is/load-balancing/
author: Amazon Web Services
date: 25-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS article; this note summarizes load-balancing benefits, static and dynamic algorithms, load-balancer types, DNS load balancing, security, scalability, and performance trade-offs.
difficulty: Beginner
tags: [system-design, load-balancing, algorithms, scalability, availability, aws]
---

# Load Balancing Algorithms and Types

## TL;DR

Load balancing distributes traffic across multiple backend resources. The main design question is: **how should the load balancer choose the next server?**

Different algorithms make different trade-offs between simplicity, fairness, performance, health awareness, and session behavior.

## Core idea

A load balancer uses rules to choose where each request should go.

```text
request → load-balancing rule → selected backend server
```

A good algorithm prevents bottlenecks, supports failover, and keeps response times stable as traffic grows.

## Why load balancing matters

AWS highlights four major benefits:

- **availability**: traffic can be redirected away from failed or unhealthy servers;
- **scalability**: more servers can be added behind the balancer;
- **security**: traffic can be monitored or routed through protection layers;
- **performance**: requests can be spread evenly or sent to closer/faster resources.

## Static algorithms

Static algorithms do not depend on current server state.

### Round robin

Requests are sent to servers in order.

```text
A → B → C → A → B → C
```

Simple, but it assumes all servers and requests are similar.

### Weighted round robin

Servers get different weights based on capacity or priority.

Example:

```text
large server weight = 3
small server weight = 1
```

The larger server receives more traffic.

### IP hash

The load balancer hashes the client IP address and maps it to a server.

This can help keep the same client on the same backend, but it may distribute traffic unevenly.

## Dynamic algorithms

Dynamic algorithms look at current server state before routing.

### Least connections

Send traffic to the server with the fewest active connections.

Good when long-lived connections vary across servers.

### Weighted least connections

Like least connections, but server capacity is also considered.

### Least response time

Send traffic to the server that responds fastest or has low load.

### Resource-based routing

Use current CPU, memory, or other health/capacity signals to route traffic.

## Types of load balancing

Common types include:

- **Application load balancing**: routes based on HTTP-level information such as path, host, headers, or content.
- **Network load balancing**: routes at lower network layers, often optimized for high throughput and low latency.
- **Global server load balancing**: routes users across regions or data centers.
- **DNS load balancing**: uses DNS responses to distribute traffic across resource pools.

## Common beginner mistakes

- Choosing round robin without checking whether requests have different cost.
- Forgetting health checks.
- Assuming DNS load balancing reacts instantly; DNS caching can delay changes.
- Ignoring sticky-session needs.
- Letting the database become the next bottleneck after scaling app servers.
- Not testing behavior during server failure or deployment.

## Mental model

A load-balancing algorithm is the scheduling rule at the entrance of your system. It decides which backend should receive each new request.

## Related notes

- [What Is Load Balancing?](what-is-load-balancing-how-load-balancers-work.md)
- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [CDN](what-is-a-cdn-content-delivery-network-explained.md)

## Source

Original source: https://aws.amazon.com/what-is/load-balancing/
