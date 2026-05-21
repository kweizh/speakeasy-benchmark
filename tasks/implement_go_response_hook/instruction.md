# Implement a Go Response Hook in Speakeasy

## Background
Speakeasy allows customizing generated SDKs using hooks. In this task, you will generate a Go SDK from an OpenAPI specification and implement a custom response hook that intercepts all successful responses and injects a specific header before returning the response to the caller.

## Requirements
- You are provided with a Speakeasy project in `/home/user/project` containing `openapi.yaml` and `gen.yaml` configured for Go SDK generation.
- Run `speakeasy generate sdk` to scaffold the SDK and the `internal/hooks` directory.
- Implement an `AfterSuccessHook` in Go that adds an `X-Hook-Injected` header with the value `true` to every successful HTTP response (`http.Response`).
- Register the hook correctly in the generated registration file so that it is executed by the SDK.
- Ensure the Go code compiles successfully (`go build ./...` inside the `sdk` directory).

## Implementation Guide
1. Move to `/home/user/project`.
2. Run `speakeasy generate sdk` to scaffold the SDK.
3. Create or modify the hook implementation in `sdk/internal/hooks/` to intercept successful responses and append the `X-Hook-Injected: true` header to the `http.Response.Header` map.
4. Register your hook in `sdk/internal/hooks/registration.go`.
5. Run `go mod tidy` and `go build ./...` inside the `sdk` directory to ensure there are no compilation errors.

## Constraints
- Project path: `/home/user/project`
- The header name must be exactly `X-Hook-Injected`.
- The header value must be exactly `true`.
- The SDK language must be Go.
- The hook must be an `AfterSuccessHook`.

## Integrations
- Speakeasy