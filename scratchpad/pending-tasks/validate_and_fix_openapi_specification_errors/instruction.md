Speakeasy enforces strict validation rules on OpenAPI specifications to ensure high-quality, generation-safe code output. A provided `broken_openapi.yaml` file fails validation due to missing required schema fields and invalid references.

You need to use the `speakeasy validate` command to identify the schema errors in `broken_openapi.yaml` and output a corrected file named `fixed_openapi.yaml` that resolves all issues.

**Constraints:**
- The original `broken_openapi.yaml` MUST remain entirely unmodified.
- The resulting `fixed_openapi.yaml` MUST return zero errors when tested with `speakeasy validate`.