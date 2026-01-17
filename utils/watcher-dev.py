import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartDockerHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_run = 0

    def on_any_event(self, event):
        # Ignoriere Verzeichnisse und versteckte Dateien (wie .git)
        if event.is_directory or '/.' in event.src_path:
            return
        
        # Debouncing: Verhindert Mehrfach-Restarts innerhalb von 2 Sekunden
        current_time = time.time()
        if current_time - self.last_run > 2:
            print(f"Änderung erkannt: {event.src_path}. Neustart wird ausgeführt...")
            subprocess.run(["docker", "compose", "restart"])
            self.last_run = current_time

if __name__ == "__main__":
    path = "."  # Aktuelles Verzeichnis
    event_handler = RestartDockerHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print(f"Beobachte Änderungen in {path}...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()