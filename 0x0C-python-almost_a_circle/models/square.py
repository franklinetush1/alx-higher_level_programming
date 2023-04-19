#!/usr/bin/python3
"""Represent Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update class """
        if args != 0 and len(args) is not None:
            lst = ['id', 'size', 'x', 'y']
            for a in range(len(args)):
                if lst[a] == 'size':
                    setattr(self, 'width', args[a])
                    setattr(self, 'height', args[a])
                else:
                    setattr(self, lst[a], args[a])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            "id": self.id, "size": self.width,
            "x": self.x, "y": self.y
        }
