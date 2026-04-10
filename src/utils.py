from pathlib import Path


def find_project_root(marker: str = "pyproject.toml") -> Path:
    current = Path(__file__).resolve()  # or Path.cwd() in notebooks
    for parent in [current, *current.parents]:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Project root marker '{marker}' not found")
