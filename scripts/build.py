#!/usr/bin/env python3
"""
Wrapper script that delegates to the paper-tooling submodule.
This keeps the paper repo minimal and uses shared tooling.
"""
import subprocess
import sys
from pathlib import Path


def main() -> int:
    # Check if submodule exists
    tooling_script = Path(__file__).parent.parent / "tooling" / "paper-tooling" / "scripts" / "build.py"
    
    if not tooling_script.exists():
        print(
            "Error: paper-tooling submodule not found.\n"
            "Please initialize the submodule:\n"
            "  git submodule update --init --recursive",
            file=sys.stderr
        )
        return 1
    
    # Delegate to the real script, passing all arguments
    cmd = [sys.executable, str(tooling_script)] + sys.argv[1:]
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
