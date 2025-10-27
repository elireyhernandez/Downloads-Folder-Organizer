# utils.py
from datetime import datetime
from pathlib import Path


# ------------------------------------------------------------
#  Utility: Logging helper for all file move operations
# ------------------------------------------------------------
def log_action(message: str, is_first_entry: bool = False):
    """
    Write a timestamped log entry to logs/activity.log.

    Args:
        message (str): Description of the action performed (e.g., "Moved fileA.txt → Documents/")
        is_first_entry (bool): If True, creates a new timestamp header for a batch of moves.
    """

    # Ensure the logs directory exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Define the log file path
    log_file = log_dir / "activity.log"

    # Create a timestamp for the log entry
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    # Append the log entry to the file
    with open(log_file, "a", encoding="utf-8") as f:
        # Add time stamp header at the start of a batch
        if is_first_entry:
            f.write(f"\n{timestamp}\n")
            
        # Write the log message
        f.write(f"{message}\n")
