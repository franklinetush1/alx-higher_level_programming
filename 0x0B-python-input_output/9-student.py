#!/usr/bin/python3
""" Defines the class Student"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Initialize student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns description of the directory"""
        return self.__dict__.copy()
