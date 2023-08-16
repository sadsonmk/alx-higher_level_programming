#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    largest = 0
    for keys, values in a_dictionary.items():
        if a_dictionary[keys] > largest:
            largest = a_dictionary[keys]
            key = keys
    return key
