# FastAPI Kubernetes Platform

This project demonstrates a production-style microservice setup using **FastAPI**, **Docker**, and **Kubernetes (Kind)** — simulating the workflow of real-world platform teams like those at Spotify.

---

## 🚀 Tech Stack

- **FastAPI** – Python web framework
- **Docker** – Containerized backend
- **Kubernetes** – Container orchestration
- **Kind** – Local Kubernetes cluster for dev/testing
- **kubectl** – CLI for managing cluster
- **VS Code Dev Container** – Reproducible dev environment

---

## 📦 What It Does

- Exposes a `/recommend` endpoint via FastAPI
- Deploys the app to a local Kubernetes cluster using a Deployment + Service
- Uses `NodePort` and `kubectl port-forward` for local access
- Teaches hands-on Kubernetes workflows (pods, services, images, port mapping)

---

## 🛠️ Getting Started

1. Clone the repo  
2. Build and load Docker image into Kind  
3. Apply Kubernetes YAMLs  
4. Access via browser or curl

```bash
kind create cluster
docker build -t fast-api-backend:latest ./backend
kind load docker-image fast-api-backend:latest
kubectl apply -f k8s/fastapi-deployment.yaml
kubectl apply -f k8s/fastapi-service.yaml
kubectl port-forward svc/fastapi-service 8080:80
