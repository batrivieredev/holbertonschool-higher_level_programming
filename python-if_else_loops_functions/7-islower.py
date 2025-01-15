#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.

    Args:
        c (str): A single character to check.

    Returns:
        bool: True if c is a lowercase letter, False otherwise.
    """
    if len(c) != 1:
        raise ValueError("Input must be a single character.")

    return ord('a') <= ord(c) <= ord('z')
