
import sys
import pytest
import os

@pytest.fixture(autouse=True, scope="session")
def fix_sys_path():
    """
    Removes 'universal_mcp/applications' from sys.path to prevent local folders (like openai, elevenlabs)
    from shadowing installed libraries.
    """
    original_path = sys.path[:]
    # Filter out any path ending in 'src/universal_mcp/applications'
    new_path = [p for p in original_path if not p.endswith("src/universal_mcp/applications")]
    
    if len(new_path) < len(original_path):
        sys.path[:] = new_path
        # print("\nDEBUG: Removed colliding paths from sys.path")
