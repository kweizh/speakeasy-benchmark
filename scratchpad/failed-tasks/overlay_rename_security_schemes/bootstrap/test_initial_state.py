import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_openapi_file_exists():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    assert os.path.isfile(openapi_path), f"OpenAPI file {openapi_path} does not exist."

def test_initial_security_scheme_exists():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    with open(openapi_path, "r") as f:
        content = f.read()
    assert "api_key:" in content, "Expected initial security scheme 'api_key' in openapi.yaml."
    assert "ApiKeyAuth" not in content, "Expected 'ApiKeyAuth' to not be in openapi.yaml initially."
