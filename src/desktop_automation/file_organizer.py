import os
import shutil
from pathlib import Path
from config.constants import DESKTOP_PATH
from utils.logger import setup_logger

logger = setup_logger(__name__)

def organize_files_by_extension(target_dir=DESKTOP_PATH):
    """Sort files into folders based on their extensions."""
    for item in Path(target_dir).iterdir():
        if item.is_file():
            ext = item.suffix[1:]  # Remove dot from .pdf/.txt
            dest_dir = Path(target_dir) / ext
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest_dir))
            logger.info(f"Moved {item.name} to {ext}/")

# Example usage:
# organize_files_by_extension()