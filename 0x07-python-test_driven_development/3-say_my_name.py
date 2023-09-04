#!/usr/bin/python3
"""A module that prints the first name and the last name"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>.

    Args:
        first_name (string): The first name value.
        last_name (string): The last name value.

    Raises:
        TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print(f"My name is {first_name} {last_name}")
