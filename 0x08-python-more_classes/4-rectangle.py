#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """creates a rectangle object"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width"""
        return(self.height)

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height"""
        return(self.height)

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return(0)
        return((self.__height + self.__width) * 2)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for a in range(self.__height):
            for b in range(self.__width):
                rectangle.append("#")
            if a != self.__height - 1:
                rectangle.append("\n")
        return("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle"""
        R = "Rectangle(" + str(self.__width)
        R += ", " + str(self.__height) + ")"
        return(R)
