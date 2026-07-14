---
source_url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
author: Unknown
date: 14-07-2026
---

# Overview of HTTP - HTTP | MDN MDN MDN Mozilla

This MDN article explains the fundamentals of the Hypertext Transfer Protocol (HTTP), the application-layer protocol that underpins the Web. It describes the client–server model, how requests and responses are exchanged, and the roles of browsers, servers, and intermediaries like proxies. The piece highlights HTTP’s extensibility via headers, its stateless nature complemented by cookies for session management, and how connections are managed over TCP/TLS with improvements in HTTP/1.1 and HTTP/2. It also outlines what HTTP can control through headers, including caching, authentication, content negotiation, CORS, and more.
- HTTP is a client–server, request/response protocol transporting resources (HTML, images, scripts, videos) over reliable transports, typically TCP/TLS.
- User-agents (browsers or tools) initiate requests; servers respond; proxies can cache, filter, load-balance, authenticate, and log.
- HTTP is human-readable and extensible via headers; it is stateless but supports sessions using cookies.
- Connection management evolved from per-request TCP (HTTP/1.0) to persistent connections (HTTP/1.1) and multiplexing in a single connection (HTTP/2); QUIC is explored for improved transport.
- Headers control behaviors like caching policies, authentication, content negotiation (media types, language), compression, range requests, and cross-origin access (CORS).
- HTTP messages consist of methods, status codes, headers, and bodies; APIs like Fetch build on these semantics.