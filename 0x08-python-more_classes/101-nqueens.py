#!/usr/bin/python3
"""
N queens puzzle
"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

# create a matrix of NxN
matrix = []
for i in range(N):
    matrix.append([0] * N)


def is_attack(i, j):
    # checking if there is a queen in row or column
    for k in range(0, N):
        if matrix[i][k] == 1 or matrix[k][j] == 1:
            return True
    # checking diagonals
    for k in range(0, N):
        for lr in range(0, N):
            if (k + lr == i + j) or (k - lr == i - j):
                if matrix[k][lr] == 1:
                    return True
    return False


def N_queen(n):
    # if n is 0, solution found
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i, j))) and (matrix[i][j] != 1):
                matrix[i][j] = 1
                # recursion
                # wether we can put the next queen with this arrangment or not
                if N_queen(n - 1) is True:
                    return True
                matrix[i][j] = 0

    return False


N_queen(N)
# for i in matrix:
#     print (i)
