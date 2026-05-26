import os
import shutil

import pytest
import yaml

PROJECT_DIR = "/home/user/project"
GEN_YAML = os.path.join(PROJECT_DIR, "gen.yaml")


def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, "speakeasy binary not found in PATH."


def test_yq_binary_available():
    assert shutil.which("yq") is not None, "yq binary not found in PATH."


def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."


def test_gen_yaml_exists():
    assert os.path.isfile(GEN_YAML), f"gen.yaml not found at {GEN_YAML}."


def test_gen_yaml_is_valid_yaml():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "gen.yaml must parse to a mapping at the top level."


def test_gen_yaml_has_typescript_block():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    assert "typescript" in data, "Top-level 'typescript:' block missing from gen.yaml."
    assert isinstance(data["typescript"], dict), "'typescript:' block must be a mapping."


def test_initial_max_method_params_is_zero():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    ts_block = data.get("typescript", {})
    assert ts_block.get("maxMethodParams") == 0, (
        "Initial gen.yaml should have typescript.maxMethodParams: 0 (the default seed value)."
    )


def test_initial_typescript_metadata_fields_present():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    ts_block = data.get("typescript", {})
    assert ts_block.get("packageName") == "my-sdk", "Initial typescript.packageName must be 'my-sdk'."
    assert ts_block.get("version") == "0.1.0", "Initial typescript.version must be '0.1.0'."


def test_initial_top_level_blocks_present():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    assert data.get("configVersion") == "2.0.0", "Initial configVersion must be '2.0.0'."
    assert "generation" in data and isinstance(data["generation"], dict), (
        "Top-level 'generation:' block must exist in the initial gen.yaml."
    )
    assert data["generation"].get("sdkClassName") == "SDK", "Initial generation.sdkClassName must be 'SDK'."
