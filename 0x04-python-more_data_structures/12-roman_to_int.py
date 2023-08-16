#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    numerls = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    old_value = 0
    for numeral in roman_string:
        new_value = numerls[numeral]
        if new_value > old_value:
            total -= (2 * old_value)
        total += new_value
        old_value = new_value
    return total
