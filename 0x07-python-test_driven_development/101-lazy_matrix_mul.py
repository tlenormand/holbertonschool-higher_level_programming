#!/usr/bin/python3
"""
module that multiply 2 matrix using NumPy

functions:
    lazy_matrix_mul: multiply 2 matrix
"""


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix using NumPy

    arguments:
        m_a: first matrix
        m_b: second matrix

    Return: new matrix multiplied
    """
    import numpy as np

    return np.matmul(m_a, m_b)
