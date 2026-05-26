import os
import re
import subprocess

import pytest
import yaml

PROJECT_DIR = "/home/user/project"
SPEC_PATH = os.path.join(PROJECT_DIR, "openapi.yaml")


@pytest.fixture(scope="module")
def spec_doc():
    assert os.path.isfile(SPEC_PATH), f"OpenAPI spec {SPEC_PATH} does not exist."
    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_spec_is_valid_yaml(spec_doc):
    assert isinstance(spec_doc, dict), "openapi.yaml must parse to a YAML mapping."


def test_spec_still_declares_openapi_3_0(spec_doc):
    version = str(spec_doc.get("openapi", ""))
    assert version.startswith("3.0"), (
        f"Expected OpenAPI version to remain 3.0.x, got {version!r}."
    )


def test_spec_preserves_original_paths(spec_doc):
    paths = spec_doc.get("paths") or {}
    assert "/users" in paths, "Path `/users` is missing from openapi.yaml."
    assert "/users/{userId}" in paths, (
        "Path `/users/{userId}` is missing from openapi.yaml."
    )


def test_spec_preserves_user_schema(spec_doc):
    components = spec_doc.get("components") or {}
    schemas = components.get("schemas") or {}
    assert "User" in schemas, "Schema component `User` is missing from openapi.yaml."


def test_speakeasy_lint_succeeds():
    """Run the real Speakeasy CLI linter and assert exit code 0."""
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
        timeout=300,
    )
    combined = (result.stdout or "") + "\n" + (result.stderr or "")
    assert result.returncode == 0, (
        "`speakeasy lint openapi` exited with a non-zero status after fixes. "
        f"exit={result.returncode}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
    # Defensive sanity check: the linter summary must not report any errors.
    # Speakeasy prints a final summary line such as "0 errors, N warnings, M hints".
    error_summary = re.search(r"(\d+)\s+errors?", combined, flags=re.IGNORECASE)
    if error_summary is not None:
        count = int(error_summary.group(1))
        assert count == 0, (
            f"Speakeasy lint reported {count} errors after fixes.\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
