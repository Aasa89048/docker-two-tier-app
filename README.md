this project is about running a multi tier application consist of flask and mysql databse using docker compose
it also explores concepts like multi stage and build cache to optimize the speed and size of container images
using healthchecks and security concepts the reliability of the images and container was assured 
i automated all that (image build optimization,reliability,security,) through a CI/CD using GitHub actions


## Project Structure

![Project Structure](screenshots/project-structure.png)

## Created Dockerfile 

- I used **multi-stage builds** to avoid unnecessary files and dependencies in the final image, keeping the production image smaller.
- I structured the Dockerfile so that the parts that change frequently are placed later. This allows Docker to reuse the already cached layers and makes rebuilds faster.
- I run the container as a **non-root user** to improve container security.
  
![Project Structure](screenshots/dockerfile.png)
