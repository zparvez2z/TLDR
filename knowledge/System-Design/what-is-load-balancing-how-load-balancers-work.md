---
source_url: https://www.cloudflare.com/learning/performance/what-is-load-balancing/
author: Cloudflare
date: 19-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Cloudflare Learning Center article; this note summarizes load balancing purpose, hardware/software load balancers, static vs dynamic algorithms, health checks, failover, and GSLB.
difficulty: Beginner
tags: [system-design, load-balancing, scalability, reliability, traffic-management]
---

# What Is Load Balancing?

## TL;DR

Load balancing distributes traffic or work across multiple servers so one server does not become overloaded.

It improves performance, reliability, and availability.

## Core idea

Instead of sending all requests to one server:

```text
clients → one overloaded server
```

A load balancer spreads requests across a pool of servers:

```text
clients → load balancer → server A / server B / server C
```

This reduces strain on each server and helps the system continue working if one server fails.

## What a load balancer does

A load balancer can:

- distribute incoming requests across healthy servers;
- check server health;
- stop sending traffic to failed servers;
- route users to nearby or less busy servers;
- support failover;
- improve response time and reduce latency;
- help applications scale horizontally.

## Hardware vs software load balancers

Cloudflare distinguishes two broad implementation types:

- **Hardware load balancers**: dedicated physical devices.
- **Software/cloud load balancers**: services or software running on servers, virtual machines, or cloud infrastructure.

Modern cloud systems usually use software or managed cloud load balancing.

## Static vs dynamic load balancing

### Static algorithms

Static algorithms follow a fixed rule and do not react to current server health.

Examples:

- round robin;
- weighted round robin;
- client-side random choice.

They are simple but can send traffic to overloaded or unhealthy servers if not combined with health checks.

### Dynamic algorithms

Dynamic algorithms consider current server state.

Examples:

- least connections;
- weighted least connections;
- resource-based routing;
- geolocation-based routing.

They are more adaptive, but more complex to configure.

## Failover

Failover means redirecting traffic away from a failed server to backup servers.

This is important because without failover, one crashed server could make the application unavailable.

## Global Server Load Balancing

Global Server Load Balancing, or GSLB, distributes traffic across servers in different regions.

It is useful for global applications because users can be routed to a nearby or healthier location.

## Common beginner mistakes

- Thinking load balancing alone fixes all scaling problems.
- Forgetting health checks.
- Treating all requests as equally expensive.
- Not planning what happens when the load balancer fails.
- Ignoring sticky sessions, caching, database bottlenecks, and stateful services.

## Mental model

A load balancer is like a traffic controller. It decides which server should handle each incoming request so the system stays fast and reliable.

## Related notes

- [Load Balancing Algorithms](what-is-load-balancing-algorithms-types-benefits.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [CDN](what-is-a-cdn-content-delivery-network-explained.md)

## Source

Original source: https://www.cloudflare.com/learning/performance/what-is-load-balancing/
