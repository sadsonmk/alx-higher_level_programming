#!/usr/bin/python3
"""module holding the base class"""
import json


class Base:
    """the base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """intitializes instances of the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
