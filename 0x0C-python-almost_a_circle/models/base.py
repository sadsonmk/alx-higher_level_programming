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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        my_file = cls.__name__
        if list_objs is None or len(list_objs) == 0:
            res = "[]"
        else:
            my_list = []

            for i in list_objs:
                my_list.append(i.to_dictionary())
                res = cls.to_json_string(my_list)
        with open(f"{my_file}.json", 'w') as f:
            f.write(res)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_obj = cls(20, 20)
        dummy_obj.update(*args=None, **dictionary)
        return dummy_obj
