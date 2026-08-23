---
source_url: https://aws.amazon.com/architecture/well-architected/
author: Amazon Web Services
date: 24-07-2026
source_type: framework_overview
verified_against_source: true
verified_date: 2026-08-23
verification_scope: Checked against the original AWS Well-Architected page; this note summarizes the framework purpose, six pillars, workload reviews, lenses, guidance, and the Well-Architected Tool.
difficulty: Beginner
tags: [system-design, cloud-architecture, aws, well-architected, reliability, security, cost-optimization]
---

# AWS Well-Architected Framework

## TL;DR

The AWS Well-Architected Framework is a set of best practices for designing, evaluating, and improving cloud workloads.

It helps teams check whether their architecture is secure, reliable, efficient, cost-aware, sustainable, and operationally manageable.

## Core idea

The framework gives cloud teams a consistent way to review architecture decisions.

Instead of asking only:

```text
Does the system work?
```

it asks:

```text
Is the system secure?
Is it reliable?
Can it recover from failure?
Is it cost efficient?
Is it operationally manageable?
Is it sustainable?
Does it use resources efficiently?
```

## The six pillars

AWS organizes the framework around six pillars:

1. **Operational excellence**  
   Run, monitor, and improve systems and operations.

2. **Security**  
   Protect data, systems, identities, permissions, and infrastructure.

3. **Reliability**  
   Make workloads perform correctly and recover from failures.

4. **Performance efficiency**  
   Use computing resources efficiently as requirements change.

5. **Cost optimization**  
   Avoid unnecessary cost while still meeting business and technical goals.

6. **Sustainability**  
   Minimize environmental impact by using resources efficiently.

## Why it matters in system design

A system design answer should not only list components.

It should also explain trade-offs across areas such as:

- availability;
- failure recovery;
- monitoring;
- access control;
- scaling;
- latency;
- cost;
- operational complexity;
- sustainability.

The Well-Architected Framework gives a structured way to think about those trade-offs.

## Well-Architected Tool

AWS provides the AWS Well-Architected Tool in the AWS Management Console.

It helps teams:

- evaluate workloads;
- identify high-risk issues;
- record improvements;
- track architectural review progress.

## Lenses and guidance

The framework is broad.

AWS also provides **Lenses** for specific domains, such as:

- machine learning;
- analytics;
- serverless;
- high performance computing;
- IoT;
- SAP;
- streaming media;
- gaming;
- hybrid networking;
- financial services.

AWS also provides targeted guidance for specific technologies or implementation scenarios.

## Common beginner mistakes

- Thinking architecture quality only means performance.
- Ignoring security until the end.
- Designing for high availability without considering cost.
- Forgetting observability and operational processes.
- Not documenting risks and trade-offs.
- Treating the framework as AWS-only memorization instead of general architecture thinking.

## Mental model

AWS Well-Architected is like a checklist for cloud architecture health. It helps you find weak spots before they become expensive production problems.

## Related notes

- [Serverless Computing](what-is-serverless-computing-explained-aws.md)
- [Availability vs Consistency](availability-vs-consistency-system-design-primer.md)
- [Performance vs Scalability](performance-vs-scalability-system-design-primer.md)
- [Event-Driven Architecture](event-driven-architecture-eda-explained-aws.md)

## Source

Original source: https://aws.amazon.com/architecture/well-architected/
