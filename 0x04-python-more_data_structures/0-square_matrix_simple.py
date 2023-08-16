#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for x in matrix:
        x_matrix = []
        for y in x:
            x_matrix.append(y ** 2)
        new_matrix.append(x_matrix)

    return new_matrix
