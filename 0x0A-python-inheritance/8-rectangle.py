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

        if type(value) != int and not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


# Defining a rectangle class that inherits from class BaseGeometry
class Rectangle(BaseGeometry):
    """A rectangle class that inherits from basegeometry"""

    def __init__(self, width, height):
        """initializes attributes"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
