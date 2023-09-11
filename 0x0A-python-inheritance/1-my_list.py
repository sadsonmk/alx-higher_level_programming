#!/usr/bin/python3
"""A module with a class that inherits from the list class"""


class MyList(list):
    """MyList class inherits from the list class"""

    def print_sorted(self):
        """prints a sorted list(ascending order)"""

        print(sorted(self))
