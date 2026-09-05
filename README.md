# Docker Two-Tier Flask Application

A two-tier application built with **Flask and MySQL**, containerized using **Docker and Docker Compose**.
The project focuses on Docker image optimization, container security, reliability, automated testing, and CI/CD using GitHub Actions.

## 🗄️ Docker Compose

The application and MySQL database are run as separate containers using Docker Compose.


┌─────────────────────┐
│   Flask Container   │
│      Gunicorn       │
│       Port 5000     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   MySQL Container   │
│       Port 3306     │
└─────────────────────┘


🧪 Automated Testing
Used Pytest to test the application.
Tests are executed in the CI pipeline before the Docker image is built.
If the tests fail, the pipeline stops and the image is not pushed or deployed.
Git Push
   ↓
Pytest
   ↓
 PASS?
  /  \
NO    YES
↓      ↓
STOP  Docker Build
          ↓
      Docker Push
          ↓
        Deploy
🔄 CI/CD

GitHub Actions is used to automate the workflow:

Code Push
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Push Image to Docker Hub
    ↓
Deploy
## Project Structure

![Project Structure](screenshots/project-structure.png)

## Created Dockerfile 

- I used **multi-stage builds** to avoid unnecessary files and dependencies in the final image, keeping the production image smaller.
- I structured the Dockerfile so that the parts that change frequently are placed later. This allows Docker to reuse the already cached layers and makes rebuilds faster.
- I run the container as a **non-root user** to improve container security.
  
![Project Structure](screenshots/dockerfile.png)
