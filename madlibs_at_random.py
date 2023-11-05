import os
import random

folder_name = "madlibs_games"
folder_path = os.path.abspath(folder_name)
file_list = [file for file in os.listdir(folder_path) if not file.startswith("__pycache__")]

if len(file_list) >= 2:
     selected_file = random.choice(file_list)
     file_to_run = os.path.join(folder_path, selected_file)

    
     exec(open(file_to_run).read())
else:
    print("There are not enough files in the folder to make a selection.")