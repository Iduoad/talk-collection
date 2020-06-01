---
title: Kubernetes Storage Lingo 101 (Kubernetes Storage Lingo 101)
description: Introduction to the storage ecosystem and terminology in kubernetes.
type: talk
speaker: Saad Ali
source: https://www.youtube.com/watch?v=uSxlgK1bCuA
tags: ['Kubernetes','Storage']
---

## The Goal: Workload Portability
- **Workload portability **: write your app once and deploy it anyware. This is achieved by abstracting away cluster details and decoupling the infra from the apps.
- Pods and replicaSets abstract compute and memory very well, but what about state ?
    - P1: Containers are ephemeral (data is lost if the container crashes).
    - P2: Containers can't share data between them.

## Challenges with abstracting storage:
- So many different types of storage:
    - Object storage
    - SQL databases
    - NoSQL databases
    - Pub/Sub systems
    - Time series databases
    - File Storage
    - Block Storage
    - File on Block
    - ...
## Solution
- K8s dev focus on the following types because the data path is standardized (Posix, ISCSI)
    - File Storage
    - Block Storage
    - File on Block
## Volume and Volume Plugins
- The way K8s abstracts away the storage part is by using Volume plugins. They specify:
    - How the volume is setup in the pod
    - Medium that backs it.
- Volume have a lifetime same as the pod's or longer.
- There are 5 categories or volume plugins that k8s supports:
    1. Remote storage:
        - AWS ebs
        - GCE PD
        - ...
    2. Ephemeral Storage:
        - EmptyDir
        - Expose k8s API
            - Secret
            - ConfigMap
            - Downward API
    3. Local Persistent Volumes (Beta)
    4. Out-of-Tree
        - Flex (exec a Binary)
        - CSI (Beta)
    5. Other
        - Host Path
### Ephemeral Storage
- Referenced in-line, not via PV/PVC.
- Volumes that expose k8s API objects are based on emptyDirs
### Remote Storage
- Can be referenced using PV/PVC.
- PV/PVC decouples volumes implementation (PV) from their consumption (PVC)
- PVs can be provisioned statically or dynamically using Storage Classes.
### Host Paths
- Host paths are to use with caution. Never use them unless you know what you are doing.
- One use case is to use them along with Node Affinity to keep some stateful apps in some nodes.
### Local Persistent Volume
- They expose a local block or file as PV.
- 2 use cases:
  - Building distributed storage systems on top of k8s
  - Building high performance caching.
### Out-of-Tree
- The volume plugins are in tree i.e. they live inside k8s codebase.
    - Powerful abstraction for block and file storage.
    - Automate Provisioning.
    - Storage portability (PV/PVC)
- There are two iniative of bringing storage out of k8s code tree:
    - CSI (Container Storage Interface): Plugins may be containerized.
    - Flex Volumes: exec based i.e. binaries that need to be installed on the nodes (slave and master). It needs Master access.
