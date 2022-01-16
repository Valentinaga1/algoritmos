#!/usr/bin/python3
"""Rotate a matrix 90 degrees."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees.
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dim and will not be empty.
    Arguments
    ---------
    - matrix  : matrix
                list of non-negative integers.
    Returns
    -------
    - Nothing. The function modifies the original argument
    """
    copy = matrix[:]

    for i in range(len(matrix)):
        # extract the i column from the copy
        col_i = [row[i] for row in copy]
        # place it on the original matrix in reverse order
        matrix[i] = col_i[::-1]
