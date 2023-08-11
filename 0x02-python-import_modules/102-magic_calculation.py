#!/usr/bin/python3

def magic_calculation(a, b):
    if a < b:
        c = a + b
        for x in range(4, 7):
            c += x
        return c
    else:
        return a - b
