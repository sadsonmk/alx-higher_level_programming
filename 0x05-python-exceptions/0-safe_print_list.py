#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    y = 0
    for b in my_list:
        length = length + 1
    try:
        while y < x:
            if x > length:
                x = length
            print(my_list[y], end='')
            y = y + 1
        print()
    except Exception as e:
        print(e)
    if (x >= length):
        return length
    else:
        return x
