import os
import subprocess
import sys

def test_initial_state():
    project_dir = "/home/user/project"
    openapi_path = os.path.join(project_dir, "openapi.yaml")
    
    # Check if project directory exists
    if not os.path.exists(project_dir):
        print(f"Error: Project directory {project_dir} does not exist.")
        sys.exit(1)
        
    # Check if openapi.yaml exists
    if not os.path.exists(openapi_path):
        print(f"Error: {openapi_path} does not exist.")
        sys.exit(1)
        
    # Check if speakeasy is installed
    try:
        subprocess.run(["speakeasy", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Speakeasy CLI is not installed or not in PATH.")
        sys.exit(1)
        
    print("Initial state verified successfully.")
    sys.exit(0)

if __name__ == "__main__":
    test_initial_state()
