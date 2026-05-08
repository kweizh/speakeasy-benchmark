import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_openapi_spec_exists():
    spec_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    assert os.path.isfile(spec_path), f"OpenAPI spec file {spec_path} does not exist."
