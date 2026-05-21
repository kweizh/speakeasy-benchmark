# Configure C# SDK Generation Target

## Background
You have a Speakeasy project initialized with an `openapi.yaml` file. You need to configure a C# SDK generation target and run the generation using the CLI.

## Requirements
- Configure a source named `my-source` pointing to `openapi.yaml`.
- Configure a C# SDK target named `csharp` using `my-source`.
- Set the output directory for the C# target to `./sdk/csharp`.
- Run the Speakeasy CLI to generate the C# SDK.

## Implementation Guide
1. Use `speakeasy configure sources --location openapi.yaml --source-name my-source --non-interactive` to add `openapi.yaml` as `my-source`.
2. Use `speakeasy configure targets --target-type csharp --source my-source --non-interactive --target-name csharp --output ./sdk/csharp` to add a `csharp` target.
3. Run `speakeasy run` to generate the SDK.

## Constraints
- Project path: /home/user/myproject
- The generated SDK must be located in `/home/user/myproject/sdk/csharp`.

## Integrations
- Speakeasy