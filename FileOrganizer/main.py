from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  
import json     # for the love of the game
import logging  # for recording every step in case of something something...

SOURCE_DIR = Path().home()/"Downloads" # from where the files will be abducted...yes abducted!
DESTINATION_DIR = Path("D:/AllDocuments") # location where the files will be sorted into different folders

logging.basicConfig(level = logging.INFO,
                        filename = Path(__file__).parent/"info.log",
                        filemode = 'a',
                        format = "--|%(asctime)s|--\n\t> %(message)s\n")

with open(Path(__file__).parent/"config.json", 'r') as f:
    data = json.load(f)

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

def organise_file(source_path, destination_path):
    for file in Path(source_path).iterdir():
        if file.is_file():
            folder = get_folder_name(file.suffix, data)
            if folder == None:
                log(f"UNKNOWN FILE FORMAT FOR: {file}")
                continue
            create_folder(destination_path/folder)
            destination = unique_filename(file, destination_path/folder)
            shutil.move(src = file, dst = destination)
            log(f"MOVED FILE: | FROM: {file} | TO: {destination}")
        else:
            log(f"SKIPPED OVER THE FOLDER: {file}")

def main():
    log("PROGRAM STARTED")
    organise_file(SOURCE_DIR, DESTINATION_DIR)
    log("PROGRAM ENDED\n\n\n")

if __name__ == "__main__":
    main()