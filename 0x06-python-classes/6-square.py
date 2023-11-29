#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0,0)):
        """Initialize the class.
        Args:
            size (int): The size of the class.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        message = "position must be a tuple of 2 positive integers"
        if isinstance(position, tuple) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1],int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(message)
            else:
                raise TypeError(message)
        else:
            raise TypeError(message)

    def area(self):
        return self.__size**2

    def my_print(self):
        if not self.size:
            print("")
        else:
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
            """else:
                for i in range(self.size):
                    print(" " * self.position[0], end="")
                    print("#" * self.size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")"""
