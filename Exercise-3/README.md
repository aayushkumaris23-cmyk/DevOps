
# Exercise 3: Scaling Flask App with ReplicaSets

## Objective
- Understand Kubernetes Pods and ReplicaSets.
- Scale a Flask application.
- Observe pod distribution on a single-node Minikube cluster.
- Verify automatic pod replacement.

## Application
The Flask application simulates an e-commerce flash sale.

- `/` - Displays the welcome message and pod hostname.
- `/buy` - Simulates a purchase and identifies the serving pod.
- `/health` - Returns the application health status.

## Files
- `app.py` - Flask application.
- `Dockerfile` - Builds the application container image.
- `flashsale-replicaset.yaml` - Defines the ReplicaSet and Service.

## Lab Procedure
1. Start Minikube.
2. Build the Docker image inside Minikube.
3. Apply the ReplicaSet and Service configuration.
4. Verify the initial three replicas.
5. Scale the ReplicaSet to five replicas.
6. Delete a pod and verify automatic replacement.
7. Inspect pod distribution using `kubectl get pods -o wide`.

## Expected Learning
A ReplicaSet maintains the desired number of pod replicas.
When a pod is deleted, Kubernetes creates a replacement.
All five pods run on the same node in this single-node exercise.
