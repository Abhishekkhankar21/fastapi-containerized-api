# docker-fastapi-test

. FastAPI Dockerized Application with CI/CD & Monitoring

This project demonstrates a complete DevOps implementation of a FastAPI application, including containerization, data persistence, CI/CD pipeline, and monitoring using Prometheus and Grafana.

---

. Project Overview

The application provides basic user management APIs:

| Method | Endpoint | Description |
|--------|---------|------------|
| GET | `/` | Returns a welcome message |
| GET | `/users` | Fetch all users |
| POST | `/users` | Add a new user |

Data is stored in a `users.json` file (no database used).

---

. TECH STACK

- FastAPI
- Docker & Docker Compose
- Jenkins (CI/CD)
- Prometheus (Monitoring)
- Grafana (Visualization)

---

. 🐳 Docker Setup

 #Build and Run using Docker Compose

```bash
docker-compose up --build -d

Access Application
FastAPI Docs: http://localhost:8000/docs
Prometheus: http://localhost:9090
Grafana: http://localhost:3000

. Data Persistence
User data is stored in data/users.json
Docker volume is used to persist data
Verification Steps:
Add user using POST /users

Stop containers:

docker-compose down

Restart:

docker-compose up -d
Check /users → Data remains intact ✅

. CI/CD Pipeline (Jenkins)

The Jenkins pipeline automates:

Cloning the repository
Building Docker image
Deploying container
Restarting service

Pipeline Stages:
Clone Repository
Build Docker Image
Deploy Container

📊 Monitoring Setup
Prometheus
Scrapes metrics from FastAPI /metrics endpoint
Configured via prometheus.yml
Grafana
Connected to Prometheus as a data source
Used for visualizing:
Request count
Response time
Error rates
