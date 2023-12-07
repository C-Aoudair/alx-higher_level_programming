#!/usr/bin/python3
"""Define the read_file function"""


def read_file(filename=""):
    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())
