#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = [(key, value) for key, value in sorted(a_dictionary.items())]
    for item in new_list:
        print(f"{item[0]}: {item[1]}")
