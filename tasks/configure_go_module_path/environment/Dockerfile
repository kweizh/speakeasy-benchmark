FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip && \
    pip3 install --break-system-packages pytest-json-ctrf && \
    wget -q https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/local/bin/yq && \
    chmod +x /usr/local/bin/yq && \
    wget -q https://github.com/speakeasy-api/speakeasy/releases/download/v1.765.1/speakeasy_linux_amd64.zip -O /tmp/speakeasy.zip && \
    unzip -q /tmp/speakeasy.zip -d /tmp/speakeasy && \
    install -m 0755 /tmp/speakeasy/speakeasy /usr/local/bin/speakeasy && \
    rm -rf /tmp/speakeasy /tmp/speakeasy.zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/user && chmod 0755 /home/user

RUN mkdir -p /home/user/project && \
    cat >/home/user/project/gen.yaml <<'EOF'
configVersion: 2.0.0
generation:
  sdkClassName: mysdk
  maintainOpenAPIOrder: true
  usageSnippets:
    optionalPropertyRendering: withExample
  fixes:
    nameResolutionDec2023: true
    parameterOrderingFeb2024: true
    requestResponseComponentNamesFeb2024: true
go:
  version: 0.1.0
  modulePath: "github.com/my-company/company-go-sdk"
  sdkPackageName: "mysdk"
EOF

LABEL Author="generate-harbor-tasks"
LABEL Description="Speakeasy CLI environment with a seeded gen.yaml that has a Go target using the default module path."

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]

# Container contents:
#   - always required apt packages: curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip
#   - always required pip3 packages: pytest-json-ctrf
#   - yq (mikefarah/yq) installed to /usr/local/bin/yq for inspecting and editing YAML
#   - speakeasy CLI v1.765.1 installed to /usr/local/bin/speakeasy
#   - /home/user/project: project directory with a seeded gen.yaml that includes a top-level
#     `go:` target whose modulePath still has the default value. The executor must change it
#     to `github.com/example/my-sdk`.
