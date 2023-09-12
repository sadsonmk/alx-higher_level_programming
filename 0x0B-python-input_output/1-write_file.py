#!/usr/bin/python3
"""a module to write to a file"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters writteni
    """
    with open(filename, 'w') as f:
        r_file = f.write(text)
    return r_file
