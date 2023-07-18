#import dependencies
from setuptools import setup, find_packages
from typing import List

#define all the variables here
PROJECT_NAME = "ML Project"
VERSION = "0.0.1"
DESCRIPTION = "This is Intermediate Level ML project"
AUTHOR_NAME = "MADHU PINCHA"
AUTHOR_EMAIL = "dummy@learning.in"

#variable to call requirements.txt
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

'''get_requirements_list()
1. we will open requirements.txt file
2. replce \n by "" 
3. to install this setup.py we use -e .
Note: When we install setup.py, a new folder is created. But when we install requirements.txt again & again, this setup file will be installed again and that folder will get created many time, so we have to handle that situation'''
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        #but /n will be included in this list, which represents new line, we have to replace it by ""
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

#find_packages-> goes to main project directory(here, src) and finds packages used (in __init__.py)
#install_requires-> a variable that will install all the libraries which are in requirements.txt

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires= get_requirements_list()
     )