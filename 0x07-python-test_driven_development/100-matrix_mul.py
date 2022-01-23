#!/usr/bin/python3
"""
module that multiply 2 matrix

functions:
    matrix_mul: multiply 2 matrix
    check_matrix:
    check_row_matrix: check if each row have the same size
    new_matrix: create a new matrix using for multiplication of m_a * m_b
"""


def matrix_mul(m_a, m_b):
    """
    multiply 2 matrix

    arguments:
        m_a: first matrix
        m_b: second matrix

    Return: new matrix multiplied
    """
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

    # check if m_a is a rectangle
    if not check_row_matrix(m_a):
        raise TypeError("each row of m_a must be of the same size")
    # check if m_b is a rectangle
    if not check_row_matrix(m_b):
        raise TypeError("each row of m_b must be of the same size")

    # create a new matrix c for the multiplication of m_a * m_b
    m_c = new_matrix(m_a, m_b)

    # iterating by row of A
    for i in range(len(m_a)):

        # iterating by column by B
        for j in range(len(m_b[0])):

            # iterating by rows of B
            for k in range(len(m_b)):
                try:
                    m_c[i][j] += m_a[i][k] * m_b[k][j]
                except Exception:
                    raise ValueError("m_a and m_b can't be multiplied")

    return m_c


def new_matrix(m_a, m_b):
    """
    create a new matrix using for multiplication of m_a * m_b

    arguments:
        m_a: matrix a
        m_b: matrix b

    Return: the new matrix
    """
    len_row_a = 0
    len_row_b = 0
    len_column_a = 0
    len_column_b = 0
    m_c = []

    # count length of row and column for matrix a
    for row in m_a:
        len_row_a += 1
        len_column_a = 0
        for column in row:
            len_column_a += 1

    # count length of row and column for matrix b
    for row in m_b:
        len_row_b += 1
        len_column_b = 0
        for column in row:
            len_column_b += 1

    # take the minimum row and column between matrix a and b
    min_row_len = min(len_row_a, len_row_b)
    min_column_len = min(len_column_a, len_column_b)

    # create and initialize to 0 the matrix c
    for i in range(min_row_len):
        m_c.append([])
        for j in range(min_column_len):
            m_c[i].append(0)

    return m_c


def check_row_matrix(matrix):
    """
    check if each row have the same size

    arguments:
        matrix to check

    Return: true if each row have the same size, false otherwise
    """
    rows = len(matrix[0])
    for row in matrix:
        if len(row) != rows:
            return False
    return True
