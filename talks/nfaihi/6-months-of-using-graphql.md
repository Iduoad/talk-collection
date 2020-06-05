---
title: 6 Months Of Using GraphQL
description: Going through some fundamental security practices to protect your infrastructures and how it enhances security
type: article
author: Manish Jain
source: https://levelup.gitconnected.com/6-months-of-using-graphql-faa0fb68b4af
tags: ['GraphQL', 'API', 'Programming']
---
- First, GraphQL is a query language for APIs gives clients the power to ask for exactly what they need and nothing more created by Facebook as an internal solution and was later open-sourced to the community
- The good :
    - **Pragmatic Data Exchange** : send exactly the asked fields, nothing more and nothing less
    - **Using Dataloaders to Reduce Network Calls** : library (not part of GraphQL itself) that can be used to decouple unrelated parts of your application without sacrificing the performance of batch data-loading
    - **Decoupling between exposed data and database models** : decouple the database modeling data with how the data is exposed to consumers. While designing the persistence layer, we could focus on the needs of that layer and then separately think about what's the best way to expose the data to the outside world
    - **Forget about versioning of APIs** : common problem in API is versioning, in GraphQL it is not the case so adding more fields to the an existing endpoint will not break the API
    - **Independent Teams** : the front-end and back-end teams can work independently and the teams can work in parallel
- The bad :
    - **Not all APIs can be evolved** : Sometimes there would be changes tricklingwhich would require a complete change in the implementation of an API (versioning problem)
    - **Unreadable code** : code can become scattered into multiple places while using Dataloaders to fetch the data and that could be difficult to maintain
    - **Longer response times** : queries can evolve and become huge, it can sometimes take a toll on the response time
    - **Caching** : caching is built into in the HTTP specification which RESTful APIs are able to leverage. And as mentioned earlier a GraphQL query can ask for any field of a resource, caching is inherently difficult.
