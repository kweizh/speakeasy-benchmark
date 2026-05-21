FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy multi-target project setup with an OpenAPI spec in /home/user/project."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat > openapi.yaml <<'EOF'
openapi: 3.0.3
info:
  title: Example API
  version: 1.0.0
paths:
  /hello:
    get:
      operationId: getHello
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
EOF

# Container contents:
#   - speakeasy CLI installed.
#   - /home/user/project - project directory with openapi.yaml

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]