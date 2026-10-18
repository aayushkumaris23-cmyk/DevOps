# Kubernetes Exercise 1: Hello Pod

## Objective
Deploy an Nginx container on Kubernetes using Minikube.

## Business Scenario
Simulate a Zepto storefront web application using Nginx.

## Tools Used
- Docker Desktop
- Minikube
- kubectl
- Kubernetes
- Nginx

## Implementation
1. Started the Minikube cluster.
2. Created the hello-k8s Pod using the Nginx image.
3. Verified the Pod status.
4. Exposed the Pod using a NodePort Service.
5. Accessed the Nginx welcome page in the browser.

## Commands
- minikube start --driver=docker
- kubectl run hello-k8s --image=nginx --port=80
- kubectl get pods
- kubectl expose pod hello-k8s --type=NodePort --port=80
- kubectl get services
- minikube service hello-k8s

## Result
The Nginx welcome page was successfully opened through Minikube.

## Evidence
See the evidence folder for Kubernetes command outputs and screenshots.
