#!/usr/bin/python3
"""Defines class base"""
import json
import csv
import os.path


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                lst = [a.to_dictionary() for a in list_objs]
                jsonfile.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            xc = cls(5, 5)
        else:
            xc = cls(5)
        xc.update(**dictionary)
        return xc

    @classmethod
    def load_from_file(cls):
        """Return a list of classes from a file of JSON strings"""
        nme = str(cls.__name__) + ".json"
        try:
            with open(nme, "r") as jsonfile:
                lst = Base.from_json_string(jsonfile.read())
                return [cls.create(**a) for a in lst]
        except IOError:
            return []
