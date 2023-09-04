#!/usr/bin/python3
"""A module for matrix division"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.

    Args:
        matrix(list): a list of lists of integers/floats.
        div(int/float): the number to be used as the dividend.

    Returns:
        A new matrix with the result of the division.

    Raises:
        TypeError, ZeroDivisionError.

    """
    temp = []
    new_matrix = []
    for idx, x in enumerate(matrix):
        ahead = idx + 1
        if ahead >= len(matrix):
            break
        elif len(matrix[idx]) != len(matrix[idx + 1]):
            raise TypeError('Each row of the matrix must have the same size')
        else:
            for y in x:
                if not isinstance(y, int) and not isinstance(y, float):
                    raise TypeError('matrix must be a matrix \
                            (list of lists) of integers/floats')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        for x in matrix:
            for y in x:
                value = round((y / div), 2)
                temp.append(value)
            new_matrix.append(temp)
            temp = []
        return new_matrix
