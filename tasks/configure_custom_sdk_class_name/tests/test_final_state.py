import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_sdk_class_name_updated():
    """Priority 1: Use yq CLI to verify the final state in gen.yaml."""
    result = subprocess.run(
        ["yq", "e", ".targets.typescript.sdkClassName", "gen.yaml"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, \
        f"'yq' command failed: {result.stderr}"
    output = result.stdout.strip()
    assert output == "MyCustomSDK", \
        f"Expected sdkClassName to be 'MyCustomSDK', got: {output}"
