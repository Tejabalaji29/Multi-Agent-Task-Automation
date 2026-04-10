"""
Tool Definitions
Tools available to agents for task execution.
"""

from typing import Callable, Dict, Any


def file_reader(path: str) -> str:
    """Read contents of a file."""
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {path}"


def file_writer(path: str, content: str) -> str:
    """Write content to a file."""
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"


def execute_command(command: str) -> str:
    """Execute a shell command."""
    import subprocess
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error executing command: {str(e)}"


def search_files(pattern: str, directory: str = ".") -> list:
    """Search for files matching a pattern."""
    import glob
    return glob.glob(f"{directory}/**/{pattern}", recursive=True)


def register_tools() -> Dict[str, Callable]:
    """Register and return all available tools."""
    tools = {
        "file_reader": file_reader,
        "file_writer": file_writer,
        "execute_command": execute_command,
        "search_files": search_files,
    }
    return tools
