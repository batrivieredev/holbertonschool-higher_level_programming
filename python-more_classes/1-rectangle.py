#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle
width must be an integer, width need to be less than 0
height must be an integer, height need to be less than 0
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
