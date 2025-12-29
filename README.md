# Python To-Do Application (Containerized)

A simple, functional To-Do application built with Python, containerized using Docker, and deployed via Kubernetes. This project demonstrates a full CI/CD-ready workflow for local development to cloud-native deployment.

## 🚀 Features
* Add, view, and delete tasks.
* Lightweight Python backend.
* Fully Dockerized for environment consistency.
* Kubernetes manifests for scalable deployment.

## 🛠️ Tech Stack
* **Language:** Python
* **Containerization:** Docker
* **Orchestration:** Kubernetes (K8s)

## 📋 Prerequisites
* Docker installed locally.
* `kubectl` configured.
* Access to a Docker Registry (Docker Hub).

## 🔧 Setup & Deployment

### 1. Dockerization
Build the image from the Dockerfile:
`docker build -t your-username/todo-app:v1 .`

Push the image to Docker Hub:
`docker push your-username/todo-app:v1`

### 2. Kubernetes Deployment
Apply the deployment configuration:
`kubectl apply -f deployment.yaml`

Expose the application:
`kubectl apply -f service.yaml`

### 3. Access the App
Once the pods are running, access the app via:
`http://localhost:<port>` (or your Cluster IP)
