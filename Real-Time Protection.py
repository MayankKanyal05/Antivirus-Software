from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class RealTimeScanner(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_modified(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        print(f"File modified: {file_path}")
        self.scan_file(file_path)

    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        print(f"File created: {file_path}")
        self.scan_file(file_path)

    def scan_file(self, file_path):
        file_hash = get_file_hash(file_path)
        if file_hash in known_virus_signatures:
            print(f"Virus detected in {file_path}!")
            quarantine_file(file_path)
            log_infection(file_path)

# Import necessary functions from antivirus.py
from antivirus import get_file_hash, quarantine_file, log_infection, known_virus_signatures

# Real-time protection setup
def start_real_time_protection(directory):
    event_handler = RealTimeScanner()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Run real-time protection (for a specific directory)
start_real_time_protection('C:/path/to/monitor')