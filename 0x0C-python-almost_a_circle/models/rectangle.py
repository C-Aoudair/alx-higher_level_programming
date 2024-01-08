#!/usr/bin/python3
"""Defines Rectangle class."""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherites from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property.setter
    def width(self, value):
        return self.__width = value

    @property
    def height(self):
        return self.__height

    @property.setter
    def height(self, value):
        return self.__height = value

    @property
    def x(self):
        return self.__x

    @property.setter
    def x(self, value):
        return self.__x = value

    property
    def y(self):
        return self.__y

    @property.setter
    def y(self, value):
         return self.__y = value
