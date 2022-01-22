#!/usr/bin/python3
"""
module divides all elements of a matrix

functions:
    matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix: matrix to divide
        div: number to divise the matrix

    Returns:
        new matrix divided
    """
    new_matrix = []
    len_line = 0

    if matrix is None or not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/f\
loats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for line in matrix:
        if not isinstance(line, list):
            raise TypeError("matrix must be a matrix (list of lists) of intege\
rs/floats")
        if len_line != 0:
            if len_line != len(line):
                raise TypeError("Each row of the matrix must have the same siz\
e")
        len_line = len(line)
        for col in line:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of in\
tegers/floats")

    for line in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), line)))

    return new_matrix
