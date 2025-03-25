"""
This script automatically backs up a folder (source_dir) to a destination
directory (destination_dir) once a day at a scheduled time. Each backup is
saved in a new folder named with the current date.
"""

import os
import shutil
import datetime
import time
import schedule


# Folder to back up
SOURCE_DIR = "C:/Users/Debor/OneDrive/Pictures/Screenshots"

# Where to save the backup
DESTINATION_DIR = "C:/Users/Debor/OneDrive/Desktop/Personal Project"


def copy_folder_to_directory(source, dest):
    """
    Copies the entire contents of the source folder to a new folder inside
    the destination directory, named using today's date (YYYY-MM-DD). If the
    folder for today already exists, it skips the copy.
    """
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


# Schedule the backup to run every day at 15:20 (3:20 PM)
schedule.every().day.at("15:20").do(
    lambda: copy_folder_to_directory(SOURCE_DIR, DESTINATION_DIR)
)

# Keep the script running and check every 60 seconds for pending tasks
while True:
    schedule.run_pending()
    time.sleep(60)
