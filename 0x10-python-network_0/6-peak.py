#!/usr/bin/python3
"""this module contains a function to find a peak"""

def find_peak(list_of_integers):
    """a function to find a peak from a given list"""
    length = len(list_of_integers)
    temp = list_of_integers

    for i in range(1, length - 1):
        if temp[i] > temp[i - 1] and temp[i] > temp[i + 1]:
            return temp[i]
        elif temp[i] == temp[i + 1] and temp[i] == temp[i - 1]:
            return temp[i]
