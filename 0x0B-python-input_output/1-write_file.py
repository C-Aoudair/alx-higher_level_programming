#!/usr/bin/python3
"""Define wrtie_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file.
    args:
        filename: The name of the file.
        text: The text to be written in the file.
    Return:
        The number of characters written.
    """

    with open(filename, 'w') as file:
        count = file.write(text)

    return count
