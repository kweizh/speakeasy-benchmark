import os
import pytest

PROJECT_DIR = "/home/user/myproject"
GENIGNORE_FILE = os.path.join(PROJECT_DIR, ".genignore")

def test_genignore_exists():
    assert os.path.isfile(GENIGNORE_FILE), f"The file {GENIGNORE_FILE} does not exist."

def test_genignore_contains_rule():
    with open(GENIGNORE_FILE, 'r') as f:
        content = f.read()
    assert "src/sdk/custom_logic.py" in content, "The .genignore file does not contain 'src/sdk/custom_logic.py'."
