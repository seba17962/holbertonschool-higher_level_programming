#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        for i in my_string:
            if (i == 'C' or i == 'c'):
                my_string.pop([i])
    return my_string
