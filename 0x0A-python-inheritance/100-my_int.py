#!/usr/bin/python3
"""a module for a class that inherits from the int class"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """defines the equal operator"""
        return not(True)

    def __ne__(self, other):
        """defines the not equal operator"""
        return not(False)
