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

    def update(self, *args, **kwargs):
        """assigns a value to each attribute"""
        if not args and len(args) < 1:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        elif len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

    def to_dictionary(self):
        """returns a dictionary representation of the square"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}

    def __str__(self):
        """the string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
