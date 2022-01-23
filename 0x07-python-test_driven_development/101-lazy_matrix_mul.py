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
    m_c = []

    # check if m_a is a list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    # check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check if m_a is a list of lists
    for column in m_a:
        if type(column) is not list:
            raise TypeError("m_a must be a list of lists")
    # check if m_b is a list of lists
    for column in m_b:
        if not isinstance(column, list):
            raise TypeError("m_b must be a list of lists")

    # check if m_a is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    # check if m_b is empty
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # check if m_a contain only integer or floats
    for column in m_a:
        for row in column:
            if not isinstance(row, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    # check if m_b contain only integer or floats
    for column in m_b:
        for row in column:
            if not isinstance(row, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # This will return dot product
    m_c = np.dot(m_a, m_b)

    return m_c
