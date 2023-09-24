#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
        tuple_sentence = (length, first_char)
        return tuple_sentence
    length = len(sentence)
    tuple_sentence = (length, None)
    return(tuple_sentence)
