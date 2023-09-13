#!/usr/bin/python3
"""module that defines a student class"""


class Student:
    """defining a student class"""

    def __init__(self, first_name, last_name, age):
        """initializing instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """converting an object to JSON
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        """
        if (type(attrs) == list and all(type(x) == str for x in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
