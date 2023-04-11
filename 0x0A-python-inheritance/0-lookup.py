#!/usr/bin/python3
"""Defines a lookup function"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object"""

    return(list(dir(obj)))
