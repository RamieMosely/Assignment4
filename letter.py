#This is the letter class it contains all the methods and attributes

class Letter:
    def __init__(self, id, first_name, last_name):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._toys = []
        self._approved = None

#Getter Methods
    def get_id(self):
        return self._id
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    def get_toys(self):
        return self._toys
    
    def get_approved(self):
        return self._approved
    
    def set_approved(self, status):
        self._approved = status

    def add_toy(self, toy):
        self._toys.append(toy)