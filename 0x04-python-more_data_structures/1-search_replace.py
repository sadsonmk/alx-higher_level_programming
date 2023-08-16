#!/usr/bin/python3

def search_replace(my_list, search, replace):
    length = len(my_list) - 1
    new_list = []
    for x in my_list:
        new_list.append(x)
    for i in range(length):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
