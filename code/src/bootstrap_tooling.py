"""
Bootstrap helper to access the paper-tooling submodule from notebooks and scripts.

This module provides a setup function that adds the tooling submodule to sys.path
so that andrewdamico helpers can be imported.
"""
import sys
from pathlib import Path


def setup_tooling(project_root=None):
    """
    Add the paper-tooling submodule to sys.path for importing andrewdamico helpers.
    
    Args:
        project_root: Optional explicit project root. If None, will search upward
                     from this file's location to find tooling/paper-tooling.
    
    Returns:
        Path: The resolved project root directory
    
    Usage in notebooks:
        from code.src.bootstrap_tooling import setup_tooling
        setup_tooling()
        import andrewdamico as ad
        
        run_id = ad.start_run(label="exp1")
        ad.export_figure(name="my_plot", fig=None, formats=["pdf", "png"])
    """
    if project_root is None:
        # Search upward from this file's location
        current = Path(__file__).resolve().parent
        
        while current != current.parent:
            tooling_path = current / "tooling" / "paper-tooling"
            if tooling_path.exists():
                project_root = current
                break
            current = current.parent
        
        if project_root is None:
            # Fallback to current working directory
            project_root = Path.cwd()
    else:
        project_root = Path(project_root).resolve()
    
    tooling_path = project_root / "tooling" / "paper-tooling"
    
    if not tooling_path.exists():
        raise FileNotFoundError(
            f"Tooling submodule not found at {tooling_path}. "
            "Initialize it with: git submodule update --init --recursive"
        )
    
    # Add to sys.path if not already present
    tooling_str = str(tooling_path)
    if tooling_str not in sys.path:
        sys.path.insert(0, tooling_str)
    
    return project_root
