import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.run_script()

    def run_script(self):
        if self.process:
            self.process.kill()
        print(f"Running {self.script}...")
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(f"{self.script} changed. Reloading...")
            self.run_script()

def main():
    if len(sys.argv) != 2:
        print("Usage: pyload myscript.py")
        sys.exit(1)

    script = sys.argv[1]
    event_handler = ReloadHandler(script)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
