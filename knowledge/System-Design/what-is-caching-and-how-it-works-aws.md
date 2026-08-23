---
source_url: https://aws.amazon.com/caching/
author: Amazon Web Services
date: 21-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS caching overview; this note summarizes cache purpose, in-memory storage, cache layers, hit/miss behavior, TTLs, high availability, and common caching use cases.
difficulty: Beginner
tags: [system-design, caching, performance, latency, scalability, redis, memcached]
---

# What Is Caching?

## TL;DR

Caching stores a temporary copy of frequently used data in a faster storage layer so future requests can be served more quickly.

It is one of the most important system design techniques for reducing latency and protecting slower backend systems.

## Core idea

Without caching:

```text
request → slow database or origin → response
```

With caching:

```text
request → cache hit → fast response
request → cache miss → backend → store result in cache → response
```

A cache trades capacity and freshness complexity for speed.

## How caching works

AWS describes a cache as a high-speed data storage layer that stores a subset of data, usually transiently.

Caches often use fast access hardware such as RAM and in-memory engines.

The goal is to reduce repeated access to slower storage such as disk-based databases or remote services.

## Common cache layers

Caching can happen at many levels:

- browser cache;
- operating system cache;
- DNS cache;
- CDN edge cache;
- reverse proxy cache;
- application cache;
- database cache;
- distributed in-memory cache such as Redis or Memcached.

## Cache hit and cache miss

A **cache hit** happens when requested data is already in the cache.

A **cache miss** happens when the data is not in the cache, so the system must fetch it from the slower source.

Good cache design tries to achieve a high hit rate for frequently requested data.

## TTL and expiration

TTL means time to live.

It controls how long cached data is considered valid.

Short TTL:

- fresher data;
- more backend requests.

Long TTL:

- faster responses;
- fewer backend requests;
- higher risk of stale data.

## Why caching matters

Caching can:

- reduce latency;
- increase throughput;
- reduce database load;
- smooth traffic spikes;
- reduce cost;
- improve user experience;
- make read-heavy systems scale better.

## Common caching use cases

AWS lists caching across many workloads, including:

- web content;
- DNS resolution;
- database query results;
- API responses;
- sessions;
- gaming leaderboards;
- media delivery;
- ecommerce recommendations;
- social feeds;
- high-performance computing simulations.

## Common beginner mistakes

- Caching data that must always be fresh.
- Forgetting cache invalidation.
- Using very long TTLs without thinking about stale data.
- Not handling cache misses safely.
- Letting a hot key overload one cache node.
- Treating the cache as the source of truth without durability planning.
- Not defining RTO/RPO if an in-memory layer becomes critical.

## Mental model

A cache is like keeping frequently used books on your desk instead of walking to the library every time.

## Related notes

- [CDN](what-is-a-cdn-content-delivery-network-explained.md)
- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [REST API](what-is-a-rest-api.md)

## Source

Original source: https://aws.amazon.com/caching/
