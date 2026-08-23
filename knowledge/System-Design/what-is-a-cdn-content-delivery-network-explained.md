---
source_url: https://aws.amazon.com/what-is/cdn/
author: Amazon Web Services
date: 20-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS article; this note summarizes CDN purpose, latency reduction, edge servers, caching, static and dynamic content handling, availability, security, and CloudFront.
difficulty: Beginner
tags: [system-design, cdn, caching, edge-computing, latency, web-performance]
---

# What Is a CDN?

## TL;DR

A CDN, or content delivery network, is a distributed network of edge servers that delivers content from locations closer to users.

The main goal is to reduce latency, improve performance, reduce origin load, and increase availability.

## Core idea

Without a CDN:

```text
user far away → origin server
```

With a CDN:

```text
user → nearby CDN edge server → origin only when needed
```

The edge server can serve cached content, so the request does not always need to travel all the way to the origin.

## Why CDNs matter

AWS explains that CDNs help because Internet users and origin servers may be far apart. Long physical distance and many network hops increase delay.

A CDN can:

- reduce page load time;
- reduce bandwidth usage at the origin;
- improve user experience;
- handle traffic spikes;
- improve availability;
- help absorb DDoS traffic by distributing load.

## Static vs dynamic content

### Static content

Static content does not change often and is ideal for caching.

Examples:

- images;
- CSS files;
- JavaScript files;
- fonts;
- videos;
- logos.

### Dynamic content

Dynamic content may change per user or request.

Examples:

- personalized recommendations;
- account pages;
- real-time dashboards;
- shopping carts.

A CDN may not cache all dynamic content, but it can still improve delivery through optimized routes, persistent connections, and edge logic.

## How a CDN works

A CDN uses geographically distributed points of presence, often called POPs.

Each POP contains edge servers.

The CDN can use:

- **caching**: storing copies of content near users;
- **dynamic acceleration**: optimizing routes and connections;
- **edge logic**: running some request handling closer to the user.

## CDN vs load balancer

A CDN and a load balancer are related but not the same.

- A **load balancer** distributes traffic across backend servers.
- A **CDN** distributes content closer to users and reduces origin traffic.

Many large systems use both.

## Common beginner mistakes

- Thinking a CDN only stores images.
- Caching private or personalized content incorrectly.
- Forgetting cache invalidation and TTL rules.
- Assuming a CDN removes the need for backend scaling.
- Not designing fallback behavior if the origin or CDN has issues.

## Mental model

A CDN is like placing copies of popular content in many local libraries instead of making every user travel to one central library.

## Related notes

- [Caching](what-is-caching-and-how-it-works-aws.md)
- [Load Balancing](what-is-load-balancing-how-load-balancers-work.md)
- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)
- [DNS](what-is-dns-and-how-it-works.md)

## Source

Original source: https://aws.amazon.com/what-is/cdn/
