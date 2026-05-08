import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."

def test_go_binary_available():
    assert shutil.which("go") is not None, "go binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_openapi_yaml_exists():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    assert os.path.isfile(openapi_path), f"OpenAPI spec {openapi_path} does not exist."

def test_gen_yaml_exists():
    gen_path = os.path.join(PROJECT_DIR, "gen.yaml")
    assert os.path.isfile(gen_path), f"Config file {gen_path} does not exist."

def test_gen_yaml_configured_for_go():
    gen_path = os.path.join(PROJECT_DIR, "gen.yaml")
    with open(gen_path, 'r') as f:
        content = f.read()
    assert "go:" in content, "Expected gen.yaml to be configured for Go SDK generation."
