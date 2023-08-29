#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """this is a constructor function"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square"""
        if value[0] < 0 or value[1] < 0 or len(value) != 2
        or not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        else:
            [print("") for i in range(0, self.__position[1])]
            for x in range(0, self.__size):
                [print(" ", end='') for y in range(0, self.__position[0])]
                [print('#', end='') for z in range(0, self.__size)]
                print('')
