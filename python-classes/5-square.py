#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square():
    """Definition of size in square"""

    def get_size(self):
        return self.__size

    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(get_size, set_size)

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
