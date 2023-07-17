#import requirements
import os, sys
from pathlib import Path
import logging

#script will ask user to enter the project name.
while True:
    project_name = input("Enter your project name : ")
    if project_name != "":
        break

#list of all the files & folder you want python to automatically create for you.
list_of_files = [
    #folders inside project_folder (project_name)
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",

    #folders in main directory
    f"config/config.yaml",
    f"schema.yaml",
    f"app.py",
    f"main.py",
    f"logs.py",
    f"exception.py",
    f"setup.py"
]

#for loop-> split files & folders and will generate these.
for filepath in list_of_files:
    filepath = Path(filepath)
    #split files & folders
    filedir, filename = os.path.split(filepath)

    #create a directory if it's empty and skip if already exists
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
    #if filepath doesn't exists or size of file is 0, then open folder and generate files in that
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info("File is already present at: {filepath}")