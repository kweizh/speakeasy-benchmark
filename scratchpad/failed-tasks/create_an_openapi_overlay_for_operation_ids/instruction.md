Standard OpenAPI specifications often contain cryptic or auto-generated `operationId` values, which lead to poorly named methods in generated SDKs. Speakeasy utilizes standard OpenAPI Overlays to refine these specs dynamically without polluting the source of truth.

You need to create an OpenAPI Overlay file named `overlay.yaml` that updates three specific cryptic operation IDs (e.g., `get_user_xyz123`) into human-readable method names (e.g., `getUser`).

**Constraints:**
- You MUST NOT modify the original OpenAPI specification file.
- The `overlay.yaml` MUST adhere to standard OpenAPI Overlays specifications supported by Speakeasy.