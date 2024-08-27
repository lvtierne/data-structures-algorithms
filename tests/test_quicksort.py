# Unit tests for QuickSort
import unittest
from src.algorithms.sorting.quicksort import quicksort

class TestQuickSort(unittest.TestCase):

    def test_quicksort(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = quicksort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
