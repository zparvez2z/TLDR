# System Design Learning Path

This page is the study guide for the System Design section of TLDR.

The System Design folder now contains **22 source-reviewed notes**. The goal of this page is to make those notes usable as a learning path instead of leaving them as a flat list of files.

Use this page in two ways:

1. Follow the beginner path if you are learning system design step by step.
2. Jump to the API, traffic, messaging, or cloud sections if you want to revise a specific area.

```text
Current status: 22 System Design notes, 22 source-reviewed, 0 unverified notes
Last learning-path update: 2026-08-25
```

---

## How to study from this folder

A good study loop is:

```text
Read one note → understand the mental model → learn the trade-offs → connect it to the next note
```

System design is not only memorizing components. It is about explaining why one design choice is better than another for a specific workload.

---

## Recommended beginner route

```text
System Design Primer
→ System Design Topics: Start Here
→ Performance vs Scalability
→ Latency vs Throughput
→ Availability vs Consistency
→ CAP Theorem
→ DNS
→ HTTP
→ API
→ REST API
→ API Gateway
→ Load Balancing
→ CDN
→ Caching
→ Browser and CDN Caches
→ Message Queue
→ Pub/Sub Messaging
→ Event-Driven Architecture
→ Serverless Computing
→ AWS Well-Architected Framework
```

---

## 1. Start here

1. [The System Design Primer](system-design-primer.md)  
   Use this as the main map for large-scale system design topics and interview preparation.

2. [System Design Topics: Start Here](system-design-topics-start-here.md)  
   Learn the recommended starting order and the major areas you should understand.

---

## 2. Core system design trade-offs

3. [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)  
   Learn the difference between making one request faster and handling more total load.

4. [Latency vs Throughput](latency-vs-throughput-system-design-primer.md)  
   Learn the difference between response time and total processing capacity.

5. [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)  
   Learn the trade-off between always responding and always returning the freshest data.

6. [CAP Theorem](cap-theorem-consistency-availability-partition-tolerance.md)  
   Learn why distributed systems must choose between consistency and availability during network partitions.

Recommended order:

```text
Performance vs Scalability → Latency vs Throughput → Availability vs Consistency → CAP Theorem
```

---

## 3. Web and network foundations

7. [What Is DNS?](what-is-dns-and-how-it-works.md)  
   Learn how domain names are translated into IP addresses using resolvers, root servers, TLD servers, authoritative nameservers, and caching.

8. [Overview of HTTP](overview-of-http-mdn.md)  
   Learn the Web request/response model, headers, statelessness, cookies, proxies, caching, and connection behavior.

Recommended order:

```text
DNS → HTTP
```

---

## 4. APIs and service entry points

9. [What Is an API?](what-is-an-api-cloudflare-learning.md)  
   Learn how APIs act as contracts between software systems.

10. [What Is a REST API?](what-is-a-rest-api.md)  
    Learn REST as an architectural style based on resources, stateless requests, representations, and cacheability.

11. [What Is an API Gateway?](what-is-an-api-gateway.md)  
    Learn how a gateway provides one controlled entry point for routing, authentication, rate limiting, transformations, caching, and monitoring.

Recommended order:

```text
API → REST API → API Gateway
```

---

## 5. Traffic management and performance

12. [What Is Load Balancing?](what-is-load-balancing-how-load-balancers-work.md)  
    Learn how traffic is distributed across multiple backend servers to improve reliability and scalability.

13. [Load Balancing Algorithms and Types](what-is-load-balancing-algorithms-types-benefits.md)  
    Learn round robin, weighted round robin, IP hash, least connections, least response time, DNS load balancing, and global load balancing.

14. [What Is a CDN?](what-is-a-cdn-content-delivery-network-explained.md)  
    Learn how edge servers reduce latency, lower origin load, and improve availability.

15. [What Is Caching?](what-is-caching-and-how-it-works-aws.md)  
    Learn cache hits, cache misses, TTLs, cache layers, freshness trade-offs, and common caching mistakes.

16. [Caching: Browser and CDN Caches](caching-browser-cdn-cloudflare.md)  
    Learn browser caching, CDN caching, cache hits, cache misses, TTL, and DNS caching from Cloudflare's CDN-focused explanation.

Recommended order:

```text
Load Balancing → Load Balancing Algorithms → CDN → Caching → Browser and CDN Caches
```

---

## 6. Messaging and asynchronous systems

17. [What Is a Message Queue?](what-is-a-message-queue.md)  
    Learn how queues decouple producers and consumers, buffer work, and support background processing.

18. [Amazon SQS: Fully Managed Message Queuing](fully-managed-message-queuing-amazon-sqs.md)  
    Learn SQS as a managed AWS implementation of the message queue pattern.

19. [What Is Pub/Sub Messaging?](what-is-pub-sub-messaging-aws-explained.md)  
    Learn one-to-many messaging with publishers, topics, subscribers, fanout, filtering, and push delivery.

20. [Event-Driven Architecture](event-driven-architecture-eda-explained-aws.md)  
    Learn how systems communicate through events, producers, routers, and consumers.

Recommended order:

```text
Message Queue → Amazon SQS → Pub/Sub Messaging → Event-Driven Architecture
```

---

## 7. Cloud architecture

21. [What Is Serverless Computing?](what-is-serverless-computing-explained-aws.md)  
    Learn managed infrastructure, automatic scaling, pay-for-use billing, FaaS, BaaS, and serverless trade-offs.

22. [AWS Well-Architected Framework](aws-well-architected-framework-overview.md)  
    Learn the six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

Recommended order:

```text
Serverless Computing → AWS Well-Architected Framework
```

---

## Suggested routes by goal

### Learn the basics for interviews

```text
System Design Primer → Performance vs Scalability → Latency vs Throughput → Availability vs Consistency → CAP → DNS → HTTP
```

### Design a web API system

```text
HTTP → API → REST API → API Gateway → Load Balancing → Caching
```

### Design for high traffic

```text
Performance vs Scalability → Latency vs Throughput → Load Balancing → CDN → Caching → Browser and CDN Caches
```

### Design asynchronous microservices

```text
Message Queue → Amazon SQS → Pub/Sub Messaging → Event-Driven Architecture
```

### Think like a cloud architect

```text
Availability vs Consistency → Serverless Computing → AWS Well-Architected Framework
```

---

## Practical revision checklist

After reading the notes, you should be able to answer these questions:

- Where does DNS fit before HTTP requests?
- What is the difference between latency and throughput?
- What is the difference between performance and scalability?
- Why does CAP matter during network partitions?
- When would you use a REST API?
- Why might you put an API Gateway in front of microservices?
- How does a load balancer improve availability?
- What problems can caching solve, and what problems can it create?
- How do browser caches and CDN caches differ?
- When is a CDN useful?
- When should you use a queue instead of direct service calls?
- When should you use pub/sub instead of a queue?
- What makes an architecture event-driven?
- What does serverless actually mean?
- What are the six AWS Well-Architected pillars?

---

## Maintenance note

When adding new System Design notes, connect them to this page if they belong to the main learning path. Advanced papers, vendor-specific details, or implementation guides can stay outside the beginner path unless they explain a core concept.

Keep the beginner path focused on concepts, trade-offs, and mental models.
