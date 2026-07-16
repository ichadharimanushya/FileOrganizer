from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  
import json     # for the love of the game
import logging  # for recording every step in case of something something...
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

SOURCE_DIR = Path().home()/"Downloads" # from where the files will be abducted...yes abducted!
DESTINATION_DIR = Path("D:/AllDocuments") # location where the files will be sorted into different folders

logging.basicConfig(level = logging.INFO,
                        filename = Path(__file__).parent/"info.log",
                        filemode = 'a',
                        format = "--|%(asctime)s|--\n\t> %(message)s\n")

with open(Path(__file__).parent/"config.json", 'r') as f:
    data = json.load(f)

class FolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            log(f"SKIPPED OVER THE FOLDER: {event.src_path}")
            return
        organise_file(Path(event.src_path), DESTINATION_DIR)

def log(message):
    logging.info(message)

def unique_filename(file, location):
    candidate_name = file.name
    candidate_path = location/candidate_name
    number = 0
    while candidate_path.exists():
        number += 1
        candidate_name = f"{file.stem}_{number}{file.suffix}"
        candidate_path = location/candidate_name
    return candidate_path

def create_folder(path):
    if not path.exists():
        path.mkdir()
        log(f"CREATED NEW FOLDER: {path}")

def get_folder_name(ext, configurations):
    for foldername in configurations:
        if ext in configurations[foldername]:
            return foldername
    return None

def organise_file(file, destination_path):
    folder = get_folder_name(file.suffix, data)
    if folder is None:
        log(f"UNKNOWN FILE FORMAT FOR: {file}")
        return
    create_folder(destination_path/folder)
    destination = unique_filename(file, destination_path/folder)
    while 1:
        try:
            shutil.move(src = file, dst = destination)
            log(f"MOVED FILE: | FROM: {file} | TO: {destination}")
            break
        except PermissionError as e:
            time.sleep(5)

def watchdog_observer():
    event_handler = FolderHandler() # instance of handler
    observer = Observer()           # instance of observer
    observer.schedule(event_handler, path=str(SOURCE_DIR), recursive=False)
    log(f"Monitoring started for: {SOURCE_DIR}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt: # ctrl + c
        observer.stop()
    observer.join()     # Wait until the background thread finishes cleaning up

def main():
    log("PROGRAM STARTED")
    watchdog_observer()
    log("PROGRAM ENDED\n\n\n")

if __name__ == "__main__":
    main()