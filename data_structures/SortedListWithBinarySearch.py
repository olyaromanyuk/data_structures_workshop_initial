from data_structures import AbstractStructure

class SortedListWithBinarySearch(AbstractStructure):
    def __init__(self):
        super().__init__()
        self._data = []

    def _search(self, value,left, right):
        if left+1 == right:
            if self._data[left]<value:
                return right
            else:
                return left
        middle = int((left+right)/2)
        if self._data[middle] > value:
            return self._search(value, left, middle)
        else:
            return self._search(value, middle, right)

    def add(self, value):
        if len(self._data) == 0:
            self._data.append(value)
        else:
            i = self._search(value, 0, len(self._data))
            self._data.insert(i, value)

    def get_min(self):
        min_elem = self._data[0]
        self._data.remove(min_elem)
        return min_elem
