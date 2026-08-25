---
source_url: https://www.cloudflare.com/learning/cdn/what-is-caching/
author: Cloudflare
date: 25-08-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-25
verification_scope: Checked against the original Cloudflare Learning Center article; this note summarizes browser caching, CDN caching, cache hits, cache misses, TTL, DNS caching, and Cloudflare CDN caching for personal learning.
difficulty: Beginner
tags: [system-design, caching, cdn, browser-cache, cache-hit, cache-miss, ttl]
---

# Caching: Browser and CDN Caches

## TL;DR

Caching stores temporary copies of files or data so they can be delivered faster the next time they are needed.

In web systems, caching can happen in browsers, DNS servers, CDN edge servers, proxies, applications, and databases.

This note focuses on browser caching and CDN caching.

## Core idea

Without caching:

```text
user → origin server → response
```

With caching:

```text
user → nearby cache → faster response
```

The cache may already have the requested content. If it does, the system avoids a slower trip to the origin.

## Browser caching

A browser cache stores copies of website files on the user's device.

Common cached files include:

- HTML;
- JavaScript;
- CSS;
- images;
- fonts.

When the user visits the same page again, the browser may load some files from local storage instead of downloading everything again.

This reduces page load time.

## Clearing the browser cache

Clearing the browser cache removes stored copies.

This can help if a bad or outdated file was cached, but it can also make websites slower temporarily because files need to be downloaded again.

## CDN caching

A CDN, or content delivery network, stores copies of content in edge servers located closer to users.

```text
user → nearby CDN edge server → origin only when needed
```

This reduces latency because the user does not always need to fetch content from a distant origin server.

CDNs commonly cache:

- images;
- videos;
- webpages;
- scripts;
- stylesheets;
- downloadable files.

## Cache hit and cache miss

A **cache hit** happens when the requested content is already in the cache.

```text
request → cache has content → fast response
```

A **cache miss** happens when the requested content is not in the cache.

```text
request → cache missing content → origin server → cache stores result → response
```

Cache hits are usually faster than cache misses.

## TTL: time to live

TTL controls how long content should remain cached.

Short TTL:

- fresher content;
- more origin requests;
- less risk of stale data.

Long TTL:

- faster repeated delivery;
- fewer origin requests;
- higher stale-content risk.

## Other caching examples

Cloudflare also mentions DNS caching.

DNS caching stores recent DNS lookup results so DNS servers do not need to repeat the full lookup every time.

Search engines may also cache webpages so users can still access a copy when the original site is temporarily unavailable.

## Why caching matters in system design

Caching helps systems:

- reduce latency;
- reduce bandwidth usage;
- reduce origin load;
- improve page load times;
- handle repeated requests more efficiently;
- make CDN delivery faster.

## Common beginner mistakes

- Caching private or user-specific content incorrectly.
- Forgetting TTL and cache invalidation.
- Assuming cached content is always fresh.
- Ignoring cache misses and origin fallback behavior.
- Clearing cache without understanding that first load may become slower.
- Thinking CDN caching replaces backend scaling completely.

## Mental model

Caching is like keeping frequently used supplies nearby instead of traveling to the source every time.

## Related notes

- [What Is Caching?](what-is-caching-and-how-it-works-aws.md)
- [What Is a CDN?](what-is-a-cdn-content-delivery-network-explained.md)
- [What Is DNS?](what-is-dns-and-how-it-works.md)
- [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)

## Source

Original source: https://www.cloudflare.com/learning/cdn/what-is-caching/
