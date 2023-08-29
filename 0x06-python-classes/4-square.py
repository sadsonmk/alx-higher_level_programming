#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """this is a constructor function"""
        self.__size = size

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """calculates the area of the square"""
        return self.__size * self.__size    
