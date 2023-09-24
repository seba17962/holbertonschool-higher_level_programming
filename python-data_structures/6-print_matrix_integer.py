#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            for y in x:
                condition = x.index(y) == len(x) - 1
                print("{:d}".format(y), end='' if condition else ' ')
            print('')
