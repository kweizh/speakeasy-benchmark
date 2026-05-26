import os
import shutil
import subprocess

import pytest
import yaml

PROJECT_DIR = "/home/user/project"
SPEC_PATH = os.path.join(PROJECT_DIR, "openapi.yaml")


def test_speakeasy_binary_available():
    assert shutil.which("speakeasy") is not None, (
        "speakeasy CLI binary not found in PATH; the lint task requires the real Speakeasy CLI."
    )


def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."


def test_openapi_spec_exists():
    assert os.path.isfile(SPEC_PATH), f"OpenAPI spec {SPEC_PATH} does not exist."


def test_openapi_spec_is_valid_yaml():
    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    assert isinstance(doc, dict), "openapi.yaml must parse to a YAML mapping."
    assert "openapi" in doc, "openapi.yaml must declare an `openapi` field."
    assert str(doc["openapi"]).startswith("3.0"), (
        f"Expected openapi 3.0.x in seed spec, got {doc.get('openapi')!r}."
    )
    assert "paths" in doc and isinstance(doc["paths"], dict), (
        "Seed spec must declare a `paths` section."
    )


def test_seed_spec_currently_has_lint_errors():
    """
    The seed openapi.yaml is intentionally broken so the executor has something to fix.
    Running `speakeasy lint openapi` against it must currently fail (non-zero exit).
    """
    result = subprocess.run(
        [
            "speakeasy",
            "lint",
            "openapi",
            "-s",
            SPEC_PATH,
            "--non-interactive",
        ],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert result.returncode != 0, (
        "Seed openapi.yaml should currently fail `speakeasy lint openapi`, "
        f"but the linter reported success.\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
