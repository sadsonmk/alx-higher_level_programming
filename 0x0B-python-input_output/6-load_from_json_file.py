#!/usr/bin/python3
"""a module that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""

    with open(filename, "r") as f:
        data = json.load(f)
        return (data)
