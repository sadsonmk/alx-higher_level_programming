#!/usr/bin/python3
"""module to return the pascal triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangle = [[1] * (x + 1) for x in range(n)]

    for x in range(1, n):
        for y in range(x + 1):
            if y == 0 or y == x:
                triangle[x][y] = 1
            else:
                triangle[x][y] = triangle[x - 1][y - 1] + triangle[x - 1][y]
    return triangle
