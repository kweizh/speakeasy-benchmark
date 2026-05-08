import os
import pytest

PROJECT_DIR = "/home/user/project"

def test_workflow_yaml_exists():
    workflow_path = os.path.join(PROJECT_DIR, ".speakeasy", "workflow.yaml")
    assert os.path.isfile(workflow_path), f"workflow.yaml not found at {workflow_path}"

def test_workflow_yaml_contents():
    workflow_path = os.path.join(PROJECT_DIR, ".speakeasy", "workflow.yaml")
    with open(workflow_path, "r") as f:
        content = f.read()
        
    assert "workflowVersion: 1.0.0" in content or "workflowVersion: '1.0.0'" in content or 'workflowVersion: "1.0.0"' in content, \
        "Expected workflowVersion to be 1.0.0 in workflow.yaml"
    
    assert "speakeasyVersion: latest" in content or "speakeasyVersion: 'latest'" in content or 'speakeasyVersion: "latest"' in content, \
        "Expected speakeasyVersion to be latest in workflow.yaml"
        
    assert "my-source:" in content, "Expected source named 'my-source' in workflow.yaml"
    assert "openapi.yaml" in content, "Expected source to point to openapi.yaml"
    
    assert "my-python-sdk:" in content, "Expected target named 'my-python-sdk' in workflow.yaml"
    assert "target: python" in content, "Expected target to use python generator"
    assert "source: my-source" in content, "Expected target to use 'my-source' source"
