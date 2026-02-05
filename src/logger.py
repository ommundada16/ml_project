import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #it cretes a new file alwyas with the name as the dat,time,etc - to make sure we know when the log file wwas created 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)       #makes a file name logs in the current working directory 
os.makedirs(logs_path, exist_ok=True)                    #makes sure that the system doesnt crash if the file already exists and cretes the file if it doesnt exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(                                                                  #basic format of info that will be stored in the file 
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":                         #__name__ is the hidden tag given to each file by python, and __main__ checks if the main file where thsi code is written open rigth now and the run button is pressed in this current file for logger . if this code is imported in anyother file and run then this line wont be printed , it only prints when this ffile for logger is run (main file)
    logging.info("Logging has started")