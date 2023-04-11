#!/usr/bin/python3
""" Defines a class that inherits from the list class"""


class MyList(list):
    """Class inherits from list class"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
