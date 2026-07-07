---
source_url: https://www.cloudflare.com/learning/dns/what-is-dns/
author: Unknown
date: 07-07-2026
---

# What is DNS? | Learning Center

The Domain Name System (DNS) maps human-readable domain names to machine-usable IP addresses, functioning like the Internet’s phonebook. A typical DNS resolution involves several specialized servers that collaboratively translate a hostname to an IP. The process includes potential caching at multiple layers to reduce latency and load, and relies on different query types to efficiently retrieve records. Cloudflare's content also distinguishes between recursive resolvers and authoritative nameservers and outlines the full lookup sequence end-to-end.
- DNS translates domains (e.g., example.com) into IP addresses so browsers can locate Internet resources.
- Four key servers in resolution: recursive resolver, root nameserver, TLD nameserver, and authoritative nameserver.
- Authoritative nameservers store DNS records; recursive resolvers fetch them on behalf of clients and can leverage caching.
- Typical DNS lookup involves up to 8 steps from browser to resolver, root, TLD, and authoritative servers, then back to the client.
- Query types: recursive, iterative, and non-recursive; caching can occur in the browser, OS, and resolvers to speed lookups.
- Cloudflare highlights its role in Internet infrastructure (e.g., hosting part of the F-root) and use of Anycast for resilient, high-volume DNS traffic handling.