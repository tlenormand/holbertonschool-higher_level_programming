#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix

    Args:
        matrix: initial matrix

    Returns a new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
"""


def square_matrix_simple(matrix=[]):
    result = []

    for sublist in matrix:
        row = []
        for item in sublist:
            row.append(item ** 2)
        result.append(row)

    return result
