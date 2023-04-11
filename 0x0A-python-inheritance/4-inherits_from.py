#!/usr/bin/python3
"""Defines a function that checks wether a
    class inherists from another class"""


def inherits_from(obj, a_class):
    """Defines a function that checks wether a
    class inherists from another class
    Args:
        obj - class to be tested
        a_class - class to be checked against
    Return:
        True: if the obj class inherits from the specified class
    otherwise:
        False
        """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
