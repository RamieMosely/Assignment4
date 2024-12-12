class Toy:
    def __init__(self, name, category, description):
        self._name = name
        self._category = category
        self._description = description

    def get_name(self):
        return self._name
    
    def get_category(self):
        return self._category
    
    def get_description(self):
        return self._description
