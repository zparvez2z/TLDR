---
source_url: https://aws.amazon.com/what-is/cdn/
author: Unknown
date: 20-07-2026
---

# What is a CDN? - Content Delivery Network Explained - AWS x facebook linkedin instagram twitch youtube podcasts email California Consumer Privacy Act (CCPA) Opt-Out Icon

A content delivery network (CDN) is a globally distributed system of interconnected edge servers that caches and delivers web content closer to users to reduce latency and improve performance. The article explains why CDNs matter, detailing benefits like faster page loads, lower bandwidth costs, higher availability, and stronger security. It outlines CDN evolution across three generations, the types of content served (static vs dynamic), and how CDNs work via points of presence using caching, dynamic acceleration, and edge logic. Practical use cases highlight high-speed content delivery, real-time streaming, and massive multi-user scaling, with Amazon CloudFront cited as AWS’s CDN service.
- CDNs reduce latency by placing intermediary edge servers between clients and origin servers, cutting round trips and bandwidth usage.
- Key benefits: faster page loads, reduced hosting/bandwidth costs via caching, improved availability and scalability, and DDoS mitigation.
- Evolution: 1st gen focused on traffic management and replication; 2nd gen addressed streaming and mobile with cloud/P2P; 3rd gen emphasizes edge computing and autonomous edge networks.
- Content types: static content is ideal for caching; dynamic content is accelerated via optimized, persistent connections rather than caching.
- How it works: globally distributed points of presence leverage caching, dynamic acceleration, and edge logic to inspect requests, optimize content, and offload origin compute.
- Use cases: global content delivery (e.g., Reuters), real-time streaming at scale (e.g., Hulu), and massive concurrent user support (e.g., King games).
- CDNs enhance user experience by handling traffic spikes and hardware failures, routing intelligently, and serving content from nearby locations.
- Amazon CloudFront is AWS’s CDN service, often used with Amazon S3 for scalable, secure, and cost-effective delivery.