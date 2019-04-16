from data_structures import AbstractStructure

class SortedListWithInsert(AbstractStructure):
    def __init__(self):
        super().__init__()
        self._data = []

    def add(self, value):
        i = 0
        while i < len(self._data) and not self._data[i] > value:
            i += 1
        self._data.insert(i, value)


    def get_min(self):
        min_elem = self._data[0]
        self._data.remove(min_elem)
        return min_elem
