---
source_url: https://aws.amazon.com/what-is/serverless-computing/
author: Amazon Web Services
date: 29-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS serverless computing article; this note summarizes managed infrastructure, automatic scaling, pay-for-use billing, FaaS, BaaS, event-driven design, use cases, and shared responsibility.
difficulty: Beginner
tags: [system-design, serverless, faas, baas, cloud, aws, event-driven-architecture]
---

# What Is Serverless Computing?

## TL;DR

Serverless computing is a cloud development model where the cloud provider manages servers, scaling, patching, capacity, and infrastructure operations.

Developers still run code on servers, but they do not manage those servers directly.

The main purpose is to let teams focus more on application logic and less on infrastructure management.

## Core idea

Traditional deployment:

```text
developer manages app + servers + scaling + patches + capacity
```

Serverless deployment:

```text
developer writes code
cloud provider manages infrastructure and scaling
```

Serverless systems often run code in response to events.

```text
event → function runs → result / side effect
```

## Important clarification

Serverless does **not** mean there are no servers.

It means the servers are abstracted away from the developer.

The cloud provider provisions, scales, maintains, monitors, and patches the infrastructure layer.

## Main benefits

AWS highlights several benefits:

- less server management;
- automatic scaling;
- pay-for-use billing;
- built-in high availability in managed services;
- faster development cycles;
- easier integration with managed cloud services.

## Common serverless building blocks

### Function as a Service

FaaS lets developers run small pieces of code on demand.

Example:

```text
file uploaded → function resizes image
```

### Backend as a Service

BaaS provides managed backend capabilities through APIs.

Examples:

- authentication;
- databases;
- storage;
- queues;
- event buses;
- API backends.

## Typical use cases

Serverless is often used for:

- stateless web applications;
- chatbots;
- IoT event handling;
- background jobs;
- batch processing;
- streaming analytics;
- business workflow automation;
- lightweight API backends;
- event-driven microservices.

## Trade-offs

Serverless can simplify operations, but it introduces design trade-offs:

- cold starts can affect latency;
- debugging distributed functions can be harder;
- local testing may not match cloud behavior;
- vendor lock-in can increase;
- long-running workloads may not fit well;
- cost can surprise you at high volume if not monitored;
- application security and permissions remain your responsibility.

## Shared responsibility

The cloud provider manages infrastructure-level responsibilities.

The customer still handles:

- application code;
- data protection;
- identity and access management;
- permissions;
- configuration;
- business logic security.

## Common beginner mistakes

- Thinking serverless means free or always cheaper.
- Ignoring cold starts and latency requirements.
- Putting too much logic in one large function.
- Not setting permissions carefully.
- Forgetting observability, logs, retries, and failure handling.
- Assuming serverless removes all operational responsibility.

## Mental model

Serverless is like renting a kitchen where the building, electricity, cleaning, and scaling are handled for you. You still need to cook the right recipe safely.

## Related notes

- [Event-Driven Architecture](event-driven-architecture-eda-explained-aws.md)
- [Amazon SQS](fully-managed-message-queuing-amazon-sqs.md)
- [Pub/Sub Messaging](what-is-pub-sub-messaging-aws-explained.md)
- [AWS Well-Architected Framework](aws-well-architected-framework-overview.md)

## Source

Original source: https://aws.amazon.com/what-is/serverless-computing/
