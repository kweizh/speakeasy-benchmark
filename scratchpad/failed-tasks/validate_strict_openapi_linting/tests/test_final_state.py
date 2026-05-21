import os
import pytest

PROJECT_DIR = "/home/user/project"
LINT_RESULTS_FILE = os.path.join(PROJECT_DIR, "lint_results.txt")

def test_lint_results_file_exists():
    """Verify that the lint results file was created."""
    assert os.path.isfile(LINT_RESULTS_FILE), \
        f"Expected lint results file at {LINT_RESULTS_FILE} but it was not found."

def test_lint_results_content():
    """Verify that the lint results contain expected output from the owasp ruleset."""
    with open(LINT_RESULTS_FILE, "r") as f:
        content = f.read()
    
    assert "OpenAPI document linting complete" in content, \
        f"Expected 'OpenAPI document linting complete' in {LINT_RESULTS_FILE}."
    
    # The speakeasy validation using owasp ruleset should report errors for our intentionally flawed spec
    assert "error" in content.lower(), \
        f"Expected validation errors to be listed in {LINT_RESULTS_FILE}."
    
    # Check for specific OWASP ruleset error like owasp-protection-global-unsafe-strict or owasp-rate-limit
    assert "owasp" in content.lower(), \
        f"Expected 'owasp' ruleset errors in {LINT_RESULTS_FILE}, indicating the correct ruleset was used."
