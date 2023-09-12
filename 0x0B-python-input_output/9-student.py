#!/usr/bin/python3
"""module that defines a student class"""


class Student:
    """defining a student class"""

    def __init__(self, first_name, last_name, age):
        """initializing instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converting an object to JSON"""



