#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """Class that inherits from int"""

    def __eq__(self, value):
        """Returns not check."""
        return self.real != value

    def __ne__(self, value):
        """Returns check"""
        return self.real == value
