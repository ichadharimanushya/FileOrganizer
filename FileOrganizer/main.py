from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  

WORKING_DIR = Path().home()/"Downloads" # from where the files will be abducted...yes abducted!
DIRECTED_DIR = Path("D:/AllDocuments") # folders where the files will be sorted into

downloaded_files =  list(WORKING_DIR.iterdir())
organised_folders = list(DIRECTED_DIR.iterdir())

