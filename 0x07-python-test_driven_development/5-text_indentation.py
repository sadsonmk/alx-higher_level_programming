#!/usr/bin/python3
"""A module that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """


def text_indentation(text):
    """prints text with 2 new lines after each of these characters: .,? and :

    Args:
        text (str): The input string

    Raises:
        TypeError

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for idx, char in enumerate(text):
            print(char, end='')
            if char == '.' or char == ',' or char == '?' or char == ':':
                print()
                print() 
