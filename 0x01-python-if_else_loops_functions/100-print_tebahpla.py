#!/usr/bin/python3

for x in range (122, 96, -1):
    if x % 2 == 1:
        x = x - 32
    print("{}".format(chr(x)), end='')

