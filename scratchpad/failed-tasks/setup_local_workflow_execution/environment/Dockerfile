FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    curl -fsSL https://go.speakeasy.com/cli-install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user/project && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy workflow execution task environment with a local OpenAPI spec."

RUN cd /home/user/project && \
    cat >openapi.yaml <<'EOF'
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /hello:
    get:
      summary: Say hello
      responses:
        '200':
          description: OK
EOF

# Container contents:
#   - speakeasy CLI installed
#   - /home/user/project  — project directory
#   - /home/user/project/openapi.yaml — OpenAPI specification file

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
