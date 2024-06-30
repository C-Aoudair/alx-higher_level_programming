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
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

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

    def update(self, *args, **kwargs):
        """Updates Square class."""
        attributes = ["id", "size", "x", "y"]

        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
