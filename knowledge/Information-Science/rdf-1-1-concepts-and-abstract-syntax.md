---
source_url: https://www.w3.org/TR/rdf11-concepts/
author: Richard Cyganiak, David Wood, Markus Lanthaler
date: 25-02-2014
---

# RDF 1.1 Concepts and Abstract Syntax

The Resource Description Framework (RDF) is a W3C standard framework for representing information on the Web using a graph-based data model. The fundamental unit of RDF is a triple, which consists of a subject, a predicate, and an object, forming a statement about a resource. This document defines the formal concepts and abstract syntax that provide the foundation for RDF semantics, detailing core components like IRIs, literals, and blank nodes.

*   **Graph Data Model:** RDF represents information as a set of statements in a directed, labeled graph.
*   **RDF Triples:** The basic building block is a triple (subject, predicate, object), which expresses a relationship between resources or between a resource and a value.
*   **Core Components:** Resources are identified by Internationalized Resource Identifiers (IRIs). Values are represented by literals (e.g., strings, numbers), and blank nodes are used for resources without a global identifier.
*   **RDF Graphs and Datasets:** An RDF graph is a set of RDF triples. An RDF dataset is a collection of RDF graphs, which is the unit for SPARQL queries and RDF updates.