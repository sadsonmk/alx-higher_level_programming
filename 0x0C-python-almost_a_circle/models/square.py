#!/usr/bin/python3
"""the module that contains the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class inheriting from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes instances of the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """the string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
