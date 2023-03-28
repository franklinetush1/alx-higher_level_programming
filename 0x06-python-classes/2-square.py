#!/usr/bin/python3
class Square:
    """reperesenting a square"""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        
        elif size < 0:
            raise ValueError("size must be >= 0")
