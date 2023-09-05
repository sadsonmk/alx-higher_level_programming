#!/usr/bin/python3
"""module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """a function to multiply matrices"""

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    elif not all(isinstance(elem, list) for elem in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(elem, list) for elem in m_b):
        raise TypeError('m_b must be a list of lists')
    elif m_a == [] or m_a == [[]]:
        raise TypeError('m_a can\'t be empty')
    elif m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    else:
        row_one = m_a[0]
        for x in m_a:
            if len(x) != len(row_one):
                raise TypeError('each row of m_a must be of the same size')
            for y in x:
                if not isinstance(y, int) and not isinstance(y, float):
                    raise TypeError('m_a should contain only integers or\
                            floats')
        row_two = m_b[0]
        for i in m_b:
            if len(i) != len(row_two):
                raise TypeError('each row of m_b must be of the same size')
            for j in i:
                if not isinstance(j, int) and not isinstance(j, float):
                    raise TypeError('m_b should contain only integers or\
                            floats')
        result_matrix = []
        for row in m_a:
            new_row = []
            for col in m_b:
                res = 0
                for x in range(len(row)):
                    res += row[x] * col[x]
                    if not isinstance(res, int) and not isinstance(res, float):
                        raise TypeError("m_a and m_b can't be multiplied")
                new_row.append(res)
            result_matrix.append(new_row)
        return result_matrix
