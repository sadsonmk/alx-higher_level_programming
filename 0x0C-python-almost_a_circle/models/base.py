#!/usr/bin/python3
"""module holding the base class"""
import json
import os
import csv
import turtle as t


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
        if cls.__name__ == "Rectangle":
            obj = cls(3, 6)
        else:
            obj = cls(3)
        obj.update(args=None, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_file = "{}.json".format(cls.__name__)
        my_list = []

        if not os.path.exists(my_file):
            return []
        else:
            with open(my_file, 'r', encoding='UTF8') as f:
                result = f.read()
            res = cls.from_json_string(result)

            for values in res:
                value = cls.create(**values)
                my_list.append(value)
            return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        my_file = "{}.csv".format(cls.__name__)
        with open(my_file, 'w', encoding='UTF8') as csvf:
            if list_objs == [] or list_objs is None:
                csvf.write('[]')
            else:
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                write_csv = csv.DictWriter(csvf, fieldnames=fieldnames)
                for obj in list_objs:
                    write_csv.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a csv"""
        my_file = "{}.csv".format(cls.__name__)
        if not os.path.exists(my_file):
            return []
        else:
            with open(my_file, 'r', encoding='UTF8') as csvf:
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = ["id", "width", "height", "x", "y"]
                my_list = csv.DictReader(csvf, fieldnames=fieldnames)
                my_list = [dict([j, int(k)] for j, k in m.items())
                           for m in my_list]
                return [cls.create(**k) for k in my_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the square and rectangle using the turtle module"""
        my_t = t.Screen()
        my_t.bgcolor('blue')
        my_t.pensize(4)

        my_t.color('white')
        for rect in list_rectangles:
            my_t.up()
            my_t.goto(rect.x, rect.y)
            my_t.down()
            for r in range(2):
                my_t.fd(rect.width)
                my_t.lt(90)
                my_t.fd(rect.height)
                my_t.lt(90)
            my_t.ht()
        my_t.color('yellow')
        for sq in list_square:
            my_t.showturtle()
            my_t.up()
            my_t.goto(sq.x, sq.y)
            my_t.down()
            for s in range(4):
                my_t.fd(sq.width)
                my_t.lt(90)
            my_t.ht()

        my_t.done()
