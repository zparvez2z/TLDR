---
source_url: https://aws.amazon.com/message-queue/
author: Amazon Web Services
date: 26-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS message queue article; this note summarizes asynchronous queues, producers, consumers, buffering, decoupling, point-to-point processing, and fanout with pub/sub.
difficulty: Beginner
tags: [system-design, message-queue, asynchronous-processing, microservices, serverless, decoupling]
---

# What Is a Message Queue?

## TL;DR

A message queue is a temporary buffer that lets services communicate asynchronously.

One service sends a message to the queue. Another service later receives, processes, and deletes that message.

The main purpose is to decouple services and smooth out workload spikes.

## Core idea

Without a queue:

```text
service A → direct request → service B
```

If service B is slow or unavailable, service A may also fail or wait.

With a queue:

```text
producer → queue → consumer
```

The producer can place work into the queue and continue. The consumer can process the work when it is ready.

## Key terms

- **Message**: small piece of data, such as a request, reply, error, job, or event.
- **Producer**: component that adds messages to the queue.
- **Queue**: buffer that stores messages temporarily.
- **Consumer**: component that retrieves and processes messages.
- **Point-to-point communication**: each message is normally processed by one consumer.

## Why message queues matter

Message queues help systems become more reliable and scalable.

They can:

- decouple services;
- buffer temporary traffic spikes;
- batch background work;
- reduce direct dependencies between components;
- let slow work happen asynchronously;
- improve reliability when one service is temporarily unavailable;
- support worker pools that scale based on queue length.

## Example

An ecommerce system receives an order.

Instead of making the user wait while the system sends emails, updates inventory, and creates shipping tasks, the system can put background jobs into queues.

```text
order service → queue → email worker
order service → queue → inventory worker
order service → queue → shipping worker
```

The user gets a fast response, and workers process the tasks in the background.

## Queue vs pub/sub

A message queue is usually point-to-point:

```text
one message → one consumer processes it
```

Pub/sub is usually one-to-many:

```text
one message → many subscribers receive it
```

If many systems need to react to the same message, a queue can be combined with pub/sub fanout.

## Common beginner mistakes

- Thinking queues make processing instant. They make processing asynchronous, not necessarily immediate.
- Forgetting retries and dead-letter queues.
- Not making message processing idempotent.
- Using a queue when every consumer must receive every message; that is often pub/sub.
- Ignoring queue depth, processing latency, and failed messages.
- Treating queues as permanent databases.

## Mental model

A message queue is like a task inbox. Producers drop work into the inbox, and workers pick up tasks when they are available.

## Related notes

- [Amazon SQS](fully-managed-message-queuing-amazon-sqs.md)
- [Pub/Sub Messaging](what-is-pub-sub-messaging-aws-explained.md)
- [Event-Driven Architecture](event-driven-architecture-eda-explained-aws.md)
- [Serverless Computing](what-is-serverless-computing-explained-aws.md)

## Source

Original source: https://aws.amazon.com/message-queue/
