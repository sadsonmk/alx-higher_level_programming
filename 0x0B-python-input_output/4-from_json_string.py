#!/usr/bin/python3
"""module to convert JSON into a python object"""
import json


def from_json_string(my_str):
    """
    a function that returns an object
    (Python data structure) represented by a JSON string
    """
    output = json.loads(my_str)

    return output
