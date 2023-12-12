#!/usr/bin/python3

"""defines a Rectangle class"""


class Rectangle:
    """represents the Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize the object"""

        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if not self.__height or not self.__width:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = []
        for i in range(self.height):
            rectangle.append("#" * self.width)
            if i != self.height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
