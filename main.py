# main.py
from pathlib import Path
from datetime import datetime
import json

from organizer.sorter import organize_downloads


def main():
    """Main entry point for the Downloads Folder Organizer."""

    # -------------------------------
    # 1. Load configuration settings
    # -------------------------------
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: config.json not found.")
        return

    # Retrieve values from config (with sensible defaults)
    use_test_date = config.get("use_test_date", False)
    test_date_str = config.get("test_date")
    download_path = config.get("download_path", str(Path.home() / "Downloads"))
    mapping = config.get("categories", {})

    # -------------------------------
    # 2. Determine the working date
    # -------------------------------
    if use_test_date and test_date_str:
        today = datetime.fromisoformat(test_date_str)
    else:
        today = datetime.now()

    # -------------------------------
    # 3. Verify the Downloads folder
    # -------------------------------
    download_dir = Path(download_path)

    if not download_dir.exists():
        print(f"Error: The path '{download_dir}' does not exist.")
        print("Using local test folder instead.\n")

        download_dir = Path("Downloads")
        download_dir.mkdir(exist_ok=True)

    # -------------------------------
    # 4. Run the sorting process
    # -------------------------------
    organize_downloads(download_dir, mapping, today)


# --------------------------------------------------
# Standard Python entry point (runs main() directly)
# --------------------------------------------------
if __name__ == "__main__":
    main()
