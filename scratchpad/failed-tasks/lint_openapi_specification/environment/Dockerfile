FROM ubuntu:24.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip sudo && \
    pip3 install --break-system-packages pytest-json-ctrf pyyaml && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the real Speakeasy CLI using the official install script.
# The install script calls the GitHub API to resolve the latest release. In
# unauthenticated build environments the GitHub API can rate-limit anonymous
# IPs (HTTP 403). When a GITHUB_TOKEN build arg is supplied we forward it to
# the install script so the API call is authenticated and the rate limit is
# raised. The install script installs the `speakeasy` binary directly into
# /usr/local/bin (via sudo), so no extra symlink is needed.
ARG GITHUB_TOKEN=""
RUN GITHUB_TOKEN="${GITHUB_TOKEN}" curl -fsSL https://go.speakeasy.com/cli-install.sh | GITHUB_TOKEN="${GITHUB_TOKEN}" sh && \
    /usr/local/bin/speakeasy --version

RUN mkdir -p /home/user && chmod 0755 /home/user
RUN mkdir -p /home/user/project

# Seed a real, broken-yet-fixable OpenAPI 3.0 specification at
# /home/user/project/openapi.yaml. The spec intentionally contains a
# duplicate `operationId` ("getUser" appears on both GET /users and
# GET /users/{userId}), which Speakeasy's default lint ruleset reports
# as an error (rule: duplicate-operation-id).
RUN cat >/home/user/project/openapi.yaml <<'EOF'
openapi: 3.0.3
info:
  title: User Service API
  version: 1.0.0
  description: A small CRUD API for managing users.
servers:
  - url: https://api.example.com/v1
paths:
  /users:
    get:
      operationId: getUser
      summary: List users
      tags:
        - users
      responses:
        '200':
          description: A list of users.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    post:
      operationId: createUser
      summary: Create a user
      tags:
        - users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '201':
          description: The created user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
  /users/{userId}:
    get:
      operationId: getUser
      summary: Get a user by id
      tags:
        - users
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: The requested user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: string
          description: Unique identifier for the user.
        name:
          type: string
          description: Display name of the user.
        email:
          type: string
          format: email
          description: Contact email for the user.
EOF

LABEL Author="generate-harbor-tasks"
LABEL Description="Speakeasy CLI environment with a broken-yet-fixable OpenAPI 3.0 spec at /home/user/project/openapi.yaml."

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]

# Container contents:
#   - always required apt packages: curl wget ca-certificates git python3 python3-pip python3-pytest bash ripgrep unzip
#   - always required pip3 packages: pytest-json-ctrf
#   - extra pip3 packages: pyyaml (used by initial/final-state tests)
#   - real Speakeasy CLI installed via https://go.speakeasy.com/cli-install.sh and symlinked into /usr/local/bin
#   - /home/user/project: working directory for the lint task
#   - /home/user/project/openapi.yaml: real, intentionally broken OpenAPI 3.0 spec with a duplicate operationId
