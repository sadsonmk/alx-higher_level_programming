#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    total = 0
    for arg in argv:
        if arg == argv[0]:
            continue
        arg = int(arg)
        total += arg
    print("{}".format(total))
