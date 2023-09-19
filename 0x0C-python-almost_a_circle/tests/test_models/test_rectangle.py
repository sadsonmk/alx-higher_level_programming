#!/usr/bin/python3
"""module that contains tests to the project"""
import unittest
from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    """Test class inheriting from unittest"""

    def tearDown(self):
        Rectangle._Base__nb_objects = 0

    def test_rect(self):
        """testing the rectangle class"""
        self.r1 = Rectangle(10, 2)

        self.assertEqual(self.r1.id, 2)

    def test_valid(self):
        """validation of values"""
        self.r2 = Rectangle(200, 100)
        with self.assertRaises(ValueError):
            self.r2.height = -100
        with self.assertRaises(TypeError):
            self.r2.width = 'Hi'

    def test_area(self):
        """tests the area of the rectangle instance"""
        self.r3 = Rectangle(10, 100)
        self.assertEqual(self.r3.area(), 1000)

if __name__ == '__main__':
    unittest.main()
