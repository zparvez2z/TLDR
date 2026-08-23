---
source_url: https://www.cloudflare.com/learning/security/api/what-is-an-api-gateway/
author: Cloudflare
date: 30-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Cloudflare Learning Center article; this note summarizes API Gateway responsibilities, request flow, security checks, transformations, caching, and benefits.
difficulty: Beginner
tags: [system-design, api-gateway, api, microservices, reverse-proxy, security]
---

# What Is an API Gateway?

## TL;DR

An API Gateway is an intermediary that accepts, routes, transforms, and manages API traffic between clients and backend services.

It gives clients one controlled entry point instead of exposing many internal services directly.

## Core idea

In a microservice system, clients may need data from many backend services.

Without a gateway:

```text
client → service A
client → service B
client → service C
```

With a gateway:

```text
client → API Gateway → backend services
```

The gateway hides internal complexity and applies common policies in one place.

## What an API Gateway does

Common responsibilities include:

- routing requests to the right backend service;
- authenticating clients using API keys, JWT, mTLS, or other mechanisms;
- checking authorization;
- rate limiting and abuse protection;
- request and response transformation;
- caching selected responses;
- collecting logs, metrics, and analytics;
- providing a stable external API while internal services change.

## Request flow

A typical flow looks like this:

```text
client sends request
→ gateway receives request
→ gateway authenticates and authorizes
→ gateway checks rate limits and policies
→ gateway routes to the correct microservice
→ microservice responds
→ gateway transforms or caches if needed
→ client receives response
```

## Why it matters in system design

API Gateways are useful when a system has many services or external consumers.

They help with:

- simplifying client integration;
- protecting internal services;
- centralizing cross-cutting concerns;
- supporting microservice architectures;
- making APIs easier to document, test, monitor, and evolve.

## Trade-offs

An API Gateway can also create problems if designed badly:

- it can become a bottleneck;
- it can become a single point of failure;
- too much business logic in the gateway makes it hard to maintain;
- debugging can become harder if gateway logs are weak;
- caching and transformation rules can cause surprising behavior.

## Common beginner mistakes

- Treating the gateway as only a router.
- Putting too much domain logic in the gateway.
- Forgetting rate limits and authentication.
- Exposing internal service URLs directly to clients.
- Not designing the gateway for high availability.

## Mental model

An API Gateway is like the front desk of a building. Visitors do not go directly to every internal office; the front desk checks, routes, and controls access.

## Related notes

- [What Is an API?](what-is-an-api-cloudflare-learning.md)
- [What Is a REST API?](what-is-a-rest-api.md)
- [Load Balancing](what-is-load-balancing-how-load-balancers-work.md)
- [Caching](what-is-caching-and-how-it-works-aws.md)

## Source

Original source: https://www.cloudflare.com/learning/security/api/what-is-an-api-gateway/
