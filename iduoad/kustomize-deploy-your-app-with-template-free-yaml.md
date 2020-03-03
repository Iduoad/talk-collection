---
title: Kustomize: Deploy Your App with Template Free YAML
description: Introduction to a Kustomize, which make you custumize your k8s deployments without templating the yaml files.
type: talk
speaker: Ryan Cox
source: https://www.youtube.com/watch?v=ahMIBxufNR0
---
- Deployment landscape in k8s is quite rich: Weave flux, ksonnet, pulumi, Octupus, DeployHub and Helm ...
- Those tools have a lot of system capabilities
    - Package/Dependency Management
    - Application Descriptors: Metadata, urls to upstreams
    - Application Discovery: places where to search for applications
    - Dashboards
    - Lifecycle Management
    - Customization
- Kustomize's target is customization i.e. it let's you customize your yaml files to your specific env.
- Kustomize read the `kustomization.yaml` file
- [The work behind Kustomize:](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/architecture/declarative-application-management.md)
- Kustomize provides many features:
    - Can add specific annotations, labels, and prefixes in names, namespaces, to secific resources.
    - *Overlays*: create separate kustomization files for each environnement, pulling from a base.
    - *Mix-in configs*: pulls configurations from different bases.
    - *Patches*: operate on existing yaml files, replace or add segments and outputs it.
    - *ConfigMaps/Secret Generators*: generate configmaps push them into the resources.
