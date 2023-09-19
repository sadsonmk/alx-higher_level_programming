#!/usr/bin/python3
"""module that contains tests to the project"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class inheriting from unittest"""
    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        """testing the ids of class base instances"""
        self.b1 = Base()

        self.assertEqual(self.b1.id, 1)

