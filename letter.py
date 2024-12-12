class Letter:
    def __init__(self, id, first_name, last_name):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._toys = []
        self._approved = None

    def get_id(self):
        return self._id
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self)
        return self._last_name
    
    