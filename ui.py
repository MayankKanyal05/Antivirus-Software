# ui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from antivirus import scan_directory, quarantine_file, log_infection

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Antivirus App")
        self.root.geometry("500x400")
        
        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Antivirus Scanner", font=("Arial", 20))
        self.title_label.pack(pady=10)
        
        # Scan Directory Button
        self.scan_button = tk.Button(self.root, text="Scan Directory", command=self.scan_directory, width=20, height=2)
        self.scan_button.pack(pady=10)
        
        # Log Area (Scrollable Text Box)
        self.log_area = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.log_area.pack(pady=10)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="Select a directory to scan", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def scan_directory(self):
        # Open file dialog to select folder
        directory = filedialog.askdirectory(title="Select a Folder to Scan")
        if not directory:
            return
        
        # Update status
        self.status_label.config(text=f"Scanning {directory}...")

        # Start the scan
        infected_files = scan_directory(directory)
        if infected_files:
            self.status_label.config(text="Scan Complete. Infected files found.")
            self.show_infected_files(infected_files)
        else:
            self.status_label.config(text="Scan Complete. No infected files found.")
            self.log_area.insert(tk.END, "No infected files found.\n")
        
    def show_infected_files(self, infected_files):
        for infected_file in infected_files:
            # Display infected file in log area
            self.log_area.insert(tk.END, f"Infected: {infected_file}\n")
            self.log_area.yview(tk.END)

            # Ask user if they want to quarantine the file
            quarantine_button = tk.Button(self.root, text=f"Quarantine {infected_file}", command=lambda f=infected_file: self.quarantine(f))
            quarantine_button.pack(pady=5)

    def quarantine(self, infected_file):
        quarantine_file(infected_file)
        log_infection(infected_file)
        self.log_area.insert(tk.END, f"File quarantined: {infected_file}\n")
        self.status_label.config(text="Infected file quarantined.")

# Create the main window
root = tk.Tk()

# Create the AntivirusApp instance
app = AntivirusApp(root)

# Run the application
root.mainloop()
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
def scan_directory(directory):
    start_time = time.time()
    print(f"\n🔍 Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    infected_files = []
    scanned_file_count = 0  # New counter

    for root, dirs, files in os.walk(directory):
        for file in files:
            scanned_file_count += 1  # Count each file
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
    print(f"📄 Total files scanned: {scanned_file_count}")
    print(f"🦠 Total infected files: {len(infected_files)}\n")
    
    return infected_files, scanned_file_count  # Return both
