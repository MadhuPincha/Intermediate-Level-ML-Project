import os, sys
import logging
from datetime import datetime

#1. directory in which we want to create logs
#2. path of directory
#3. define format in which you want logs to be created
#4. file name
#5. file path
#6. logging configuration details you want

LOG_DIR = 'logs'
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename=log_file_path, 
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
