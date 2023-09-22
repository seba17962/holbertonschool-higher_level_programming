#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) == 2:
    print("{} argument:\n{}: {}".format(len(argv) - 1, len(argv) - 1, argv[1]))
elif len(argv) > 2:
    print("{} arguments:".format(len(argv)))
    for f in range(1, len(argv)):
        print("{}: {}".format(f, argv[f]))
