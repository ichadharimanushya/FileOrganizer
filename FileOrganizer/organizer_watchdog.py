import organizer
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

SOURCE_DIR = Path().home()/"Downloads"
DESTINATION_DIR = Path("D:/AllDocuments")

class FolderHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        time.sleep(5)
        organizer.organise_folder(SOURCE_DIR, DESTINATION_DIR)

def watchdog_observer():
    event_handler = FolderHandler() # instance of handler
    observer = Observer()           # instance of observer
    observer.schedule(event_handler, path=str(SOURCE_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt: # ctrl + c
        pass
    finally:
        observer.stop()
        observer.join()     # Wait until the background thread finishes cleaning up

def organise_and_observer():
    organizer.organise_folder(SOURCE_DIR, DESTINATION_DIR)
    watchdog_observer()