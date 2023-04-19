#!/usr/bin/python3
"""Define class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set the new width"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the new height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rec = self.y * "\n"
        for i in range(self.height):
            rec += (" " * self.x)
            rec += ("#" * self.width) + "\n"

        print(rec, end='')

    def __str__(self):
        """Returns the representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ update class """
        if args is not None and len(args) != 0:
            lst = ['id', 'width', 'height', 'x', 'y']
            for a in range(len(args)):
                setattr(self, lst[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle."""
        return {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x,
            "y": self.y}
