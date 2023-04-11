#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Create a new Rectangle.
        Args:
            width : The width of the new Rectangle.
            height : The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
