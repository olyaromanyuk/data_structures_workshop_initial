import unittest
from data_structures import List as DataStructure

class TestDataStructure(unittest.TestCase):
    def test_data_structure(self):
        ds = DataStructure()
        ds.add(5)
        ds.add(1)
        ds.add(0)
        ds.add(2)
        ds.add(2)
        ds.add(4)

        self.assertEqual(ds.get_min(), 0)
        self.assertEqual(ds.get_min(), 1)
        self.assertEqual(ds.get_min(), 2)
        self.assertEqual(ds.get_min(), 2)
        self.assertEqual(ds.get_min(), 4)
        self.assertEqual(ds.get_min(), 5)