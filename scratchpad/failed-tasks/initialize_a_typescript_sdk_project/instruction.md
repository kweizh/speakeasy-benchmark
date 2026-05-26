Speakeasy relies on a configured project environment to map an OpenAPI specification to desired generation targets. You have a local `openapi.yaml` file that needs to be configured for a new TypeScript client SDK.

You need to use the Speakeasy CLI to initialize a new project targeting a TypeScript SDK based on the provided `openapi.yaml` file, establishing the core configuration without actually generating the code yet.

**Constraints:**
- The resulting configuration MUST be successfully saved to a `gen.yaml` file.
- Do NOT execute the `speakeasy generate sdk` command; only complete the initialization step.