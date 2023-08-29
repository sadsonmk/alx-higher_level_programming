#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """this is a constructor function"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
