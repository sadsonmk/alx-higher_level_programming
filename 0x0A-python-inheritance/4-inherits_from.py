#!/usr/bin/python3
"""
    module to check if an object is an instance of a subclass
"""


def inherits_from(obj, a_class):
    """
    a function to check if an object is an instance of a subclass
    """
    obj_class = type(obj)
    if obj_class != a_class and issubclass(obj_class, a_class):
        return True
    else:
        return False
