#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    biggest_key = None
    score = None
    for keys, value in a_dictionary.items():
        if score is None or value > score:
            score = value
            biggest_key = keys
    return biggest_key
