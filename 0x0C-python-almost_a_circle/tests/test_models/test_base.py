#!/usr/bin/python3
"""module that contains tests to the project"""
import unittest
from models.base import Base


class TestBase_obj(unittest.TestCase):
    """Test class inheriting from unittest for Base class objects"""

    def test_base_zero_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


    def test_numerous_zero_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b4.id - 4)


    def test_supplied_id(self):
        self.assertEqual(Base(15).id, 15)

    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_string(self):
        self.assertEqual(Base('hi').id, 'hi')

    def test_id_bool(self):
        self.assertEqual(Base(True).id, True)

    def test_id_list(self):
        self.assertEqual(Base([1,2,3,4]).id, [1,2,3,4])
    
    def test_lotof_args(self):
        with self.assertRaises(TypeError):
            Base(12, 45)
