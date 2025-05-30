# antivirus.py
import hashlib
import os
import shutil
import logging
from datetime import datetime
import time

# List of known virus hashes (MD5/SHA256 of known viruses)
known_virus_signatures = [
    "examplehash1", "examplehash2", "examplehash3"  # Add actual virus hashes
]

def get_file_hash(file_path):
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_directory(directory):
    start_time = time.time()
    print(f"\n🔍 Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    infected_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash in known_virus_signatures:
                print(f"⚠️  Virus detected: {file_path} at {datetime.now().strftime('%H:%M:%S')}")
                log_infection(file_path)
                quarantine_file(file_path)
                infected_files.append(file_path)

    end_time = time.time()
    print(f"\n✅ Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🕒 Total time: {end_time - start_time:.2f} seconds")
    print(f"🦠 Total infected files: {len(infected_files)}\n")
    return infected_files

def quarantine_file(file_path, quarantine_folder="quarantine/"):
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    try:
        shutil.move(file_path, os.path.join(quarantine_folder, os.path.basename(file_path)))
        print(f"📦 Moved to quarantine: {file_path}")
    except Exception as e:
        print(f"Error quarantining {file_path}: {e}")

def log_infection(file_path):
    logging.basicConfig(
        filename="antivirus_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )
    logging.info(f"Detected infected file: {file_path}")

if __name__ == "__main__":
    dir_to_scan = input("📁 Enter directory to scan: ")
    if os.path.exists(dir_to_scan):
        scan_directory(dir_to_scan)
    else:
        print("❌ Directory not found.")
