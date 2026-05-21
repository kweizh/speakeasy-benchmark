import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
SDK_DIR = os.path.join(PROJECT_DIR, "sdk")
HOOKS_DIR = os.path.join(SDK_DIR, "internal", "hooks")

def test_hooks_directory_exists():
    assert os.path.isdir(HOOKS_DIR), f"Hooks directory {HOOKS_DIR} does not exist. Did you run speakeasy generate sdk?"

def test_registration_file_exists():
    reg_file = os.path.join(HOOKS_DIR, "registration.go")
    assert os.path.isfile(reg_file), f"Registration file {reg_file} does not exist."

def test_hook_implementation_contains_header_injection():
    # Search for the header injection in all .go files in the hooks directory
    found_header = False
    for root, _, files in os.walk(HOOKS_DIR):
        for file in files:
            if file.endswith(".go"):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    if "X-Hook-Injected" in content and "true" in content:
                        found_header = True
                        break
        if found_header:
            break
            
    assert found_header, "Could not find 'X-Hook-Injected' and 'true' in any Go file within the internal/hooks directory."

def test_sdk_compiles_successfully():
    # Run go mod tidy and go build ./... in the sdk directory
    tidy_result = subprocess.run(
        ["go", "mod", "tidy"],
        cwd=SDK_DIR,
        capture_output=True,
        text=True
    )
    assert tidy_result.returncode == 0, f"'go mod tidy' failed: {tidy_result.stderr}"

    build_result = subprocess.run(
        ["go", "build", "./..."],
        cwd=SDK_DIR,
        capture_output=True,
        text=True
    )
    assert build_result.returncode == 0, f"'go build ./...' failed: {build_result.stderr}\n{build_result.stdout}"
