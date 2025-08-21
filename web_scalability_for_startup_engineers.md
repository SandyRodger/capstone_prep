## Intro:
- how software architecture and the infrastructure work together to romote scalability
# Chapter 1 : core concepts
(page 1)
- In start-ups one must be as ______ as possible:
  - flexible
  - resourceful
  - adaptable to changing conditions
    - ... because things happen much faster than in a traditional business.
- Scaling up 10x in a few weeks then down again.
- Three pillars of scalability:
  - What it is / how it evolves
  - What it looks like in a large scale application
  - What its application architecture looks like
- Getting comfortable with drawing infrastructure and architecturewill help understand this (also in your next job interview.
## What is scalability 
(page 2)
(page 3)
- "an ability to adjust the capacity of the system to cost-efficiently fulfill the demands. Scalability usually means an ability to handle more users, clients, data, transactions, or requests without affecting the user experience. It's important to remember that scalability should allow us to scale down as much as scale up and that scaling should be relatively cheap and quick to do."
- Most scalability issues can be boiled down to the following issues:
  - handling more data
  - handling higher concurrency levels: how many users can can your system serve at a time without their experience being effected.
  - Handling higher interaction rates
- scalability may be constrained by how many engineers can be working on the system. As the system grows, you will need to consider organizational scalability well.
## Evolution from a sungle server to a global audience
- Single server Configuration
- Making the server stronger: scaling vertically
- Isolation of services
- Content delivery network: Scalability for static content
- Distributing the Traffic: Horizontal scalability
- Scalability for a global architecture
## Overview of a data centre infrastructure
- The front Line
- Web application layer
- Web services layer
- Additional Components
- Data Persistence layer
- Data Center infrastructure
## Overview of the application architecture
- front end
- web services
- supporting technologies
## summary
# Chapter 2: Principles of good software design
## Simplicity
- Hide complexity and build abstractions
- Avoid over-engineering
- Try test-driven development
- Learn from models of simplicity in software design
## Loose coupling
- promoting loose coupling
- avoiding unnecessary coupling
- models of loose coupling
## Don't Repeat Yourself (DRY)
- copy and paste programming
## coding to contract
## Draw Diagrams
- Use case diagrams
- Class diagrams
- module diagrams
## Single responsibility
- promoting single responsibility
- examples of single responsibility
## Open-closed principle
## Dependency injection
## Inversion of Control (IOC)
## Designing for Scale
  - adding more clones
  - Functional partitioning
  - data partitioning
## Design for self-healing
## Summary
