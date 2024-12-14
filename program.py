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

    def openLetterData(self):
        """Opens and reads letter data from JSON file"""
        try:
            with open("Letters.json", "r") as file:
                data = json.load(file)
                for letter_data in data:
                    letter = Letter(
                        letter_data["id"],
                        letter_data["first_name"],
                        letter_data["last_name"]
                    )
                    for toy_data in letter_data["toys"]:
                        toy = Toy(
                            toy_data["name"],
                            toy_data["category"],
                            toy_data["description"]
                        )
                        letter.add_toy(toy)
                    letter.set_approved(letter_data.get("approved"))
                    self._letters.append(letter)
            self._log_action("Opened letter data")
        except Exception as e:
            self._log_action(f"Error opening letter data: {str(e)}")
            raise

    def exportChildrenList(self):
        try:
            headers = ["Letter ID", "Full Name", "Nice"]

            with open("ChildrenListTemplate.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

                for letter in self._letters:
                    row = [
                        letter.get_id(),
                        letter.get_full_name(),
                        ""  
                    ]
                    writer.writerow(row)

            self._log_action("Exported children list to ChildrenListTemplate.csv")

        except Exception as e:
            self._log_action(f"Error exporting children list: {str(e)}")
            raise

    def importChildrenData(self):
        #This imports the children list as naughty or nice status and updates letter objects
        try:
            with open("ChildrenList.csv", "r", newline='') as file:
                reader = csv.DictReader(file)
                nice_status = {}

                for row in reader:
                    letter_id = int(row["Letter ID"])
                    is_nice = row["Nice"].lower() == "true"
                    nice_status[letter_id] = is_nice

                for letter in self._letters:
                    if letter.get_id() in nice_status:
                        letter.set_approved(nice_status[letter.get_id()])

            self.saveLetterData()
            self._log_action("Imported children data from CHildrenList.csv")

        except FileNotFoundError:
            error_msg = "ChildrenList.csv file not found"
            self._log_action(f"Error! {error_msg}")
            raise FileNotFoundError(error_msg)
        except Exception as e:
            self._log_action(f"Error importing children data: {str(e)}")
            raise

    def exportToyManufacturingData(self):
        try:
            headers = ["Name", "Category", "Description"]

            with open("RequestedToys.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writenow(headers)

                unique_toys = set()

                for letter in self._letters:
                    if letter.get_approved() == True:
                        for toy in letter.get_toys():
                            toy_info = (
                                toy.get_name(),
                                toy.get_category(),
                                toy.get_description()
                            )

                            if toy_info not in unique_toys:
                                unique_toys.add(toy_info)
                                writer.writerow(toy_info)
            
            self._log_action("Exported toy manufacturing data to RequestedToys.csv")

        except Exception as e:
            self._log_action(f"Error exporting toy manufacturing data: {str(e)}")
            raise

    def saveLetterData(self):
        try:
            letters_data = []

            for letter in self._letters:
                letter_dict = {
                    
                }




