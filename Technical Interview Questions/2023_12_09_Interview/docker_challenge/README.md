
# Technical Assessment Docker Challenge

## Overview
The application creates a simple HTTP server using Node.js, which responds with an ASCII art representation of a wise cow. It is dockerised for easy deployment and isolation.

## Dockerisation
The application is containerized using Docker, which ensures that it can be run in a consistent environment. The Dockerfile used for this purpose is based on `node:20.10.0-alpine`, keeping the image lightweight. The application listens on port 8080.

## Building and Running the Image
A Makefile is provided for convenience, with a build target to build the Docker image using Docker BuildKit, and a help target for assistance.

### Makefile Usage
- To build the Docker image:
  ```bash
  make build
  ```
- To display help information:
  ```bash
  make help
  ```

## Running the Container
To run the container, use the following command:
```bash
docker run -d -p 8080:8080 --rm --name moo cowsay:moo
```
This command runs the container in detached mode, maps port 8080 of the host to port 8080 of the container, removes the container after it stops, and names the container moo.

## Testing the Application
After running the container, you can test the application using curl by sending a request to localhost:8080. Use the following command:
```bash
curl http://localhost:8080
```
