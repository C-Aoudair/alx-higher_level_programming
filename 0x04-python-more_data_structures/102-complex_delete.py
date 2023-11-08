#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for c, h in list(a_dictionary.items()):
        if h is value:
            a_dictionary.pop(c)
    return a_dictionary
