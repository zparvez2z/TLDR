---
source_url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
author: MDN Web Docs
date: 14-07-2026
source_type: documentation
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original MDN HTTP overview; this note summarizes HTTP's request/response model, statelessness, extensibility, headers, sessions, proxies, and connection behavior.
difficulty: Beginner
tags: [system-design, http, web, networking, client-server]
---

# Overview of HTTP

## TL;DR

HTTP is the application-layer protocol used by the Web to fetch and exchange resources such as HTML pages, images, videos, scripts, API responses, and form data.

It follows a client-server request/response model: the client sends a request, and the server sends a response.

## Core idea

A browser or other client asks for a resource:

```text
client → HTTP request → server
```

The server answers:

```text
server → HTTP response → client
```

HTTP sits above transport protocols such as TCP and TLS-secured TCP connections. Modern HTTP versions improve how connections are reused and multiplexed, but the basic request/response idea remains central.

## Main components

HTTP-based systems usually involve:

- **client / user-agent**: browser, mobile app, crawler, CLI tool, or API client;
- **server**: handles requests and returns responses;
- **proxies / intermediaries**: can cache, filter, log, authenticate, load-balance, or forward traffic;
- **resources**: documents, images, JSON, scripts, videos, or API data.

## HTTP messages

HTTP messages usually include:

- method, such as `GET`, `POST`, `PUT`, or `DELETE`;
- path or URL;
- status code, such as `200`, `404`, or `500`;
- headers;
- optional body.

Example mental model:

```text
GET /products/42 → 200 OK + product data
```

## Important properties

### HTTP is extensible

Headers allow clients and servers to add behavior without changing the whole protocol.

Headers can control things such as:

- caching;
- authentication;
- content type;
- compression;
- language negotiation;
- CORS;
- range requests;
- cookies.

### HTTP is stateless

Each request is independent at the protocol level. The server does not automatically remember previous requests.

However, HTTP is not sessionless. Cookies and other mechanisms can create stateful user sessions on top of HTTP.

### HTTP uses intermediaries

Proxies, gateways, caches, CDNs, and load balancers can sit between client and server. They are important for performance, security, observability, and reliability.

## Why HTTP matters in system design

Many system design problems involve web APIs. Understanding HTTP helps you reason about:

- API design;
- caching behavior;
- authentication;
- browser behavior;
- proxies and load balancers;
- latency;
- retries and idempotency;
- status codes and error handling.

## Common beginner mistakes

- Thinking HTTP is only for websites, not APIs.
- Forgetting that HTTP is stateless by default.
- Ignoring headers when debugging behavior.
- Treating all HTTP methods as interchangeable.
- Returning unclear status codes from APIs.
- Forgetting that intermediaries can cache or modify behavior.

## Mental model

HTTP is the shared language between clients and servers on the Web.

```text
request → response
```

Everything else, such as cookies, caching, APIs, and proxies, builds on that basic exchange.

## Related notes

- [What Is DNS?](what-is-dns-and-how-it-works.md)
- [What Is an API?](what-is-an-api-cloudflare-learning.md)
- [What Is a REST API?](what-is-a-rest-api.md)
- [What Is an API Gateway?](what-is-an-api-gateway.md)

## Source

Original source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
