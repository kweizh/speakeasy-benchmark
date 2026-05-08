import os
import subprocess
import sys

def test_final_state():
    project_dir = "/home/user/project"
    
    if not os.path.exists(project_dir):
        print(f"Error: Project directory {project_dir} does not exist.")
        sys.exit(1)
        
    os.chdir(project_dir)
    
    # Check if server.extensions.ts exists
    extensions_file = None
    for root, dirs, files in os.walk("."):
        if "server.extensions.ts" in files:
            extensions_file = os.path.join(root, "server.extensions.ts")
            break
            
    if not extensions_file:
        print("Error: server.extensions.ts not found.")
        sys.exit(1)
            
    # Check if the prompt is registered
    with open(extensions_file, "r") as f:
        content = f.read()
        if "tell-me-a-joke" not in content and "tell_me_a_joke" not in content and "tellMeAJoke" not in content:
            print("Error: tell-me-a-joke prompt not registered in server.extensions.ts.")
            sys.exit(1)
            
    # Check if custom prompt definition exists
    prompt_found = False
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".ts"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    if "tell-me-a-joke" in f.read():
                        prompt_found = True
                        break
        if prompt_found:
            break
            
    if not prompt_found:
        print("Error: custom prompt definition for tell-me-a-joke not found in any .ts file.")
        sys.exit(1)
        
    # Check if the project compiles
    try:
        subprocess.run(["npm", "install"], check=True, capture_output=True)
        subprocess.run(["npm", "run", "build"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Build failed. Output: {e.output.decode() if e.output else e.stderr.decode() if e.stderr else 'Unknown error'}")
        sys.exit(1)
        
    print("Final state verified successfully.")
    sys.exit(0)

if __name__ == "__main__":
    test_final_state()
