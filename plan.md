### 1. Library Overview
*   **Description**: Speakeasy is an AI-native API development platform and "AI control plane." It enables developers to generate idiomatic, type-safe client SDKs, Terraform providers, MCP (Model Context Protocol) servers, and CLIs directly from OpenAPI specifications. It also provides a cloud platform for API registry, versioning, and managed MCP hosting.
*   **Ecosystem Role**: It acts as the bridge between API producers and consumers (including AI agents). It integrates with CI/CD workflows (GitHub Actions) and major AI clients (Claude, Cursor, etc.), providing the necessary artifacts to make APIs reachable and governable.
*   **Project Setup**:
    1.  **Install CLI**:
        ```bash
        # macOS
        brew install speakeasy-api/tap/speakeasy
        # Linux/macOS script
        curl -fsSL https://go.speakeasy.com/cli-install.sh | sh
        ```
    2.  **Authenticate**:
        ```bash
        speakeasy auth login
        ```
        For automated environments/CI, set the `SPEAKEASY_API_KEY` environment variable.
    3.  **Initialize**:
        ```bash
        speakeasy quickstart
        ```
        This command guides you through selecting an OpenAPI spec and choosing targets (SDKs, MCP, etc.).
### 2. Core Primitives & APIs
*   **`gen.yaml`**: The primary configuration file for SDK generation targets. It defines the SDK class name, language-specific options, and features like retries and pagination.
    *   [gen.yaml Reference](https://www.speakeasy.com/docs/speakeasy-reference/generation/gen-yaml)
*   **`workflow.yaml`**: Defines CI/CD workflows for automating the generation and publishing of artifacts.
    *   [Workflow Reference](https://www.speakeasy.com/docs/speakeasy-reference/workflow/workflow-yaml)
*   **CLI Commands**:
    *   `speakeasy generate sdk`: Generates a client SDK from a spec.
    *   `speakeasy validate`: Checks an OpenAPI spec for compatibility and errors.
    *   `speakeasy run`: Executes the workflows defined in the project.
    *   `speakeasy configure`: Interactive command to manage sources, targets, and publishing.
    *   [CLI Reference](https://www.speakeasy.com/docs/speakeasy-reference/cli/getting-started)
*   **OpenAPI Overlays**: A standard-based way to modify or extend an OpenAPI spec without changing the source file, used by Speakeasy to refine the generated output.
    *   [Overlays Documentation](https://www.speakeasy.com/docs/customize/overlays/introduction)
### 3. Real-World Use Cases & Templates
*   **SDK Generation for AI Companies**: Mistral AI uses Speakeasy to generate their Python and TypeScript SDKs.
*   **Infrastructure-as-Code**: Kong uses Speakeasy to generate Terraform providers from their OpenAPI specs.
*   **AI Agent Integration**: Vercel and Docusign use Speakeasy to generate MCP servers, allowing AI agents like Claude to interact directly with their APIs.
*   **Example Project**: [Speakeasy Bar](https://github.com/speakeasy-api/speakeasybar) is a reference implementation showing a complete OpenAPI spec and the resulting generated artifacts.
### 4. Developer Friction Points
*   **OpenAPI Spec Quality**: Speakeasy has strict validation to ensure high-quality code generation. Developers often struggle with fixing spec errors that standard validators might ignore. [Validation Docs](https://www.speakeasy.com/docs/prep-openapi/validation).
*   **Complex Authentication**: Configuring OAuth2 flows (especially Client Credentials or PKCE) in both the spec and `gen.yaml` can be tricky. [Authentication Guide](https://www.speakeasy.com/docs/customize/authentication/configuration).
*   **Customizing Generated Code**: While Speakeasy allows "hooks" and "overlays," understanding where to inject custom logic without breaking the "generation-safe" nature of the project is a common challenge. [Hooks Documentation](https://www.speakeasy.com/docs/customize/code/hooks).
### 5. Evaluation Ideas
*   **Basic**: Initialize a TypeScript SDK project from a local `openapi.yaml` using the CLI.
*   **Intermediate**: Use `speakeasy validate` to identify and fix three specific schema errors in a provided broken OpenAPI spec.
*   **Intermediate**: Configure a GitHub Action workflow to automatically regenerate a Python SDK whenever the OpenAPI spec in the repository changes.
*   **Advanced**: Implement a custom TypeScript hook that injects a dynamic `X-Organization-Id` header into every outgoing API request.
*   **Advanced**: Create an OpenAPI Overlay to rename a set of cryptic operation IDs into human-readable method names without modifying the original spec file.
*   **Complex**: Generate an MCP server from an OpenAPI spec and configure it to use JQ filters to truncate large JSON responses for better LLM performance.
*   **Complex**: Set up a multi-target project (Go SDK and Terraform Provider) sharing the same OpenAPI source with different versioning strategies.
### 6. Sources
1.  [Speakeasy llms.txt](https://www.speakeasy.com/llms.txt) - Structured overview of the platform and documentation.
2.  [Speakeasy Evaluation Guide](https://www.speakeasy.com/eval.md) - Specific guide for AI agents evaluating the platform.
3.  [CLI Getting Started](https://www.speakeasy.com/md/docs/speakeasy-reference/cli/getting-started.md) - Installation and authentication details.
4.  [gen.yaml Reference](https://www.speakeasy.com/md/docs/speakeasy-reference/generation/gen-yaml.md) - Core configuration file details.
5.  [Speakeasy Documentation](https://www.speakeasy.com/docs) - Main documentation portal.