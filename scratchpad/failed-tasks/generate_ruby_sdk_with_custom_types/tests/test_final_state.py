import os
import pytest

PROJECT_DIR = "/home/user/project"
SDK_DIR = os.path.join(PROJECT_DIR, "sdk")
GEN_YAML_PATH = os.path.join(PROJECT_DIR, "gen.yaml")
GEMSPEC_PATH = os.path.join(SDK_DIR, "my-custom-ruby-sdk.gemspec")

def test_gen_yaml_contains_ruby_config():
    assert os.path.isfile(GEN_YAML_PATH), f"gen.yaml not found at {GEN_YAML_PATH}"
    with open(GEN_YAML_PATH) as f:
        content = f.read()
    
    assert "ruby:" in content, "Expected 'ruby:' block in gen.yaml."
    assert "packageName: my-custom-ruby-sdk" in content or "packageName: \"my-custom-ruby-sdk\"" in content or "packageName: 'my-custom-ruby-sdk'" in content, "Expected packageName to be 'my-custom-ruby-sdk' in gen.yaml."
    assert "module: MyCustomTypesSDK" in content or "module: \"MyCustomTypesSDK\"" in content or "module: 'MyCustomTypesSDK'" in content, "Expected module to be 'MyCustomTypesSDK' in gen.yaml."
    assert "author: Zealt" in content or "author: \"Zealt\"" in content or "author: 'Zealt'" in content, "Expected author to be 'Zealt' in gen.yaml."
    assert "version: 1.0.0" in content or "version: \"1.0.0\"" in content or "version: '1.0.0'" in content, "Expected version to be '1.0.0' in gen.yaml."

def test_sdk_directory_exists():
    assert os.path.isdir(SDK_DIR), f"SDK directory {SDK_DIR} does not exist."

def test_gemspec_exists_and_configured():
    assert os.path.isfile(GEMSPEC_PATH), f"Gemspec file {GEMSPEC_PATH} does not exist."
    with open(GEMSPEC_PATH) as f:
        content = f.read()
    
    assert "my-custom-ruby-sdk" in content, "Expected gemspec to contain the package name 'my-custom-ruby-sdk'."
    assert "1.0.0" in content, "Expected gemspec to contain the version '1.0.0'."
    assert "Zealt" in content, "Expected gemspec to contain the author 'Zealt'."
