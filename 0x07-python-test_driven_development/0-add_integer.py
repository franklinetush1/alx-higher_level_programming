#!/usr/bin/python3
"""Defines a function to add two integers"""


def add_integer(a, b=98):
    """Adds two integers
    Raises:
      Typeerror if input is not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
