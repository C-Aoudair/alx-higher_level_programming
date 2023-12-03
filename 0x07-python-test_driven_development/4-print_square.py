#!/usr/bin/python3
"""Define print_square function"""


def print_square(size):
    """Prints a square with the character #.
    args:
    size: The size length of square.
    """

    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
