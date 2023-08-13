#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    
    if matrix == [[]]:
        print()
        return
    length = len(matrix)
    for x in range(length):
        for y in range(length):
            print("{:d}".format(matrix[x][y]), end=' ')
        print()
