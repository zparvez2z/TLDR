---
source_url: https://aws.amazon.com/what-is/pub-sub-messaging/
author: Amazon Web Services
date: 27-07-2026
source_type: learning_article
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS pub/sub messaging article; this note summarizes publishers, topics, subscribers, fanout, filtering, push delivery, queue differences, and AWS AppSync/SNS support.
difficulty: Beginner
tags: [system-design, pub-sub, messaging, event-driven-architecture, fanout, sns]
---

# What Is Pub/Sub Messaging?

## TL;DR

Pub/sub, or publish-subscribe messaging, is an asynchronous communication model where publishers send messages to topics and subscribers receive messages from those topics.

The publisher does not need to know who the subscribers are.

The main purpose is scalable one-to-many event distribution.

## Core idea

Instead of a sender directly calling every receiver:

```text
sender → service A
sender → service B
sender → service C
```

The sender publishes once to a topic:

```text
publisher → topic → subscriber A
                  → subscriber B
                  → subscriber C
```

This reduces tight coupling between systems.

## Key components

- **Message**: data sent through the system.
- **Topic**: channel that groups messages by subject.
- **Publisher**: system that sends messages to a topic.
- **Subscriber**: system that receives messages from a topic.

## Important features

AWS highlights several useful pub/sub features:

- **push delivery**: subscribers are notified when messages are available;
- **multiple delivery protocols**: topics can connect to queues, serverless functions, HTTP endpoints, email, and more;
- **fanout**: one message is copied to multiple subscribers;
- **filtering**: subscribers can receive only messages that match their interests;
- **multiplexing**: systems can publish and subscribe in connected message flows.

## Why pub/sub matters

Pub/sub helps build event-driven systems.

It can:

- eliminate polling;
- deliver updates in near real time;
- let services scale independently;
- simplify integration between many systems;
- support parallel processing;
- improve durability and reliability;
- reduce direct dependencies between producers and consumers.

## Pub/sub vs message queues

Message queues are usually point-to-point:

```text
one message → one consumer
```

Pub/sub is usually one-to-many:

```text
one message → many subscribers
```

Use a queue when one worker should process each task.

Use pub/sub when many systems should react to the same event.

## Example

A payment service publishes this event:

```text
payment.completed
```

Subscribers can react independently:

```text
email service → send receipt
analytics service → update dashboard
shipping service → start fulfillment
fraud service → update risk record
```

The payment service does not need to know all these consumers.

## AWS services

AWS describes two services for pub/sub needs:

- **AWS AppSync** for serverless GraphQL and real-time pub/sub APIs;
- **Amazon SNS** for high-throughput many-to-many pub/sub messaging.

## Common beginner mistakes

- Using pub/sub when exactly one worker should process each task.
- Forgetting message filtering and sending every event to every subscriber.
- Not planning duplicate handling.
- Assuming subscribers always process events instantly.
- Not monitoring failed deliveries.
- Creating too many event types without clear naming rules.

## Mental model

Pub/sub is like a radio broadcast. The broadcaster sends once, and anyone tuned to the channel can receive the message.

## Related notes

- [What Is a Message Queue?](what-is-a-message-queue.md)
- [Amazon SQS](fully-managed-message-queuing-amazon-sqs.md)
- [Event-Driven Architecture](event-driven-architecture-eda-explained-aws.md)
- [Serverless Computing](what-is-serverless-computing-explained-aws.md)

## Source

Original source: https://aws.amazon.com/what-is/pub-sub-messaging/
