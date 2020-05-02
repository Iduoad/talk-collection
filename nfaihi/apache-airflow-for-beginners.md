---
title: Apache Airflow for beginners
description: An introduction to Airflow for beginners
type: talk
author: Varya Karpenko
source: https://www.youtube.com/watch?v=YWtfU0MQZ_4
tags: ['Apache', 'Airflow', 'Python', 'Data pipelines']
---
- Apache Airflow is a tool to build, schedule and monitor your data pipelines (Set of data processing elements connected in series)
- Building a data pipeline that search for questions for a specific topic on stackoverflow and mail them to your email inbox
- Trying to automate the previous workflow using Airflow
- The 7 building blocks of Airflow
    - **Operator** : (Worker) knows how to perform a task and has the tools to do it (Python operator, Email operator ...)
    - **DAG** : Directed Acyclic Graph, describes the order of the tasks and what to do if one of them fails
    - **Task** : job that is done by an operator (Load data, store data ...)
    - **Connection** : credentials to the external systems that can be securely stored in Airflow
    - **Hooks** : interfaces to the external platforms and databases 
    - **Variables** : like environment variables. Can store arbitrary information and be used in the tasks (URLs, tokens, IDs ...)
    - **XComs** : stands for cross communications between tasks and let them exchange small messages
- Demo of the built pipeline
- You can create your own operator if there is no one that can do the job you wanted