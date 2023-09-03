#!/usr/bin/python3
"""A module to add two integers"""


def add_integer(a, b=98):
    """A function that adds two integers.

    Args:
        a (int/float): the first argument to be added.
        b (int/float): the second argument to be added.
    Returns:
        int: The sum of a and b.
    Raises:
        TypeError: Raises an exception if a or b is neither an int nor a float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return int(a + b)
