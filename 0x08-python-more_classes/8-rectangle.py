#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """creates a rectangle object
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rectangle.append(str(self.print_symbol))
            if a != self.__height - 1:
                rectangle.append("\n")
        return("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle"""
        R = "Rectangle(" + str(self.__width)
        R += ", " + str(self.__height) + ")"
        return(R)

    def __del__(self):
        """Print message on Rectangle Deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with bigger area
        Arguments:
            rect_1 (Rectangle): First Rectangle.
            rect_2 (Rectangle): Second Rectangle.
        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
