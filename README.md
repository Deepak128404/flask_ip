# Flask IP Display App with CI/CD Pipeline

## Project Overview

This repository contains a Flask application that displays the IP address of the container it's running in. The project demonstrates a complete CI/CD pipeline using GitHub, AWS services (CodePipeline, CodeBuild), and ArgoCD for deployment to Kubernetes.

## Application Details

The core application is a simple Flask app that shows the IP address of its container. It's containerized using a multi-stage Dockerfile for optimal build and runtime environments.

## CI/CD Pipeline

Our CI/CD pipeline consists of the following components:

1. **Source Control**: GitHub (this repository)
2. **Continuous Integration**: AWS CodePipeline and CodeBuild
3. **Container Registry**: DockerHub
4. **Continuous Deployment**: ArgoCD
5. **Deployment Platform**: Kubernetes

### CI Process (AWS CodePipeline and CodeBuild)

The CI process is managed by AWS CodePipeline and executed by CodeBuild. The `buildspec.yml` file in this repository defines the build process:

- Install dependencies
- Run tests (placeholder for actual tests)
- Build Docker image
- Push Docker image to DockerHub

### CD Process (ArgoCD)

ArgoCD is used for continuous delivery to our Kubernetes cluster. It watches this repository for changes in the Kubernetes manifests and ensures that the cluster state matches the desired state defined in the repository.

## Repository Structure

- `/ip_app`: Contains the Flask application code
- `(https://github.com/Deepak128404/argo-cd-menifest-python/tree/main/python-flask-cd)`: Contains Kubernetes manifests (deployment.yaml, service.yaml)
- `Dockerfile`: Multi-stage Dockerfile for building the application
- `buildspec.yml`: AWS CodeBuild specification file
- `requirements.txt`: Python dependencies for the Flask app

## Kubernetes Manifests

The `(https://github.com/Deepak128404/argo-cd-menifest-python/tree/main/python-flask-cd)` repo contains:

1. `deployment.yaml`: Defines the Kubernetes Deployment for the Flask app
2. `svc.yaml`: Defines the Kubernetes Service to expose the app

## Setup and Usage

1. Fork this repository
2. Set up AWS CodePipeline and CodeBuild, pointing to your forked repository
3. Configure AWS Systems Manager Parameter Store with your DockerHub credentials
4. Install ArgoCD in your Kubernetes cluster
5. Configure ArgoCD to watch this repository
6. Push changes to the repository to trigger the CI/CD pipeline

## Security Note

Sensitive information like DockerHub credentials are stored securely in AWS Systems Manager Parameter Store and accessed during the build process.

## Contributions and Feedback

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Deepak128404/flask_ip/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
