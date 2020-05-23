#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases
    """

    def test_maxint(self):
        """cases
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-5, -1]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 5, 1]), 5)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([7218332, -1000, -123, -20]), 7218332)
        self.assertNotIn(max_integer([5, 4, 6]), [9, 4, 2])
        self.assertEqual(max_integer([13]), 13)

if __name__ == '__main__':
    unittest.main()
