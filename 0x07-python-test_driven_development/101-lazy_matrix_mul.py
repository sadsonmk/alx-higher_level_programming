#!/usr/bin/python3
"""module to multiply matrices using numpy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices by using the module NumPy"""

    new_m_a = np.array(m_a)
    new_m_b = np.array(m_b)

    result = np.dot(new_m_a, new_m_b)
    return result
