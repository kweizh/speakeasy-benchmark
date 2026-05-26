import os
import subprocess

import pytest

PROJECT_DIR = "/home/user/project"
GEN_YAML = os.path.join(PROJECT_DIR, "gen.yaml")


def _yq(expression: str) -> str:
    result = subprocess.run(
        ["yq", expression, GEN_YAML],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"yq failed for expression {expression!r}: {result.stderr.strip()}"
    )
    return result.stdout.strip()


def test_gen_yaml_is_valid_yaml():
    assert os.path.isfile(GEN_YAML), (
        f"Expected gen.yaml at {GEN_YAML} to still exist after the task."
    )
    # `yq .` validates the YAML structure.
    result = subprocess.run(
        ["yq", ".", GEN_YAML],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"gen.yaml is not valid YAML after the task: {result.stderr.strip()}"
    )


def test_go_module_path_set_to_target():
    value = _yq(".go.modulePath")
    assert value == "github.com/example/my-sdk", (
        f"Expected .go.modulePath in gen.yaml to be 'github.com/example/my-sdk', got {value!r}."
    )


def test_config_version_preserved():
    value = _yq(".configVersion")
    assert value == "2.0.0", (
        f"Expected configVersion to remain '2.0.0' in gen.yaml, got {value!r}."
    )


def test_sdk_class_name_preserved():
    value = _yq(".generation.sdkClassName")
    assert value == "mysdk", (
        f"Expected generation.sdkClassName to remain 'mysdk' in gen.yaml, got {value!r}."
    )


def test_go_version_preserved():
    value = _yq(".go.version")
    assert value and value != "null", (
        f"Expected .go.version to be preserved (non-empty) in gen.yaml, got {value!r}."
    )


def test_go_sdk_package_name_preserved():
    value = _yq(".go.sdkPackageName")
    assert value and value != "null", (
        f"Expected .go.sdkPackageName to be preserved (non-empty) in gen.yaml, got {value!r}."
    )
