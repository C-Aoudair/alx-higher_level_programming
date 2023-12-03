#!/usr/bin/python3
"""Define say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints the name.
    args:
    first_name: The first name.
    last_name: The last name.
    """

    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
