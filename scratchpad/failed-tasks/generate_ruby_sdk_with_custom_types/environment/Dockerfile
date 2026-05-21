FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy CLI with a basic OpenAPI spec in /home/user/project"

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >openapi.yaml <<'EOF'
openapi: 3.1.0
info:
  title: Example API
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /hello:
    get:
      operationId: getHello
      responses:
        "200":
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
#   - Speakeasy CLI installed
#   - /home/user/project - working directory
#   - openapi.yaml - basic OpenAPI spec

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
