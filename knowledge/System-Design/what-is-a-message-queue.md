---
source_url: https://aws.amazon.com/message-queue/
author: Unknown
date: 26-07-2026
---

# What is a Message Queue? x facebook linkedin instagram twitch youtube podcasts email California Consumer Privacy Act (CCPA) Opt-Out Icon

A message queue is an asynchronous communication mechanism used to connect services in serverless and microservices architectures. It temporarily stores messages until a single consumer processes and deletes them, enabling point-to-point communication. Message queues help decouple components, buffer and batch workloads, and smooth spikes to improve performance, reliability, and scalability. They can be combined with Pub/Sub in a fanout pattern when multiple consumers need the same message and are supported on AWS via Amazon SQS and SNS.
- Asynchronous, point-to-point messaging where each message is processed by a single consumer
- Decouples applications and simplifies coding while improving performance, reliability, and scalability
- Buffers and batches work to handle spiky workloads smoothly
- Producers enqueue messages; consumers retrieve and handle them via lightweight queue endpoints
- Use Pub/Sub fanout (e.g., Amazon SNS) when multiple consumers must process the same message
- AWS provides managed queuing via Amazon Simple Queue Service (SQS)