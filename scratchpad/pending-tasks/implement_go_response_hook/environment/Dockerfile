FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip sudo golang-go && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

RUN pip3 install --break-system-packages pyyaml

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy project with an initial openapi.yaml and gen.yaml configured for Go SDK generation."

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
  /data:
    get:
      operationId: getData
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
EOF

RUN cd /home/user/project && \
    cat >gen.yaml <<'EOF'
configVersion: 2.0.0
generation:
  sdkClassName: ExampleSDK
  usageSnippets:
    optionalPropertyRendering: withExample
  fixes:
    nameResolutionDec2023: true
    parameterOrderingFeb2024: true
    requestResponseBasedMethodNamesAndTokensApr2024: true
go:
  version: 1.0.0
  packageName: github.com/example/sdk
EOF

# Container contents:
#   - speakeasy CLI installed.
#   - golang-go installed.
#   - /home/user/project  — Speakeasy project with initial config
#   - openapi.yaml
#   - gen.yaml configured for Go

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
