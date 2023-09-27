#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        for i in range(len(my_list)):
            if i < x:
                print("{}".format(my_list[i]), end='')

        print()
        return my_list[i]
