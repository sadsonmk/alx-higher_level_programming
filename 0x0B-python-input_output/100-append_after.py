#!/usr/bin/python3
"""module to append a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename) as f:
        data = ''
        for line in f:
            data += line
            if search_string in line:
                data += new_string

    with open(filename, 'w') as f1:
        f1.write(data)
