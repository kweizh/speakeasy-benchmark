FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    ARCH=$(dpkg --print-architecture) && \
    if [ "$ARCH" = "amd64" ]; then \
        curl -fsSL -o speakeasy.zip https://github.com/speakeasy-api/speakeasy/releases/download/v1.762.0/speakeasy_linux_amd64.zip; \
    elif [ "$ARCH" = "arm64" ]; then \
        curl -fsSL -o speakeasy.zip https://github.com/speakeasy-api/speakeasy/releases/download/v1.762.0/speakeasy_linux_arm64.zip; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    unzip speakeasy.zip -d /usr/local/bin && \
    rm speakeasy.zip && \
    chmod +x /usr/local/bin/speakeasy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy project with an initial directory in /home/user/myproject."

RUN mkdir -p /home/user/myproject

# Container contents:
#   - speakeasy installed via direct download
#   - /home/user/myproject — base directory for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
