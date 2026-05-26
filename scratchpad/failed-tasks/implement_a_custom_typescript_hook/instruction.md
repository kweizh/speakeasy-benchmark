While Speakeasy generates idiomatic code, developers occasionally need to inject custom runtime logic into the request lifecycle without breaking the "generation-safe" structure of the project.

You need to implement a custom TypeScript hook within the designated hooks directory that intercepts every outgoing API request and injects a dynamic `X-Organization-Id` header based on the current execution environment.

**Constraints:**
- The hook MUST be correctly registered in the Speakeasy hooks registry file.
- You MUST NOT manually modify any auto-generated SDK files outside of the designated `src/hooks/` directory.