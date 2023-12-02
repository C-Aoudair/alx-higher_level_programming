#!/usr/bin/python3
"""matrix_divided"""


def matrix_divided(matrix, div):
    """divided a matrix by the number div.
    args:
    matrix: list of lists 0f integers or floats.
    div: The number to divide by.
    """

    if (
        not isinstance(matrix, list)
        or not all(isinstance(item, list) for item in matrix)
        or (
            not all(isinstance(num, int) for row in matrix for num in row)
            and not all(isinstance(num, float) for row in matrix for num in row)
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in row] for row in matrix]
