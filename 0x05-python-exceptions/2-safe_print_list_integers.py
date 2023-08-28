#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y = 0
    num = 0
    try:
        while y < x:
            if str(my_list[y]).isdigit():
                print("{:d}".format(my_list[y]), end='')
                num = num + 1
            y = y + 1
        print()
        return num
    except IndexError:
        return
