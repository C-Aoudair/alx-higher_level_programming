#!/usr/bin/python3
"""Defines Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square class."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Gets size of Square class."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of Square class."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
