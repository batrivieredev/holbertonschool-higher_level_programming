#!/usr/bin/python3
"""
Module for appending a string after each line containing a specific substring.

This module provides a function `append_after` which inserts a line of text
to a file after each line containing a specific substring.

Attributes:
    None
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    This method reads a file, searches for lines containing the `search_string`,
    and appends the `new_string` after each line that contains `search_string`.

    Args:
        filename (str): The name of the file to modify. The file must exist.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each matching line.
                          It must include the newline character `\n` if you want to start a new line.

    Returns:
        None

    Raises:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read all lines into memory

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)  # Write each line back to the file
            if search_string in line:
                file.write(new_string)  # Append new_string after the matching line

