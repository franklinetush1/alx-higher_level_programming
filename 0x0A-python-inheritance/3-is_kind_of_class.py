#!/usr/bin/python3
"""Defines function that checks if object
is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if object is an istance of a class
    Args:
        Obj- Object to be checked
        a_class - Class to be compared to
    Return:
        True if obj is an instance of a_class
        False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
