# Lint and Fix an OpenAPI Specification with Speakeasy CLI

## Background
A teammate has handed you an OpenAPI 3.0 specification (`openapi.yaml`) that they intend to use as the source for a Speakeasy-generated SDK. Running `speakeasy lint openapi` against the spec currently reports errors that block SDK generation. Your job is to use the Speakeasy CLI to identify the linting errors and edit the spec until the linter reports no errors.

## Requirements
- Use the Speakeasy CLI (`speakeasy lint openapi`) to validate the provided OpenAPI document.
- Edit `openapi.yaml` in place to fix every lint error reported by Speakeasy.
- Keep the existing `info`, `servers`, and overall structure (paths, schemas) intact. Do **not** remove operations or change the HTTP methods/paths.
- After your edits, running `speakeasy lint openapi -s openapi.yaml --non-interactive` must exit with code 0 (no errors). Warnings or hints are acceptable.

## Implementation Hints
- The Speakeasy CLI is preinstalled and available on the `PATH` as `speakeasy`.
- Run the linter to see which rules are violated and which lines/operations are flagged.
- The `--non-interactive` flag is helpful when running the linter from a shell where you only want the textual output.
- Common errors Speakeasy reports include duplicate `operationId` values, missing required OpenAPI fields, and unresolved `$ref` references. Use the messages from the linter as your guide.
- You only need to modify `openapi.yaml`. Do not introduce additional files or change directory layout.

## Acceptance Criteria
- Project path: /home/user/project
- Spec file: /home/user/project/openapi.yaml
- Running `speakeasy lint openapi -s /home/user/project/openapi.yaml --non-interactive` exits with status code 0.
- The spec must still describe at least the original two paths (`/users` and `/users/{userId}`) and define the original `User` schema component.
- The OpenAPI version declared in the spec must remain `3.0.x` (e.g., `3.0.3`).

