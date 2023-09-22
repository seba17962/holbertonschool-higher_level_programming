#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    _args = len(argv) - 1
    if len(argv) == 1:
        print("{} arguments.".format(_args))
    elif len(argv) == 2:
        print("{} argument:".format(_args))
        print("{}: {}".format(_args, argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(_args))
        for i in range(1, len(argv)):
            print("{}: {}".format((i), argv[i]))
