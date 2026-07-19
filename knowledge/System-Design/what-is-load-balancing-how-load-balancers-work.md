---
source_url: https://www.cloudflare.com/learning/performance/what-is-load-balancing/
author: Unknown
date: 19-07-2026
---

# What is load balancing? | How load balancers work

Load balancing is the practice of distributing network traffic and computational workloads across multiple servers to improve performance, reliability, and user experience. Load balancers can be hardware or software-based and use algorithms that are either static (predetermined) or dynamic (responsive to server health and capacity). Dynamic approaches rely on server monitoring and health checks to enable failover, ensuring continuity when servers fail. Load balancing is widely used in web applications, data centers, large networks, and globally via GSLB to reduce latency and optimize responsiveness for users. Content delivery networks often include load balancing capabilities to enhance scalability and efficiency.
- Load balancing divides traffic among multiple servers to reduce strain, improve speed, and lower latency.
- Static algorithms (e.g., round-robin DNS, client-side random) are quick to set up but ignore server health, risking inefficiencies.
- Dynamic algorithms (e.g., least connection, weighted least connection, resource-based, geolocation-based) adjust in real time based on server status and workload.
- Server monitoring with regular health checks enables intelligent distribution and rapid failover to backup servers.
- Hardware load balancers require dedicated devices; software/cloud load balancers run on servers, VMs, or in the cloud and may be part of CDNs.
- Global Server Load Balancing (GSLB) spreads traffic across worldwide servers to optimize performance by user location.
- Common use cases include web applications, data centers, and large enterprise networks.