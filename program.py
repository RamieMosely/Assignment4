#Assignment 3
#PROG10004
#Ramie Mosely

import json
from datetime import datetime
import csv
from letter import Letter
from toy import Toy

class Program:
    def __init__(self):
        self._letters = []

    def run(self):
        self._log_action("Program has started!")

    def get_letters(self):
        return self._letters
    
    def _log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("ProgramLog.txt", "a") as log_file:
            log_file.write(f"{timestamp}: {action}\n")