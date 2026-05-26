Keeping generated artifacts in sync with backend API changes requires automation. Speakeasy uses a `workflow.yaml` file to define CI/CD pipelines that manage generation and publishing.

You need to configure a `.speakeasy/workflow.yaml` file that is designed to be executed via GitHub Actions to automatically trigger the regeneration of a Python SDK whenever the `openapi.yaml` file in the repository changes.

**Constraints:**
- The workflow configuration MUST target a Python SDK build.
- The configuration MUST properly reference the `SPEAKEASY_API_KEY` environment variable for authentication.