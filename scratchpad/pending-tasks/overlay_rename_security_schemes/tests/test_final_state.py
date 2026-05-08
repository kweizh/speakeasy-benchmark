import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_overlay_file_exists():
    """Priority 3: Check if overlay.yaml exists."""
    overlay_path = os.path.join(PROJECT_DIR, "overlay.yaml")
    assert os.path.isfile(overlay_path), f"overlay.yaml not found at {overlay_path}"

def test_modified_openapi_file_exists():
    """Priority 3: Check if modified_openapi.yaml exists."""
    modified_path = os.path.join(PROJECT_DIR, "modified_openapi.yaml")
    assert os.path.isfile(modified_path), f"modified_openapi.yaml not found at {modified_path}"

def test_modified_openapi_is_valid():
    """Priority 1: Use Speakeasy CLI to validate the modified OpenAPI spec."""
    result = subprocess.run(
        ["speakeasy", "validate", "-s", "modified_openapi.yaml"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'speakeasy validate' failed: {result.stderr}\n{result.stdout}"

def test_modified_openapi_contains_renamed_scheme():
    """Priority 3: Check the contents of modified_openapi.yaml for the renamed security scheme."""
    modified_path = os.path.join(PROJECT_DIR, "modified_openapi.yaml")
    with open(modified_path, "r") as f:
        content = f.read()
    
    assert "api_key:" not in content, "Expected 'api_key' to be removed from modified_openapi.yaml."
    assert "ApiKeyAuth:" in content, "Expected 'ApiKeyAuth' in modified_openapi.yaml."
    
    # Check global security array uses ApiKeyAuth
    assert "- ApiKeyAuth:" in content or "- ApiKeyAuth: []" in content, "Expected global security array to use 'ApiKeyAuth'."
