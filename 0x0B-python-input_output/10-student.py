#!/usr/bin/python3
""" Defines the class Student"""


class Student:
    """Creates student instances"""

    def __init__(self, first_name, last_name, age):
        """ Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns description of the directory"""
        return self.__dict__.copy()

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ty) == str for ty in attrs)):
            ret = {m: getattr(self, m) for m in attrs if hasattr(self, m)}
            return(ret)
        return self.__dict__
