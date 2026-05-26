import os
import subprocess

import pytest
import yaml

PROJECT_DIR = "/home/user/project"
GEN_YAML = os.path.join(PROJECT_DIR, "gen.yaml")


def _run_yq(expression):
    result = subprocess.run(
        ["yq", expression, GEN_YAML],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"yq '{expression}' failed: {result.stderr}"
    return result.stdout.strip()


def test_gen_yaml_exists_and_parses():
    assert os.path.isfile(GEN_YAML), f"gen.yaml not found at {GEN_YAML}."
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "gen.yaml must parse to a top-level YAML mapping."


def test_max_method_params_is_four_via_yq():
    out = _run_yq(".typescript.maxMethodParams")
    assert out == "4", (
        f"Expected `typescript.maxMethodParams` to be `4`, got `{out}` from yq output."
    )


def test_max_method_params_is_four_via_yaml_parse():
    with open(GEN_YAML) as f:
        data = yaml.safe_load(f)
    ts = data.get("typescript", {})
    assert ts.get("maxMethodParams") == 4, (
        f"Expected `typescript.maxMethodParams` to be integer 4, got {ts.get('maxMethodParams')!r}."
    )


def test_typescript_metadata_preserved():
    package_name = _run_yq(".typescript.packageName")
    version = _run_yq(".typescript.version")
    assert package_name == "my-sdk", (
        f"Expected typescript.packageName to remain 'my-sdk', got '{package_name}'."
    )
    assert version == "0.1.0", (
        f"Expected typescript.version to remain '0.1.0', got '{version}'."
    )


def test_other_top_level_blocks_preserved():
    config_version = _run_yq(".configVersion")
    sdk_class_name = _run_yq(".generation.sdkClassName")
    assert config_version == "2.0.0", (
        f"Expected configVersion '2.0.0', got '{config_version}'."
    )
    assert sdk_class_name == "SDK", (
        f"Expected generation.sdkClassName 'SDK', got '{sdk_class_name}'."
    )
