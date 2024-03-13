import time
import subprocess
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JSFileHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.last_modified = None

    def on_modified(self, event):
        if event.src_path == self.filepath:
            current_modified = os.path.getmtime(self.filepath)
            if self.last_modified != current_modified:
                self.last_modified = current_modified
                os.system('cls')
                subprocess.run(["node", self.filepath], shell=True)

if __name__ == "__main__":
    js_filename = sys.argv[1]
    js_filepath = os.path.abspath(js_filename)
    event_handler = JSFileHandler(js_filepath)
    print('Observing for changes in file '+js_filename)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(js_filepath), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
