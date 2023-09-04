#!/usr/bin/python3
"""A module that prints a square using the # symbol"""


def print_square(size):
    """A function that prints a square with the character #.

    Args:
        size (int): is the size length of the square.

    Raises:
        TypeError, ValueError
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif not isinstance(size, int) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for x in range(size):
            for y in range(size):
                print("#", end='')
            print()
