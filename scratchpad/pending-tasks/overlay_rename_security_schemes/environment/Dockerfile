FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy environment with an initial openapi.yaml containing an api_key security scheme."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >openapi.yaml <<'EOF'
openapi: 3.1.0
info:
  title: Test API
  version: 1.0.0
servers:
  - url: http://api.example.com
security:
  - api_key: []
paths:
  /ping:
    get:
      summary: Ping
      responses:
        '200':
          description: OK
components:
  securitySchemes:
    api_key:
      type: apiKey
      name: X-API-Key
      in: header
EOF

# Container contents:
#   - Speakeasy CLI installed.
#   - /home/user/project  — project directory
#   - openapi.yaml with api_key security scheme

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]