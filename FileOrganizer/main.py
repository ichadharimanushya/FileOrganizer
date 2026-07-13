from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  
SOURCE_DIR = Path().home()/"Downloads" # from where the files will be abducted...yes abducted!
DESTINATION_DIR = Path("D:/AllDocuments") # folders where the files will be sorted into

downloaded_files =  list(SOURCE_DIR.iterdir())
organised_folders = list(DESTINATION_DIR.iterdir())

organization_criteria = {
    "applicationexe":[".exe"],
    "images":[".jpg",".jpeg",".png",".gif",".webp"],
    "documents":[".pdf",".doc",".docx",".txt",".ppt",".pptx",".xlsx"],
    "videos":[".mp4",".mkv",".mov",".avi"],
    "audios":[".mp3",".wav",".flac"],
    "others":[".zip",".rar",".7z"]
}




for file in downloaded_files:
    if file.is_file():
        for key in organization_criteria:
            found = False
            if file.suffix in organization_criteria[key]: # the desktop.ini will be excluded
                for folder in organised_folders:
                    if folder.name == key:
                        found = True
                        break
                if not found:
                    (DESTINATION_DIR/key).mkdir()
                    # create a new dir with name key and add it to the destination_dir for future iterations
                    organised_folders.append(DESTINATION_DIR/key)
                shutil.move(src = file, dst = DESTINATION_DIR/key)
                break
                    



#  phrase 3:
#     handling name crashes, instead of overwriting the files, produce _1, _2, etc between the name and the extension
#     logging, storing the history, for better configuration use json to transfer files
