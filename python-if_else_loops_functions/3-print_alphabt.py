#!/usr/bin/python3
for alfabeth in range(ord('a'), ord('z') + 1):
    if alfabeth != ord('e') and alfabeth != ord('q'):
        print("{}".format(chr(alfabeth)), end='')
