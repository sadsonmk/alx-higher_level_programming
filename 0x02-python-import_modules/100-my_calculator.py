#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    args = len(argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        arg1 = int(argv[1])
        arg2 = argv[2]
        arg3 = int(argv[3])
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(arg1, arg3, add(arg1, arg3)))
            exit(0)
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(arg1, arg3, sub(arg1, arg3)))
            exit(0)
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(arg1, arg3, mul(arg1, arg3)))
            exit(0)
        elif argv[2] == 'div':
            print("{:d} / {:d} = {:d}".format(arg1, arg3, div(arg1, arg3)))
            exit(0)
        elif arg2 != '+' or arg2 != '-' or arg2 != '*' or arg2 != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
