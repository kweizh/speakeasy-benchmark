import os
import pytest

PROJECT_DIR = "/home/user/project"

def test_python_sdk_generated():
    """Priority 3 fallback: basic file existence check for Python SDK."""
    python_sdk_dir = os.path.join(PROJECT_DIR, "python-sdk")
    assert os.path.isdir(python_sdk_dir), f"Python SDK directory {python_sdk_dir} does not exist."
    
    # Check for typical Python SDK files
    files = os.listdir(python_sdk_dir)
    assert any(f.endswith(".py") for f in files) or "setup.py" in files or "pyproject.toml" in files, \
        f"No Python project files found in {python_sdk_dir}"

def test_go_sdk_generated():
    """Priority 3 fallback: basic file existence check for Go SDK."""
    go_sdk_dir = os.path.join(PROJECT_DIR, "go-sdk")
    assert os.path.isdir(go_sdk_dir), f"Go SDK directory {go_sdk_dir} does not exist."
    
    # Check for typical Go SDK files
    files = os.listdir(go_sdk_dir)
    assert any(f.endswith(".go") for f in files) or "go.mod" in files, \
        f"No Go project files found in {go_sdk_dir}"