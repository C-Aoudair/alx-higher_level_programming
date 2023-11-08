#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key_of_big = list(a_dictionary.keys())[0]
    big = a_dictionary[key_of_big]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            key_of_big = k
    return (key_of_big)
