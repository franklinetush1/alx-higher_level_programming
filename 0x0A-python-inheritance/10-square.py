#!/usr/bin/python3
"""Reperesents a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Create a new square.
        Args:
            size: The size of the new square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
