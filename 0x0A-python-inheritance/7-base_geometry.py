#!/usr/bin/python3
"""A module containing the basegeometry class"""


class BaseGeometry:
    """
    The BaseGeometry class
    """
    def area(self):
        """a method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
