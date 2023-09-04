#!/usr/bin/python3
"""This is a module for the class Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """prints the rectangle using the # symbol"""
        if self.width == 0 or self.height == 0:
            return ('')
        else:
            value = []
            for x in range(self.height):
                for y in range(self.width):
                    value.append('#')
                if x != self.height - 1:
                    value.append('\n')
            return("".join(value))
