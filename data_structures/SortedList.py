from data_structures import AbstractStructure

class SortedList(AbstractStructure):
    def __init__(self):
        super().__init__()
        self._data = []

    def add(self, value):
        self._data.append(value)
        self._data.sort()

    def get_min(self):
        min_elem = self._data[0]
        self._data.remove(min_elem)
        return min_elem
