# Downloads Folder Organizer

A lightweight Python automation script that keeps your Downloads folder clean and organized automatically.
It sorts older files into categorized folders (Documents, Pictures, Videos, etc.) while leaving today's downloads untouched.

This project began as a simple solution to a real problem — a cluttered Downloads folder.
After scrolling through countless old files, I decided to automate the cleanup process with Python.
It also served as a way to strengthen my understanding of Python syntax, file handling, and automation concepts.

---
## Table of Contents

- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [How it Works](#how-it-works)
- [Project Structure](#project-structure)
- [FAQs](#faqs)
- [Author](#author)
- [LICENSE](#license)

---

## Features

- Automatically organizes files in your Downloads directory
- Leaves today's downloads untouched to avoid moving active work
- Categorizes files by type (PDFs → Documents, JPGs → Pictures, etc.)
- Uses minimal system resources
- Can run twice a day in the background using Windows Task Scheduler
- Keeps a timestamped activity log in `logs/activity.log`

---

## Installation and Setup

### Requirements
- Python 3.9 or higher
- Windows 10 or 11

### Setup Steps
1. Clone or download this repository:
   ```
   git clone https://github.com/elireyhernandez/Downloads-Folder-Organizer.git
   cd downloads-folder-organizer
   ```
2. Extract the zip archive and move your `Downloads-Folder-Organizer-main` somewhere outside your Downloads folder.
- For example, place it in your Documents or Desktop folder.
- This prevents the organizer from accidentally sorting itself!

4. Configure your settings in `config.json`:
   ```
   {
     "use_test_date": false,
     "test_date": "2025-10-30",
     "download_path": "C:/Users/YourName/Downloads",
     "categories": {
       "Documents": [".pdf", ".docx", ".txt"],
       "Pictures": [".jpg", ".png", ".gif"]
     }
   }
   ```

5. Run manually (for testing):
   ```
   python main.py
   ```

6. (Optional) Automate it to run twice a day silently:
   - Run `automation/install_task.vbs`
   - This creates a Windows Task Scheduler entry that executes the script automatically.
   - To remove the task, run `automation/uninstall_task.vbs`.

---

## How It Works

1. The script checks your Downloads directory for files.
2. It compares each file’s last modified date to today’s date.
3. If the file is older than today:
   - It determines the file type based on extension
   - Creates a category folder if needed
   - Moves the file there
4. All actions are logged in `logs/activity.log`.

Example log output:
```
[2025-10-25 22:30:12]
Moved report.pdf → Downloads/Documents/report.pdf
Moved photo.jpg → Downloads/Pictures/photo.jpg
```

---

## Project Structure

```
Downloads Folder Organizer/
│
├── main.py
├── config.json
├── README.md
│
├── automation/
│   ├── install_task.vbs
│   ├── uninstall_task.vbs
│   └── run_organizer.bat
│
├── organizer/
│   ├── sorter.py
│   ├── utils.py
│   └── __init__.py
│
└── logs/
    └── .gitkeep
```

---
## FAQs
### 1. Why doesn’t my custom download_path work in config.json?  
Windows paths copied directly (like C:\Users\YourName\Downloads) use backslashes,  
but JSON treats backslashes as escape characters — which can cause errors when loading the config file.  
  
To fix this, use one of these formats instead:  
Option 1 (Recommended):  
`"download_path": "C:/Users/YourName/Downloads"`  
  
Option 2 (Also valid):  
`"download_path": "C:\\Users\\YourName\\Downloads"`  
  
Avoid using a single backslash (\), or you’ll get an error like:  
json.decoder.JSONDecodeError: Invalid \escape  
  
### 2 When I run run_organizer.bat, it says "Python was not found" or "'python' is not recognized."  
This happens when Python is not installed correctly or was installed without adding it to your system PATH.  
The script depends on Python being globally accessible from the command line.  
  
To fix this:  
1. Install Python 3.9 or newer from [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. During installation, make sure to check the box that says: “Add Python to PATH.”  
3. After installation, open Command Prompt and verify it’s installed correctly:  
`python --version`  
You should see a version number like `Python 3.11.6`  
4. Once Python is working, you can rerun the program or reinstall the scheduled task using `automation/install_task.vbs`  
  
### 3. I’m getting a “Smart App Control blocked a file” message. What should I do?  
Windows Smart App Control or Defender can sometimes block unsigned .vbs or .bat files.  
This happens because the installer script uses Windows Task Scheduler commands (schtasks) to create an automated background task.  
This behavior is normal and safe — the script does not access the internet or make any external changes to your system.  
  
To fix this:  
1. When the system prompts for administrator privileges during installation, click “Yes” to allow the program to continue.  
2. If you see a Smart App Control message, click “More info” → “Run anyway.”  
3. Once installed, the program will run silently in the background and won’t ask for admin rights again unless you uninstall or reinstall it. 
   
Administrative privileges are required only once — during installation — because creating or removing scheduled tasks requires elevated permissions.  
  
### 4. How can I uninstall or stop it from running automatically?  
Run automation/uninstall_task.vbs.  
This removes the scheduled task from Windows Task Scheduler, stopping automatic runs.  
  
### 5. Will this work on macOS or Linux?  
Not yet.  
This version was built for Windows (using Task Scheduler and .bat/.vbs automation).  
Future versions may include cross-platform support.  

---

## Author

Eli Rey Hernandez

GitHub: https://github.com/elireyhernandez

---

## LICENSE

This project is licensed under the MIT License (see LICENSE file for details).
