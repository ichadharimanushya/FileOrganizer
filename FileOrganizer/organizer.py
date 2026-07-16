from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  
import json     # for the love of the game

with open(Path(__file__).parent/"config.json", 'r') as f:
    data = json.load(f)

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

def get_folder_name(ext, configurations):
    for foldername in configurations:
        if ext in configurations[foldername]:
            return foldername
    return None

def organise_folder(source_path, destination_path):
    for file in source_path.iterdir():
        if not file.is_file(): continue
        print(file.name)
        folder = get_folder_name(file.suffix, data)
        if folder is None:
            continue
        create_folder(destination_path/folder)
        destination = unique_filename(file, destination_path/folder)
        shutil.move(src = file, dst = destination)