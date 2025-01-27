#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of size in square"""

    def __init__(self, size=0, position=(0, 0)):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is tuple and len(position) == 2 and\
            type(position[0]) is int and type(position[1]) is int and\
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and\
            type(value[0]) is int and type(value[1]) is int and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end='')
                for _ in range(self.__size):
                    print("#", end='')
                print()
