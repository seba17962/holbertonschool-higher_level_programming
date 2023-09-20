#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) + 1):
        if str[i] >= 97 and str[i] <= 122:
            print("{}".format((ord(str[i]) - 32)))
        else:
            print(f"{str[i]}")
