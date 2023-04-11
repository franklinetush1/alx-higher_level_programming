#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.
    Args:
        obj: The object to add an attribute to.
        att: Attribute to add to obj.
        value: The value of att.
    Raises:
        TypeError - If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
