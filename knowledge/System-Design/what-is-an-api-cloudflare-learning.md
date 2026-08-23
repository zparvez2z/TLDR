---
source_url: https://www.cloudflare.com/learning/security/api/what-is-an-api/
author: Cloudflare
date: 15-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Cloudflare Learning Center article; this note summarizes API calls, endpoints, schemas, integrations, web APIs, SOAP/REST distinction, and basic API security.
difficulty: Beginner
tags: [system-design, api, web-api, integration, api-security]
---

# What Is an API?

## TL;DR

An API, or application programming interface, is a set of rules that lets one software system use data or functionality from another software system.

APIs are important in system design because they define how services communicate.

## Core idea

Instead of rebuilding functionality from scratch, a system can call another system through an API.

```text
client application → API request → API server → API response
```

Example: a travel app does not need to build its own weather system. It can call a weather API and display the returned forecast.

## Key terms

- **API call / API request**: a message sent to an API to trigger some action or get data.
- **API response**: the data or result returned by the API.
- **API endpoint**: the URL or address where a specific API function is available.
- **API schema**: the expected shape of valid requests and responses.
- **API integration**: connecting two or more systems using APIs.
- **Web API**: an API accessed over the Internet by web applications or services.

## Why APIs matter in system design

Modern systems are usually made of many services. APIs let those services communicate without exposing all internal details.

They help with:

- separating frontend and backend systems;
- connecting microservices;
- integrating third-party services;
- reusing existing functionality;
- exposing controlled access to data;
- building mobile, web, and partner integrations.

## REST and SOAP

Cloudflare distinguishes two common API styles:

- **SOAP APIs** use the SOAP protocol.
- **REST APIs** follow the REST architectural style and are common in modern web APIs.

Most beginner system design discussions focus on REST-style HTTP APIs, but the core idea is broader: an API defines how systems interact.

## API security basics

APIs expose system functionality, so they can be abused if they are not protected.

Important protections include:

- authentication;
- authorization;
- rate limiting;
- DDoS protection;
- schema validation;
- encrypted transport such as HTTPS;
- mutual TLS for stronger client/server authentication.

## Common beginner mistakes

- Thinking an API is only a URL. The URL is usually just one endpoint; the API also includes rules, request formats, responses, and behavior.
- Ignoring authentication and rate limiting.
- Exposing internal service details directly to clients.
- Not validating request schemas.
- Treating third-party API calls as always reliable.

## Mental model

An API is a contract between software systems. One side promises: "If you ask in this format, I will respond in this format."

## Related notes

- [What Is a REST API?](what-is-a-rest-api.md)
- [What Is an API Gateway?](what-is-an-api-gateway.md)
- [Overview of HTTP](overview-of-http-mdn.md)
- [Rate Limiting and Load Balancing](what-is-load-balancing-how-load-balancers-work.md)

## Source

Original source: https://www.cloudflare.com/learning/security/api/what-is-an-api/
