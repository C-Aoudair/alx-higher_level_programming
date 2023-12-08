#!/usr/bin/python3
"""Define append_write function"""

def append_write(filename="", text=""):
    """Appends a string at the and of a text file.
    Args:
        filename: The name of the file.
        text: The string to be appended to the file.
    Return:
        The number of characters added.
    """

    with open(filename, "a") as file:
        return file.write(text)
