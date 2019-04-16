from data_structures import AbstractStructure
from binary_heap import MinHeap

class Heap(AbstractStructure):
    def __init__(self):
        super().__init__()
        self._data = MinHeap()

    def get_min(self):
        return self._data.extract_root()

    def add(self, value):
        return self._data.add_element(value)