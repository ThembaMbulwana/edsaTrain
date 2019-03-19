import unittest
from sorting import *

class SortingTestCase(unittest.TestCase):
    """ Test for 'bubble_sort' function. """
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5,3,4,2,1]), [1,2,3,4,5])
        self.assertEqual(bubble_sort([100]), [100])
        self.assertEqual(bubble_sort([10, 20, 30]), [10,20,30])

    """ Test for 'merge_sort' function. """
    def test_merge_sort(self):
        self.assertEqual(merge_sort([100,10,1000]), [10, 100, 1000])
        self.assertEqual(merge_sort([9]), [9])
        self.assertEqual(merge_sort([40, 4, 4000, 400]), [4,40,400,4000]) 
    
    """ Test for 'quick_sort' function. """
    def test_quick_sort(self):
        self.assertEqual(quick_sort([1,2,3]), [1,2,3])
        self.assertEqual(quick_sort([80,8,800]), [8,80,800])
        self.assertEqual(quick_sort([-100]), [-100])

unittest.main()
