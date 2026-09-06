# Docker Two-Tier Flask Application

A production-oriented two-tier Flask application with MySQL, containerized using Docker and Docker Compose.

The project demonstrates practical **DevOps and cloud engineering practices**, including:
- Multi-stage Docker builds
- Non-root containers
- Container healthchecks
- Persistent database storage
- Automated testing with GitHub Actions
- Docker image vulnerability scanning with Docker Scout
- Secure credential management using GitHub Actions Secrets

## Project Structure

![Project Structure](screenshots/project-structure.png)

## Created Dockerfile 

- I used **multi-stage builds** to avoid unnecessary files and dependencies in the final image, keeping the production image smaller.
- I structured the Dockerfile so that the parts that change frequently are placed later. This allows Docker to reuse the already cached layers and makes rebuilds faster.
- I run the container as a **non-root user** to improve container security.
  
![Project Structure](screenshots/dockerfile.png)

## Docker Compose

- I added **healthchecks** to make sure the app and database are healthy, not just running.
- I created a **named volume** to persist database data beyond the container lifecycle.
- i added **Dependency conditions** prevent the application from starting before MySQL is healthy.

![Docker Compose](screenshots/compose.png)

## CI/CD Pipeline

The pipeline performs the following steps:

1. **Checkout** the source code.
2. **Start MySQL** as a GitHub Actions service container.
3. **Install Python dependencies**.
4. **Run automated tests** using Pytest.
5. **Build the Docker image**.
6. **Authenticate with Docker Hub** using GitHub Actions Secrets.
7. **Scan the Docker image** for known vulnerabilities using Docker Scout.

This creates an automated quality and security gate before changes are considered ready for deployment.

![adding the ci](screenshots/ci.png)
---
![the ci testing](screenshots/testsinactions.png)


## Continuous Deployment (CD)

- I created a separate **CD workflow** using GitHub Actions to automatically build and publish the Docker image to Docker Hub whenever changes are pushed to the `main` branch.

- I used **Docker Buildx** to build the production image and **GitHub Secrets** to securely authenticate with Docker Hub.

- I configured **versioned image tags** using the Git commit SHA along with the `latest` tag, making it easier to track releases and identify the exact version of an image.

- The workflow creates a **reproducible deployment artifact** that can be pulled and deployed to a cloud environment.

![CD Pipeline](screenshots/cd.png)

- Github CD workflow

![Github workflow](screenshots/githubcd.png)

- Dockerhub repo with the pushed images

![dockerhub images](screenshots/dockerhub.png)

