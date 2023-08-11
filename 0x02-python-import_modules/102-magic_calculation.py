#!/usr/bin/python3

import magic_calculation_102
if __name__ == "__main__":
    def magic_calculation(a, b):
        if a < b:
            c = magic_calculation_102.add(a, b)
            for x in range(4, 7):
                c += x
            return c
        else:
            return magic_calculation_102.sub(a, b)
