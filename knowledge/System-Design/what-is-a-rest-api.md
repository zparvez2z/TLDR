---
source_url: https://www.redhat.com/en/topics/api/what-is-a-rest-api
author: Red Hat
date: 18-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Red Hat article; this note summarizes REST as an architectural style, REST constraints, resource representations, HTTP metadata, and REST vs SOAP trade-offs.
difficulty: Beginner
tags: [system-design, api, rest, http, client-server]
---

# What Is a REST API?

## TL;DR

A REST API is an API that follows the REST architectural style. It usually exposes resources over HTTP and lets clients create, read, update, or delete those resources using standard request patterns.

REST is not a protocol. It is a set of architectural constraints.

## Core idea

REST stands for Representational State Transfer.

The key idea is that clients interact with **resources**, and the server returns a **representation** of the resource state.

```text
client → HTTP request → resource endpoint → representation in response
```

Example:

```text
GET /users/42
```

The server might return a JSON representation of user `42`.

## Key REST constraints

A RESTful API should follow these ideas:

- **Client-server separation**: the client and server have separate responsibilities.
- **Statelessness**: each request contains the information needed to process it; the server does not rely on stored client session state for the request.
- **Cacheability**: responses should indicate whether they can be cached.
- **Uniform interface**: resources are accessed in a consistent way.
- **Layered system**: intermediaries such as proxies, gateways, and load balancers can sit between client and server.
- **Code on demand**: optional ability for a server to send executable code to the client.

## Common data formats

REST APIs often use JSON because it is readable and easy for many languages to parse.

Other possible formats include:

- XML;
- HTML;
- plain text;
- binary formats.

## Why REST matters in system design

REST APIs are common because they are simple, language-agnostic, scalable, and easy to integrate with web clients.

They help systems expose operations such as:

```text
GET    /products
GET    /products/123
POST   /orders
PUT    /users/42
DELETE /sessions/current
```

## REST vs SOAP

Red Hat describes SOAP as a more prescribed protocol with stricter requirements, while REST is a flexible architectural style that can be implemented as needed.

In practice:

- SOAP can be useful where strict standards and enterprise requirements matter.
- REST is usually lighter and more common for web and mobile APIs.

## Common beginner mistakes

- Thinking REST is the same thing as HTTP. REST is an architectural style; HTTP is the most common transport used with it.
- Making every endpoint action-based instead of resource-based.
- Keeping hidden server-side session assumptions while calling the API stateless.
- Ignoring HTTP status codes, headers, caching, and idempotency.
- Returning inconsistent response formats.

## Mental model

A REST API is like a structured set of doors into a system. Each door represents a resource, and the client uses clear request rules to interact with it.

## Related notes

- [What Is an API?](what-is-an-api-cloudflare-learning.md)
- [Overview of HTTP](overview-of-http-mdn.md)
- [What Is an API Gateway?](what-is-an-api-gateway.md)
- [Caching](what-is-caching-and-how-it-works-aws.md)

## Source

Original source: https://www.redhat.com/en/topics/api/what-is-a-rest-api
