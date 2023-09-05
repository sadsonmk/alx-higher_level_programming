#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        """find the largest number in a list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -4, -5, -10]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0.4, 0.8, 0.2, 0.5]), 0.8)
