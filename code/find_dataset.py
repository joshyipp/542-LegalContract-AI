"""Module for locating the datasets directory in the project hierarchy."""

import os
from pathlib import Path


def locate(target_dir: str = "Datasets") -> Path:
    """Locate the datasets directory by searching up to 4 levels up in the directory hierarchy.

    Returns:
        Path | None: Path to the datasets directory if found, None otherwise.

    """
    data_dir = Path.cwd()

    # Hardcoded to 4 levels up, change if needed, but should be enough
    for _ in range(4):
        if target_dir in os.listdir(data_dir):
            return Path(data_dir, target_dir)
        data_dir = data_dir.parent

    raise FileNotFoundError(f"Could not find the {target_dir} directory. Please ensure you are running this script from the correct location.")


if __name__ == "__main__":
    print(locate())
