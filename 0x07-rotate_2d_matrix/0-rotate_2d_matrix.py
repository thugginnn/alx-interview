#!/usr/bin/python3
""" Rotate 2D Matrix """

def rotate_2d_matrix(matrix):
    """
    Rotates a given nxn 2D matrix 90 degrees clockwise in place.

    Parameters:
    matrix (list of list of int): The 2D matrix to rotate.

    Returns:
    None: The matrix is rotated in place.
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
