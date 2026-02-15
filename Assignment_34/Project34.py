import sys
import os
import time
import shutil
import hashlib
import zipfile
import schedule
import logging
from datetime import datetime

# -------------------- GLOBAL CONFIG --------------------

LOG_DIR = "Logs"
HISTORY_FILE = "backup_history.txt"
EXCLUDE_EXT = [".tmp", ".log", ".exe"]

# -------------------- LOGGER SETUP --------------------

def setup_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    log_filename = os.path.join(LOG_DIR,
        "backup_" + time.strftime("%Y%m%d_%H%M%S") + ".log")

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return log_filename

# -------------------- HASH FUNCTION --------------------

def calculate_hash(path):
    hobj = hashlib.md5()
    with open(path, "rb") as fobj:
        while chunk := fobj.read(1024):
            hobj.update(chunk)
    return hobj.hexdigest()

# -------------------- BACKUP FUNCTION --------------------

def BackupFiles(Source, Destination):
    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            if any(file.endswith(ext) for ext in EXCLUDE_EXT):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
                logging.info(f"Copied: {relative}")

    return copied_files

# -------------------- ZIP FUNCTION --------------------

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zobj:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                zobj.write(full_path, relative)

    return zip_name

# -------------------- HISTORY TRACKER --------------------

def update_history(num_files, zip_name):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{datetime.now()} | Files: {num_files} | Zip: {zip_name}\n")

# -------------------- RESTORE FUNCTION --------------------

def restore_backup(zipfile_name, destination):
    if not os.path.exists(zipfile_name):
        logging.error("Zip file not found")
        return

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zipfile_name, 'r') as zobj:
        zobj.extractall(destination)

    logging.info("Backup restored successfully")

# -------------------- MAIN BACKUP PROCESS --------------------

def MarvellousDataShieldStart(Source):
    BackupName = "MarvellousBackup"

    logging.info("Backup Process Started")

    files = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)

    update_history(len(files), zip_file)

    logging.info(f"Backup Completed | Files: {len(files)} | Zip: {zip_file}")

# -------------------- MAIN FUNCTION --------------------

def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--history":
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE) as f:
                    print(f.read())
            else:
                print("No history found")

        else:
            print("Invalid argument")

    elif len(sys.argv) == 3:
        # python Script.py 5 Data
        interval = int(sys.argv[1])
        source = sys.argv[2]

        log_file = setup_logger()

        schedule.every(interval).minutes.do(MarvellousDataShieldStart, source)

        print("Data Shield System Started...")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        # python Script.py --restore backup.zip Destination
        restore_backup(sys.argv[2], sys.argv[3])
        print("Restore Completed")

    else:
        print("Usage:")
        print("Backup  : Script.py TimeInterval SourceFolder")
        print("History : Script.py --history")
        print("Restore : Script.py --restore ZipFile Destination")


if __name__ == "__main__":
    main()
