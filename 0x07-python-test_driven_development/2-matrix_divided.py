#!/usr/bin/python3
"""Defines a function to divide matrix elements"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number to divide by
    Raises:
        TypeError:  If the matrix contains non-numbers
                    If the matrix contains rows of different sizes
                    If div is not an int or float.
        ZeroDivisionError: If div is zero
    Returns:
        A new matrix with the result of the division
    """

    matlength = 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err)

    for value in matrix:
        if not value or not isinstance(value, list):
            raise TypeError(err)

        if matlength != 0 and len(value) != matlength:
            raise TypeError("Each row of the matrix must have the same size")

        for num in value:
            if not isinstance(num, (int, float)):
                raise TypeError(err)

        matlength = len(value)

    s = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (s)
