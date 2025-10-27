# sorter.py
from pathlib import Path
from datetime import datetime
import shutil
import os

from organizer.utils import log_action


# ------------------------------------------------------------
#  Helper: Determine a file's category based on its extension
# ------------------------------------------------------------
def get_file_category(file_path: Path, mapping: dict) -> str:
    """Return the category name (e.g., 'Documents', 'Pictures') based on file extension."""

    ext = file_path.suffix.lower()  # Example: ".jpg"
    for category, extensions in mapping.items():
        if ext in extensions:
            return category

    # Default fallback if extension not found in mapping
    return "Miscellaneous"


# ------------------------------------------------------------
#  Main: Organize files within the Downloads directory
# ------------------------------------------------------------
def organize_downloads(download_dir: Path, mapping: dict, today: datetime):
    """Scan the Downloads folder and move files into category subfolders."""

    categories = list(mapping.keys())
    print(f"Today's Date: {today.date()}\n")

    first_log = True # Tracks if this is the first file being moved

    # Iterate over every item in the directory
    for file in download_dir.iterdir():
        # Skip category folders to prevent recursion
        if file.is_dir() and file.name in categories:
            print(f"Skipping existing category folder: {file.name}")
            continue

                # If it's a folder that's NOT a category folder → move it to Archives
        if file.is_dir() and file.name not in categories:
            destination_folder = download_dir / "Archives"
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder / file.name

            # Handle duplicate folder names
            counter = 1
            while destination.exists():
                new_name = f"{file.name}_{counter}"
                destination = destination_folder / new_name
                counter += 1

            shutil.move(str(file), str(destination))
            print(f"Moved folder {file.name} → {destination}")
            log_action(f"Moved folder {file.name} → {destination}", is_first_entry=first_log)
            first_log = False
            continue  # ✅ skip the rest of the loop for this folder


        # Display current file name
        print(f"Processing: {file.name}")

        # --------------------------------------------
        # Retrieve file's last modification timestamp
        # --------------------------------------------
        stats = os.stat(file)
        mod_time = stats.st_mtime
        readable_time = datetime.fromtimestamp(mod_time)
        mod_date = readable_time.date()
        print(f"Last Modified: {mod_date}")

        # --------------------------------------------
        # Compare modification date vs today's date
        # --------------------------------------------
        if mod_date != today.date():
            category = get_file_category(file, mapping)
            destination_folder = download_dir / category
            destination_folder.mkdir(exist_ok=True)  # Create folder if missing

            destination = destination_folder / file.name

            # Handle duplicate filenames gracefully
            counter = 1
            while destination.exists():
                new_name = f"{file.stem}_{counter}{file.suffix}"
                destination = destination_folder / new_name
                counter += 1

            # Move the file to its categorized folder
            shutil.move(str(file), str(destination))
            print(f"Moved {file.name} → {destination}")
            log_action(f"Moved {file.name} → {destination}", is_first_entry=first_log)
            first_log = False

        elif mod_date == today.date():
            # Skip files downloaded or modified today
            print("This file is from today — skipping.\n")

        else:
            # Unexpected condition (should rarely occur)
            print("Unknown error: could not determine file date.\n")
