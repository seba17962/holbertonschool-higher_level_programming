#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = my_string.replace('c', '').replace('C', '')
    return my_string
