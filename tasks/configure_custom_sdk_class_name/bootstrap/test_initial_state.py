import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_gen_yaml_exists():
    config_path = os.path.join(PROJECT_DIR, "gen.yaml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

def test_initial_sdk_class_name_not_custom():
    config_path = os.path.join(PROJECT_DIR, "gen.yaml")
    with open(config_path) as f:
        content = f.read()
    assert "sdkClassName: MyCustomSDK" not in content, \
        "Expected initial sdkClassName to not be MyCustomSDK yet."
