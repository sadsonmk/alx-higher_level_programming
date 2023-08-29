#!/usr/bin/python3
class Square:
    '''Defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''this is a constructor function'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''returns the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the value of size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        '''retrieves the position of the square'''
        return self.__position

    @position.setter
    def position(self, value):
        '''sets the position of the square'''
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        '''calculates the area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print('#', end='')
                print()
