import os
import shutil
import subprocess
import pytest
import yaml

PROJECT_DIR = "/home/user/project"

def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_openapi_yaml_exists():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    assert os.path.isfile(openapi_path), f"openapi.yaml does not exist at {openapi_path}."

def test_gen_yaml_exists():
    gen_path = os.path.join(PROJECT_DIR, "gen.yaml")
    assert os.path.isfile(gen_path), f"gen.yaml does not exist at {gen_path}."

def test_initial_openapi_lacks_oauth2():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    with open(openapi_path) as f:
        spec = yaml.safe_load(f)
    schemes = spec.get("components", {}).get("securitySchemes", {})
    assert "oauth2" not in str(schemes).lower(), "Expected initial openapi.yaml to lack oauth2 security scheme."

def test_initial_gen_yaml_lacks_oauth2_config():
    gen_path = os.path.join(PROJECT_DIR, "gen.yaml")
    with open(gen_path) as f:
        config = yaml.safe_load(f)
    auth_config = config.get("generation", {}).get("auth", {})
    assert not auth_config.get("OAuth2ClientCredentialsEnabled"), "Expected initial gen.yaml to lack OAuth2ClientCredentialsEnabled: true."
