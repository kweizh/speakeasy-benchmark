# Setup Speakeasy Ignore Rules

## Background
You have a Speakeasy Python SDK project in `/home/user/myproject`. You want to customize the generated SDK by modifying a file manually, but you don't want Speakeasy to overwrite your changes during the next generation.

## Requirements
- Create a `.genignore` file in the project root to instruct Speakeasy to ignore specific files.
- Add a rule to ignore the `src/sdk/custom_logic.py` file.

## Implementation Guide
1. Navigate to `/home/user/myproject`.
2. Create a `.genignore` file.
3. Add `src/sdk/custom_logic.py` to the `.genignore` file.

## Constraints
- Project path: `/home/user/myproject`