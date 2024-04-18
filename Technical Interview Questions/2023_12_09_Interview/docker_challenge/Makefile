# Makefile for building Ringier Cow Docker image

# Enable Docker BuildKit
export DOCKER_BUILDKIT=1

# Image name and tag
IMAGE_NAME := cowsay
IMAGE_TAG := moo

# Default target
all: build

# Target for building the Docker image
.PHONY: build
build:
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "Docker image built successfully."

# Cow wisdom
talk:
	@echo "Moooooooooo"

# Help target for displaying help information
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  build    - Builds the Docker image using Docker BuildKit."
	@echo "  help     - Displays this help message."
	@echo "  talk      - Get some cow wisdom"
	@echo ""
	@echo "Usage: make [TARGET]"
	@echo "Example: make build"

