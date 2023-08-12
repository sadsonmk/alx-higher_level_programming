#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = reversed(my_list)
    for x in new_list:
        print("{:d}".format(x))
