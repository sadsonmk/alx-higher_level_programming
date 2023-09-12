#!/usr/bin/python3
"""a module for reading files"""


def read_file(filename=""):
    """a function to read a file and prints it to stdout"""

    with open(filename, 'r', encoding='utf8') as f:
        r = f.read()
        print(r)
