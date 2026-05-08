import os
import subprocess
import pytest
import yaml
import ast

PROJECT_DIR = "/home/user/project"

def test_gen_yaml_oauth2_enabled():
    gen_path = os.path.join(PROJECT_DIR, "gen.yaml")
    assert os.path.isfile(gen_path), "gen.yaml not found."
    with open(gen_path) as f:
        config = yaml.safe_load(f)
    auth_config = config.get("generation", {}).get("auth", {})
    assert auth_config.get("OAuth2ClientCredentialsEnabled") is True, \
        "Expected OAuth2ClientCredentialsEnabled: true in gen.yaml under generation.auth."

def test_openapi_yaml_oauth2_scheme():
    openapi_path = os.path.join(PROJECT_DIR, "openapi.yaml")
    assert os.path.isfile(openapi_path), "openapi.yaml not found."
    with open(openapi_path) as f:
        spec = yaml.safe_load(f)
    
    schemes = spec.get("components", {}).get("securitySchemes", {})
    oauth_scheme = None
    for name, scheme in schemes.items():
        if scheme.get("type") == "oauth2":
            oauth_scheme = scheme
            break
    
    assert oauth_scheme is not None, "No oauth2 security scheme found in openapi.yaml."
    
    flows = oauth_scheme.get("flows", {})
    assert "clientCredentials" in flows, "No clientCredentials flow found in oauth2 security scheme."
    
    token_url = flows["clientCredentials"].get("tokenUrl")
    assert token_url == "https://api.example.com/oauth/token", \
        f"Expected tokenUrl to be https://api.example.com/oauth/token, got {token_url}."

def test_sdk_generated():
    sdk_dir = os.path.join(PROJECT_DIR, "sdk")
    assert os.path.isdir(sdk_dir), "SDK directory /home/user/project/sdk does not exist."
    assert os.path.isfile(os.path.join(sdk_dir, "setup.py")) or os.path.isfile(os.path.join(sdk_dir, "pyproject.toml")), \
        "SDK directory does not appear to contain a generated Python SDK (no setup.py or pyproject.toml)."

def test_test_script_exists_and_valid():
    script_path = os.path.join(PROJECT_DIR, "test_sdk.py")
    assert os.path.isfile(script_path), "test_sdk.py not found."
    
    with open(script_path) as f:
        content = f.read()
    
    try:
        ast.parse(content)
    except SyntaxError as e:
        pytest.fail(f"test_sdk.py contains a syntax error: {e}")
    
    assert "test_client" in content, "Expected client ID 'test_client' in test_sdk.py."
    assert "test_secret" in content, "Expected client secret 'test_secret' in test_sdk.py."
