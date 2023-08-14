#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 == 1 or len2 == 1:
        return (tuple_a[0] + tuple_b[0], 0)

