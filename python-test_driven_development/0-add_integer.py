#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers (or floats) a and b.
    Both a and b are cast to integers if they are floats.
    Raises a TypeError if either a or b is not an integer or float.

    Args:
        a (int, float): The first number to be added.
        b (int, float, optional): The second number to be added (default is 98).

    Returns:
        int: The sum of a and b, both cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
