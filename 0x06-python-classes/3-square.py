#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Initialize the class.
        Args:
            size (int): The size of the class.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    def area(self):
        return (self.__size ** 2)
