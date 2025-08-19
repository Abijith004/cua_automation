import os
import shutil

def run():
    """
    Example desktop automation:
    Creates a folder and moves a sample file into it.
    """
    base_dir = "outputs/desktop"
    os.makedirs(base_dir, exist_ok=True)

    # Example: create a text file and move it
    sample_file = "sample.txt"
    with open(sample_file, "w") as f:
        f.write("This is a sample file created by desktop automation.")

    shutil.move(sample_file, os.path.join(base_dir, sample_file))
    print(f"[Desktop Automation] Moved {sample_file} into {base_dir}")
