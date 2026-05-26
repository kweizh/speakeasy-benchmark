import os
import shutil
import subprocess

import pytest

PROJECT_DIR = "/home/user/project"
GEN_YAML = os.path.join(PROJECT_DIR, "gen.yaml")


def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, (
        "speakeasy CLI binary was not found in PATH."
    )


def test_yq_binary_available():
    assert shutil.which("yq") is not None, (
        "yq binary was not found in PATH; it is required to inspect gen.yaml."
    )


def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), (
        f"Expected project directory {PROJECT_DIR} to exist before the task starts."
    )


def test_gen_yaml_exists():
    assert os.path.isfile(GEN_YAML), (
        f"Expected initial gen.yaml at {GEN_YAML} to exist before the task starts."
    )


def test_gen_yaml_has_go_target():
    result = subprocess.run(
        ["yq", ".go", GEN_YAML],
        check=True,
        capture_output=True,
        text=True,
    )
    output = result.stdout.strip()
    assert output and output != "null", (
        "Expected gen.yaml to already contain a top-level 'go:' target section before the task starts."
    )


def test_gen_yaml_module_path_not_target_value():
    result = subprocess.run(
        ["yq", ".go.modulePath", GEN_YAML],
        check=True,
        capture_output=True,
        text=True,
    )
    current = result.stdout.strip()
    assert current != "github.com/example/my-sdk", (
        "Initial gen.yaml already has modulePath set to the target value; "
        "the executor must perform a real change."
    )


def test_gen_yaml_has_config_version():
    result = subprocess.run(
        ["yq", ".configVersion", GEN_YAML],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "2.0.0", (
        "Expected initial gen.yaml to define configVersion: 2.0.0."
    )


def test_gen_yaml_has_sdk_class_name():
    result = subprocess.run(
        ["yq", ".generation.sdkClassName", GEN_YAML],
        check=True,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    assert value and value != "null", (
        "Expected initial gen.yaml to define generation.sdkClassName."
    )
