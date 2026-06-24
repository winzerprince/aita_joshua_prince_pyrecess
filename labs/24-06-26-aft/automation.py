# Automation and web scraping
# What is automation inpython ?
# Automation in Python refers to the use of Python programming language to automate repetitive tasks, processes,
# or workflows. It involves writing scripts or programs that can perform tasks without human intervention, saving time
# and reducing the potential for errors. Python's simplicity, readability, and extensive libraries make it a popular
# choice for automation.
"""
Automation pipeline
input , transformation, ouput, reliability, running,

"""
# Key automation libraries
# - pathlib: For working with file paths and directories.
# - shutil: For high-level file operations like copying and moving files.
# - schedule: For scheduling tasks to run at specific intervals.
# - watchdog: For monitoring file system events and triggering actions based on changes.
# - openpyxl: For working with Excel files (reading and writing).


# File automation and organization script
#
# Get the file path downloads

# from pathlib import Path
# import os

# # old way using os.path
# file_path = os.path.join(os.path.expanduser("~"), "tmp", "downloads", "file.txt")
#
# # new way
# file_path = Path.home() / "tmp" / "downloads" / "file.txt"
#
# automatically orgainzee fileds into folders by file type

# folder_path = Path.home() / "tmp" / "downloads"
#
# Import libraries

from pathlib import Path
from datetime import datetime
import shutil
from dataclasses import dataclass

# Config


@dataclass(frozen=True)  # this will make the class immutable
class Config:
    DOWNLOADS_DIR: Path = Path.home() / "Downloads"
    ORGANIZED_DIR: Path = DOWNLOADS_DIR / "Organized"
    LOG_FILE: Path = ORGANIZED_DIR / "file_organization.log"


EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".tar.gz", ".rar"],
    "Scripts": [".py", ".js", ".sh"],
    "Code": [".c", ".cpp", ".java", ".cs", ".py", ".js", ".html", ".css"],
    "Others": [],
}

# Logic for file automation


def get_target_folder(file_path: Path) -> Path:
    """Determine the target folder based on file extension."""
    file_name = file_path.name.lower()
    for folder, extensions in EXTENSION_MAP.items():
        if any(file_name.endswith(extension) for extension in extensions):
            return Config.ORGANIZED_DIR / folder
    return Config.ORGANIZED_DIR / "Others"


def ensure_organization_dirs() -> None:
    """Create the output folders before files are moved."""
    Config.ORGANIZED_DIR.mkdir(parents=True, exist_ok=True)
    for folder_name in EXTENSION_MAP:
        (Config.ORGANIZED_DIR / folder_name).mkdir(parents=True, exist_ok=True)
    (Config.ORGANIZED_DIR / "Others").mkdir(parents=True, exist_ok=True)


def log_action(message: str) -> None:
    """Append a timestamped message to the organization log."""
    ensure_organization_dirs()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Config.LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")


def organize_downloads() -> None:
    """Move files from Downloads into type-based folders."""
    ensure_organization_dirs()

    for item in Config.DOWNLOADS_DIR.iterdir():
        if not item.is_file():
            continue
        if item.parent == Config.ORGANIZED_DIR:
            continue

        target_folder = get_target_folder(item)
        target_path = target_folder / item.name

        if target_path.exists():
            suffixes = "".join(item.suffixes)
            base_name = item.name[: -len(suffixes)] if suffixes else item.name
            counter = 1
            while target_path.exists():
                target_path = target_folder / f"{base_name}_{counter}{suffixes}"
                counter += 1

        shutil.move(str(item), str(target_path))
        log_action(f"Moved {item.name} -> {target_path.parent.name}/")


if __name__ == "__main__":
    organize_downloads()
