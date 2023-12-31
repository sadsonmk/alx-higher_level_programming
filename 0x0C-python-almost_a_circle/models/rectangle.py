#!/usr/bin/python3
"""module defining the rectangle class"""
from models.base import Base
import json


class Rectangle(Base):
    """defining the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intialize the attributes of a rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width attribute of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute of the rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """returns the height attribute of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute of the rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """returns the x attribute of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute of the rectangle"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns the y attribute of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute of the rectangle"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        [print("") for i in range(0, self.__y)]
        for x in range(0, self.__height):
            [print(" ", end='') for y in range(0, self.__x)]
            [print('#', end='') for z in range(0, self.__width)]
            print('')

    def __str__(self):
        return f"[Rectangle]\
 ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns a value to each attribute"""
        if not args and len(args) < 1:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.__width)
            self.height = kwargs.get('height', self.__height)
            self.x = kwargs.get('x', self.__x)
            self.y = kwargs.get('y', self.__y)
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

    def to_dictionary(self):
        """returns a dictionary representation of the rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'width': self.width,
                'height': self.height}
