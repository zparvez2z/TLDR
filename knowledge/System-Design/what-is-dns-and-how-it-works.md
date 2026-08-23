---
source_url: https://www.cloudflare.com/learning/dns/what-is-dns/
author: Cloudflare
date: 07-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original Cloudflare Learning Center article; this note summarizes DNS purpose, lookup flow, server roles, query types, and caching.
difficulty: Beginner
tags: [system-design, dns, networking, web, infrastructure]
---

# What Is DNS?

## TL;DR

DNS, the Domain Name System, translates human-readable domain names into IP addresses that computers use to find each other.

It is often described as the phonebook of the Internet.

## Core idea

Humans prefer names like:

```text
example.com
```

Computers communicate using IP addresses like:

```text
93.184.216.34
```

DNS connects those two worlds.

```text
domain name → DNS lookup → IP address → browser connects to server
```

## Main DNS server roles

A typical lookup can involve several DNS server types:

- **DNS recursive resolver**: receives the client query and performs the lookup work.
- **Root nameserver**: points the resolver toward the correct top-level domain nameserver.
- **TLD nameserver**: handles domains such as `.com`, `.org`, or country-code domains.
- **Authoritative nameserver**: stores the final DNS records for a domain.

The resolver often caches answers, so not every request needs the full lookup path.

## Simple lookup flow

A simplified lookup looks like this:

```text
browser → recursive resolver → root server → TLD server → authoritative server → IP address → browser
```

The browser can then connect to the server using the returned IP address.

## Key terms

- **Domain name**: human-readable name such as `cloudflare.com`.
- **IP address**: numeric network address used by computers.
- **DNS record**: stored mapping or metadata, such as A, AAAA, CNAME, MX, TXT, or NS records.
- **Recursive resolver**: server that does lookup work for the client.
- **Authoritative nameserver**: server that has the official record for a domain.
- **Caching**: storing DNS answers temporarily to reduce latency and load.
- **TTL**: time to live; how long a DNS answer can be cached.

## Why DNS matters in system design

DNS affects:

- how users reach services;
- failover and traffic routing;
- CDN integration;
- latency before a connection starts;
- service discovery;
- domain ownership and security;
- resilience during outages.

A slow or broken DNS setup can make a healthy application unreachable.

## Common beginner mistakes

- Thinking DNS directly sends website content. It only helps find where to connect.
- Forgetting that DNS answers can be cached.
- Changing DNS records and expecting instant global updates.
- Confusing recursive resolvers with authoritative nameservers.
- Ignoring DNS as part of availability and incident response.

## Mental model

DNS is the address lookup step before a client can talk to a server.

```text
name first, address second, connection third
```

## Related notes

- [Overview of HTTP](overview-of-http-mdn.md)
- [What Is a CDN?](what-is-a-cdn-content-delivery-network-explained.md)
- [Load Balancing](what-is-load-balancing-how-load-balancers-work.md)

## Source

Original source: https://www.cloudflare.com/learning/dns/what-is-dns/
