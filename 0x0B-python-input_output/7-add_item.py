#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys


def save_to_json_file(my_obj=[], filename="add_item.json"):
    """a function that writes an Object to a text file using JSON"""

    for args in sys.argv:
        if args is not sys.argv[0]:
            my_obj.append(args)
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

    return my_obj


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""

    filename = save_to_json_file()
    with open(filename, 'r') as f:
        data = json.load(f)
        return (data)
