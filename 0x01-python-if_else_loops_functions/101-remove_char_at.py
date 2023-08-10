#!/usr/bin/python3

def remove_char_at(str, n):
    output = ''
    length = len(str)
    if n > length - 1 or n < 0:
        return str
    remove = str[n]
    for x in str:
        if x == remove:
            continue
        output += x
    return output
