#!/usr/bin/python3
"""Defines a Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class the inherites from Rectangle class."""

    def __init__(self, size):
        self.integer_validator(size)
        super().__init__(size, size)
