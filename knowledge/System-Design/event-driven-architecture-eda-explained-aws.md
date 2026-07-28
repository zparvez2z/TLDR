---
source_url: https://aws.amazon.com/what-is/eda/
author: Unknown
date: 28-07-2026
---

# What is EDA? - Event-Driven Architecture Explained - AWS x facebook linkedin instagram twitch youtube podcasts email California Consumer Privacy Act (CCPA) Opt-Out Icon

Event-driven architecture (EDA) is a modern design pattern where small, decoupled services publish, route, and consume events representing changes in state. By promoting loose coupling, EDA enables independent scaling and failure tolerance, reduces complexity, and increases developer agility and extensibility. EDA typically uses an event router and messaging components to push events in real time, avoiding the cost and overhead of polling. It suits highly scalable, highly available, and spikey workloads, and is commonly applied to microservices backends and automated business workflows.
- EDA centers on events (state changes) produced and consumed by decoupled microservices.
- Benefits include independent scaling and failure isolation, reduced workflow complexity, and faster feature delivery.
- Push-based event flows cut costs by eliminating continuous polling and reducing bandwidth, CPU, and idle capacity.
- Event routers filter, route, buffer, and log events, enabling real-time responsiveness and easier auditing and policy control.
- Decoupled data strategies improve fault tolerance, resiliency, and time-to-market for new features.
- Systems are highly extensible: new consumers can be added without changing producers or creating tight dependencies.
- EDA supports decomposing monoliths into domain-driven services communicating asynchronously via queues and routers.
- Well-suited for unpredictable traffic and peak-demand scenarios, exemplified by e-commerce order processing pipelines.
- Common use cases include microservices communication for web/mobile backends and automated, orchestrated business workflows.