---
title: Canonical - Using containers to create the World s fastest OpenStack
description: Using LXC/LXD to build fast Openstack clouds.
type: talk
speaker: [Dustin Kirkland, Tycho Andersen]
source: https://www.youtube.com/watch?v=lM2wwYDLB2M
tags:['Cloud','Containers','LXC/LXD', 'OpenStack']
---
## LXC/LXD
- History of compute in the cloud, type hyvervisor -> type2 -> system containers.
- Machine(system) containers boot a full OS in contrast with process containers which boot processes.
- Machine containers look like *VM* but use *Linux containers* technology and run on *Bare Metal*.
- LXD can function in a rootless mode, and provide a Rest api in addition to the CLI interface.
- LXD is a deamon on top of LXC, that works as a abstract layer responsible od the communication with LXC.
- LXD CLI uses the Rest api to communicate with LXD.
- LXD uses ZFS-Linux, which make the containers faster, due to the snapshoting and COW cloning.
    - On create, ZFS make a COW clone of the image. which offer deduplication and efficiency.
    - ZFS also uses integrity checks to catch problems and efficient compression.
- LXD is fast because: Compute (sharing the kernel), Storage (ZFS)
- LXD is secure because: it runs as non-root, has DAC and MAC (AppArmor)

## Why is this the fastest Openstack
1. The cloud in the demo deploys in minutes.
2. Instances launch in seconds.
3. The entire environnement can be snapshot in seconds. (backup)
4. Instances run in nearly bare metal speeds.
5. Services migrate in real-time.

## Demo
- To upgrade Openstack, the the stack is move completely to somewhere else, then Ubuntu and Openstack are getted upgraded
- The speaker could run 636 container on a 16Gi Server. (20 mins for machines to join, and te same amount of time for nodes to draw its ip address)
- The demo uses conjure-up to setup the cluster
- We can run containers inside container without losing performance.
