FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash unzip sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://go.speakeasy.com/cli-install.sh | sh

RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && \
    chmod +x /usr/bin/yq

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Speakeasy environment with an initial gen.yaml configuration."

RUN mkdir -p /home/user/project && \
    cd /home/user/project && \
    cat >gen.yaml <<'EOF'
configVersion: 2.0.0
generation:
  sdkClassName: Speakeasy
  maintainOpenAPIOrder: true
  usageSnippets:
    optionalPropertyRendering: withExample
  useClassNamesForArrayFields: true
  fixes:
    nameResolutionDec2023: true
    parameterOrderingFeb2024: true
    requestResponseComponentNamesFeb2024: true
  auth:
    oAuth2ClientCredentialsEnabled: true
    oAuth2PasswordEnabled: true
targets:
  typescript:
    compilerMacOs: tsc
    sdkClassName: Speakeasy
    clientServerStatusCodesAsErrors: true
    flattenGlobalSecurity: true
    imports:
      option: openapi
      paths:
        callbacks: models/callbacks
        errors: models/errors
        operations: models/operations
        shared: models/components
        webhooks: models/webhooks
    inputModelSuffix: input
    maxMethodParams: 0
    outputModelSuffix: output
    responseFormat: flat
    templateVersion: v2
EOF

# Container contents:
#   - speakeasy installed.
#   - yq installed for validation.
#   - /home/user/project  — project directory with initial gen.yaml

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
