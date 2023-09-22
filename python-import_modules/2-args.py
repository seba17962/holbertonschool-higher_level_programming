#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    a = len(argv)
    if a == 1:
        print("{} arguments.".format(a - 1))
    elif a == 2:
        print("{} argument:\n{}: {}".format(a - 1))
        print("{}: {}".format(a - 1, argv[1]))
    elif a > 2:
        print("{} arguments:".format(a))
        for f in range(1, a):
            print("{}: {}".format(f, argv[f]))
