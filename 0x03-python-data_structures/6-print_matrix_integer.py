#!/usr/bin/python3
"""function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            if column != 0:
                print(" ", end='')
            print("{:d}".format(matrix[line][column]), end='')
        print()
