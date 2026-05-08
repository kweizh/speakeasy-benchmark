FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    curl -fsSL https://go.speakeasy.com/cli-install.sh | sed 's/sudo -p "sudo password required for installing to $INSTALL_DIR: " -- sh -c "$sudo_cmd"/eval "$sudo_cmd"/g' | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy project with an initial openapi.yaml in /home/user/myproject."

RUN mkdir -p /home/user/myproject && \
    cd /home/user/myproject && \
    cat >openapi.yaml <<'EOF'
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /ping:
    get:
      operationId: ping
      responses:
        '200':
          description: OK
EOF

# Container contents:
#   - speakeasy CLI installed
#   - /home/user/myproject  — speakeasy project with initial openapi.yaml

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
