#!/usr/bin/python3
"""module to append a string at the end of file"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added
    """

    with open(filename, 'a', encoding='UTF8') as f:
        a_file = f.write(text)
    return (a_file)
