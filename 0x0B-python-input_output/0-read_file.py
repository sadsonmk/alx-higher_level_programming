#!/usr/bin/python3
"""a module for reading files"""


def read_file(filename=""):
    """a function to read a file and prints it to stdout"""

    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            print(line, end='')
