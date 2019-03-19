import unittest
from recursion_plus_sorting.recursion import *

class RecursionTestCase(unittest.TestCase):
    """ Test for 'sum_array' function. """
    def test_sum_array(self):
        self.assertEqual(sum_array([1,2,3,4,5]), 15)
        self.assertEqual(sum_array([10,10,10]), 30)
        self.assertEqual(sum_array([10, 20, 30]), 60)

    """ Test for 'fibonacci' function. """
    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(20), 6765) 
    
    """ Test for 'factorial' function. """
    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    """ Test for 'reverse' function. """
    def test_reverse(self):
        self.assertEqual(reverse("Hello"), "olleH")
        self.assertEqual(reverse("P"), "P")
        self.assertEqual(reverse("All good"), "doog llA")

unittest.main()
