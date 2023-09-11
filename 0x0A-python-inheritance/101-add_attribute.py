#!/usr/bin/python3
"""a module that adds an attribute to an object"""


def add_attribute(obj, name, value):
    """a function to add an attribute to an object"""

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
