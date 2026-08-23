---
source_url: https://aws.amazon.com/what-is/eda/
author: Amazon Web Services
date: 28-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS event-driven architecture article; this note summarizes events, producers, consumers, routers, loose coupling, scalability, resiliency, push-based flow, and common EDA patterns.
difficulty: Beginner
tags: [system-design, event-driven-architecture, events, microservices, pub-sub, messaging]
---

# Event-Driven Architecture

## TL;DR

Event-driven architecture, or EDA, is a design pattern where services communicate by producing and consuming events.

An event represents a change in state, such as an order being placed, a file being uploaded, or a payment being completed.

The main purpose is loose coupling: producers do not need to know exactly which consumers will react.

## Core idea

In a request-driven system, one service directly asks another service to do something.

```text
service A → call service B
```

In an event-driven system, a service publishes an event, and interested consumers react.

```text
event producer → event router / messaging layer → event consumers
```

This makes the system easier to extend because new consumers can be added without changing the producer.

## Key components

- **Event**: a record that something happened.
- **Producer**: service that creates or publishes the event.
- **Router / broker / messaging layer**: system that receives, filters, routes, buffers, and logs events.
- **Consumer**: service that subscribes to and processes events.

## Why EDA matters

Event-driven systems can:

- reduce tight coupling between services;
- help services scale independently;
- isolate failures;
- reduce polling;
- support near-real-time reactions;
- make workflows easier to extend;
- help handle unpredictable or spiky traffic;
- support auditing by logging event flow.

## Example

An ecommerce system receives an order.

Instead of one large monolith doing everything directly, it publishes an event:

```text
order.created
```

Then several consumers can react:

```text
payment service → authorize payment
inventory service → reserve stock
email service → send confirmation
shipping service → prepare fulfillment
analytics service → record metric
```

Each service can scale and fail independently.

## EDA vs queue vs pub/sub

EDA is the architectural style.

Message queues and pub/sub systems are implementation patterns used inside EDA.

```text
Architecture: Event-Driven Architecture
Building blocks: queues, topics, routers, streams, event buses
```

## Suitable workloads

EDA works well for:

- microservice communication;
- serverless workflows;
- ecommerce order processing;
- business workflow automation;
- infrastructure monitoring and alerting;
- cross-account or cross-region data replication;
- fanout and parallel processing;
- systems with unpredictable traffic.

## Challenges

EDA is powerful, but it adds complexity.

Common challenges include:

- tracing requests across many asynchronous services;
- handling duplicates;
- managing event schemas and versions;
- ensuring idempotent consumers;
- dealing with eventual consistency;
- debugging failures after the original request has ended;
- avoiding event storms and unclear ownership.

## Common beginner mistakes

- Thinking EDA means there are no direct API calls anywhere.
- Not defining event names and schemas clearly.
- Forgetting retries and dead-letter queues.
- Assuming events are processed exactly once.
- Making consumers depend too strongly on producer internals.
- Not monitoring event lag and failed events.

## Mental model

EDA is like a notification system. One service announces that something happened, and other services decide whether to react.

## Related notes

- [Pub/Sub Messaging](what-is-pub-sub-messaging-aws-explained.md)
- [What Is a Message Queue?](what-is-a-message-queue.md)
- [Amazon SQS](fully-managed-message-queuing-amazon-sqs.md)
- [Serverless Computing](what-is-serverless-computing-explained-aws.md)

## Source

Original source: https://aws.amazon.com/what-is/eda/
