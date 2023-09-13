#!/usr/bin/python3
"""module that puts class data into an object"""


def class_to_json(obj):
    """a function that returns the dictionary
    description with simple data structure
    """

    data = obj.__dict__
    return (data)
