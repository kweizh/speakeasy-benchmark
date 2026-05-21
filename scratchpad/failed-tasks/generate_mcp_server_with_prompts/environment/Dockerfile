FROM node:20-bookworm

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install speakeasy CLI
RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

# Set up user and project directory
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER user
WORKDIR /home/user/project

# Copy openapi.yaml
COPY --chown=user:user openapi.yaml /home/user/project/openapi.yaml
