import os

def test_final_state():
    assert os.path.exists("/home/user/myproject/.speakeasy/workflow.yaml"), "workflow.yaml must exist"
    assert os.path.exists("/home/user/myproject/sdk/csharp"), "sdk/csharp must exist"
    
    # Check if there are some .cs files
    has_cs_files = False
    for root, dirs, files in os.walk("/home/user/myproject/sdk/csharp"):
        for file in files:
            if file.endswith(".cs"):
                has_cs_files = True
                break
    
    assert has_cs_files, "Generated C# SDK must contain .cs files"
