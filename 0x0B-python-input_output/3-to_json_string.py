#!/usr/bin/python3
"""a module that turns an object into JSON"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)"""

    output = json.dumps(my_obj)

    return output
