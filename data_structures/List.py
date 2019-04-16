from data_structures import AbstractStructure

class List(AbstractStructure):
    def __init__(self):
        super().__init__()
        self._data = []

    def get_min(self):
        min_elem = min(self._data)
        self._data.remove(min_elem)
        return min_elem

    def add(self, value):
        self._data.append(value)