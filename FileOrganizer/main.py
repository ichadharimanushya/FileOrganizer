from pathlib import Path  # for the path of the files and stuff
import shutil   # moving and copying the files  
import json     # for the love of the game
import logging  # for recording every step in case of something something...


SOURCE_DIR = Path().home()/"Downloads" # from where the files will be abducted...yes abducted!
DESTINATION_DIR = Path("D:/AllDocuments") # folders where the files will be sorted into

downloaded_files =  list(SOURCE_DIR.iterdir())
organised_folders = list(DESTINATION_DIR.iterdir())


# organization_criteria = {
#     "applicationexe":[".exe"],
#     "images":[".jpg",".jpeg",".png",".gif",".webp"],
#     "documents":[".pdf",".doc",".docx",".txt",".ppt",".pptx",".xlsx"],
#     "videos":[".mp4",".mkv",".mov",".avi"],
#     "audios":[".mp3",".wav",".flac"],
#     "others":[".zip",".rar",".7z"]
# }

config = Path(__file__).parent/"config.json"
with open(config, 'r') as f:
    data = json.load(f)



logging.basicConfig(level = logging.INFO,
                    filename = Path(__file__).parent/"info.log",
                    filemode = 'a',
                    format = "%(asctime)s - %(levelname)s - %(message)s")


# for file in downloaded_files:
#     if file.is_file():
#         for key in organization_criteria:
#             found = False
#             if file.suffix in organization_criteria[key]:
#                 for folder in organised_folders:
#                     if folder.name == key:
#                         found = True
#                         break
#                 if not found:
#                     (DESTINATION_DIR/key).mkdir()
#                     organised_folders.append(DESTINATION_DIR/key)
#                 shutil.move(src = file, dst = DESTINATION_DIR/key)
#                 break
                    



#  phrase 3:
#     handling name crashes, instead of overwriting the files, produce _1, _2, etc between the name and the extension
#     logging, storing the history, for better configuration use json to transfer files

logging.info("PROGRAM STARTED")

for file in downloaded_files:
    if file.is_file():
        for key in data:
            found = False
            if file.suffix in data[key]:
                for folder in organised_folders:
                    if folder.name == key:
                        found = True
                        break
                if not found:
                    (DESTINATION_DIR/key).mkdir()
                    logging.info(f"CREATED FOLDER: {DESTINATION_DIR/key}")
                    organised_folders.append(DESTINATION_DIR/key)
                
                # move the file
                candidate_name = file.name
                candidate_path = DESTINATION_DIR/key/candidate_name
                number = 1
                while candidate_path.exists():
                    logging.info(f"DUPLICATE DETECTED: {candidate_path}")
                    candidate_name = f"{file.stem}_{number}{file.suffix}"
                    candidate_path = DESTINATION_DIR/key/candidate_name
                    logging.info(f"TRYING FILENAME: {candidate_name}")
                    number += 1
                shutil.move(src = file, dst = candidate_path)
                logging.info(f"MOVED FILE | FROM: {file} | TO: {candidate_path}")
    else:
        logging.info(f"SKIPPED FOLDER: {file}")


logging.info("PROGRAM FINISHED")


                # potential_duplicates = list((DESTINATION_DIR/key).iterdir())
                # duplicate_files = 0
                # for f in files_at_destination_dir:
                #     if file.name == f.name and file.suffix == f.suffix:
                #         duplicate_files += 1
                # if not duplicate_files:
                #     shutil.move(src = file, dst = DESTINATION_DIR/key)
                # else:
                #     parent_file = file.parent
                #     file_name = file.stem
                #     file_extension = file.suffix
                #     new_file_name = f"{file_name}_{duplicate_files}{file_extension}"
                #     final_file = Path(parent_file/new_file_name)
                #     shutil.move(src = final_file, dst = DESTINATION_DIR/key)
                # break


                # number = 0
                # file_name_ = file.name
                # while (DESTINATION_DIR/key/file_name_ in potential_duplicates):
                #     number += 1
                #     parent_file = file.parent
                #     file_name = file.stem
                #     file_extension = file.suffix
                #     new_file_name = f"{file_name}_{number}{file_extension}"
                #     file_name_ = Path(parent_file/new_file_name)
                # shutil.move(src = file, dst = parent_file/new_file_name)  
                # shutil.move(src = file_name_, dst = DESTINATION_DIR/key)
                # break