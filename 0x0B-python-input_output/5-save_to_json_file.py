#!/usr/bin/python3
"""
a module that writes an Object to a
text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file using JSON"""

    obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        file_r = f.write(obj)
        return file_r
