#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    length = len(argv)

    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
        num = 1
        for arg in argv:
            if arg == argv[0]:
                continue
            print("{}: {}".format(num, arg))
            num = num + 1
    else:
        print("{} arguments:".format(length - 1))
        num = 1
        for arg in argv:
            if arg == argv[0]:
                continue
            print("{}: {}".format(num, arg))
            num = num + 1


