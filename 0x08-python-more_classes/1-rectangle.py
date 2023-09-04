#!/usr/bin/python3
"""This is a module for the class Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width attribute of the retangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the new width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height property of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to a new value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
