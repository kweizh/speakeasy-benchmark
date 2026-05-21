import os

def test_initial_state():
    assert os.path.exists("/home/user/myproject/openapi.yaml"), "openapi.yaml must exist"
    assert not os.path.exists("/home/user/myproject/sdk/csharp"), "sdk/csharp must not exist initially"
