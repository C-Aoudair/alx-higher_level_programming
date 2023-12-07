#!/usr/bin/python3
"""Define the read_file function"""


def read_file(filename=""):
    """Reads the file and prints it to stdout.
    args:
    filename: The name of the file.
    """

    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())
