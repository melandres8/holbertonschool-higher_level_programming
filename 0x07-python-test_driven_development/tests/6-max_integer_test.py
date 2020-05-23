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

    def test_values1(self):
        with self.assertRaises(TypeError):
            max_integer(True, False)

    def test_values2(self):
        with self.assertRaises(TypeError):
            max_integer(1, "epa", 3, 7)

    def test_values3(self):
        with self.assertRaises(TypeError):
            max_integer("hola")
