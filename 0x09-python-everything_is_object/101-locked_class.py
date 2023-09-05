#!/usr/bin/python3
"""
    This is a module that prevents the user
    from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    """
    A class with one attribute - first_name.
    """
    __slots__ = ["first_name"]
