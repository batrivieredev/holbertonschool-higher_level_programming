#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.
    
    :param filename: The name of the file to modify.
    :param search_string: The string to search for in each line.
    :param new_string: The string to insert after each matching line.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

