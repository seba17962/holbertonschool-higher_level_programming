#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    only_one_number = set(my_list)
    for i in only_one_number:
        add += i
    return add
