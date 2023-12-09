#!/usr/bin/python3
"""Difine load_from_json_file function."""


import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".
    Args:
        filename: The name of json file.
    Return: The Object.
    """

    with open(filename, 'r') as file:
        return json.load(file)
