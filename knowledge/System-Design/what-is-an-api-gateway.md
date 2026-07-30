---
source_url: https://www.cloudflare.com/learning/security/api/what-is-an-api-gateway/
author: Unknown
date: 30-07-2026
---

# What is an API Gateway?

An API gateway is a service or proxy that sits between clients and backend microservices, accepting, routing, and managing API traffic. It centralizes concerns like authentication, authorization, rate limiting, caching, and request/response transformations to improve security, performance, and maintainability. The gateway workflow typically involves receiving HTTP/HTTPS requests, routing by URL and policies, verifying identity via mTLS/JWT/API keys, transforming payloads, returning responses, and collecting analytics. By providing a unified entry point, API gateways enhance developer and consumer experiences and enable teams to share data across systems without exposing internal services directly.
- Acts as a reverse proxy and intermediary for API traffic to backend services and microservices
- Handles security tasks (authentication, authorization, rate limiting) using mechanisms like mTLS, JWT, and API keys
- Performs performance optimizations such as caching and request/response transformation
- Workflow: receive request, route to microservice, verify and authorize, transform payloads, return response, collect telemetry/analytics
- Provides abstraction and a unified entry point, improving developer tooling (analytics, docs, testing) and consumer ease of use
- Enables inter-departmental data sharing without direct access to internal systems