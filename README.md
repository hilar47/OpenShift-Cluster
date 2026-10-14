# OpenShift-Cluster: CI/CD Pipeline with GitHub Actions, Tekton and OpenShift

**Project name:** OpenShift CI/CD Pipeline (oc-pipelines)

**Author:** hilar47

## Overview
A sample Python/Flask application built and deployed with a complete CI/CD pipeline:

- **GitHub Actions** (`.github/workflows/workflow.yml`): lints with flake8 and runs unit tests with nose on every push and pull request.
- **Tekton** (`.tekton/tasks.yml`, `.tekton/pipeline.yml`): cleanup, clone, lint, nose tests, build, deploy.
- **OpenShift Pipelines**: runs the Tekton pipeline (`oc-pipelines`) against a PersistentVolumeClaim workspace and deploys the app.

## Structure
```
.github/workflows/workflow.yml   GitHub Actions CI
.tekton/tasks.yml                Custom Tekton tasks (cleanup, nose)
.tekton/pipeline.yml             Pipeline definition
.tekton/pvc.yml                  PersistentVolumeClaim for the workspace
