import os, sys
from flask import Flask
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    try:
        raise Exception("We are testing our exception file")
    except Exception as e:
        ML=CustomException(e, sys)
        logging.info(ML.error_message)
        logging.info("We are testing our logging file.")

    return "Welcome to exception-logging testing."

if __name__ == '__main__':
    app.run(debug=True) #port by default=5000