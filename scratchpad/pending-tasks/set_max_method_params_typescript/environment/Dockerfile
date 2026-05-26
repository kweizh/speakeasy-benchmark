FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip && \
    pip3 install --break-system-packages pytest-json-ctrf pyyaml && \
    wget -q https://github.com/speakeasy-api/speakeasy/releases/download/v1.765.1/speakeasy_linux_amd64.zip -O /tmp/speakeasy.zip && \
    unzip -q /tmp/speakeasy.zip -d /tmp/speakeasy && \
    mv /tmp/speakeasy/speakeasy /usr/local/bin/speakeasy && \
    chmod +x /usr/local/bin/speakeasy && \
    rm -rf /tmp/speakeasy /tmp/speakeasy.zip && \
    wget -q https://github.com/mikefarah/yq/releases/download/v4.44.3/yq_linux_amd64 -O /usr/local/bin/yq && \
    chmod +x /usr/local/bin/yq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

RUN mkdir -p /home/user/project && \
    cat > /home/user/project/gen.yaml <<'EOF'
configVersion: 2.0.0
generation:
  sdkClassName: SDK
  baseServerURL: https://api.example.com
  maintainOpenAPIOrder: true
  usageSnippets:
    optionalPropertyRendering: withExample
typescript:
  version: 0.1.0
  packageName: my-sdk
  author: Example Author
  maxMethodParams: 0
  flatteningOrder: parameters-first
  methodArguments: infer-optional-args
EOF

LABEL Author="generate-harbor-tasks"
LABEL Description="Speakeasy CLI v1.765.1 environment with a seed gen.yaml for tuning typescript.maxMethodParams."

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]

# Container contents:
#   - always required apt packages: curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip
#   - always required pip3 packages: pytest-json-ctrf
#   - pyyaml: used by the initial/final-state pytest scripts to parse gen.yaml
#   - speakeasy CLI v1.765.1: installed from the official GitHub release into /usr/local/bin/speakeasy
#   - yq v4.44.3: installed from the official GitHub release into /usr/local/bin/yq
#   - /home/user/project: pre-created Speakeasy project directory
#   - /home/user/project/gen.yaml: seed configuration with top-level typescript.maxMethodParams: 0
