#!/usr/bin/python3
if _name_ == "__main__":
    import hidden_4

    list = dir(hidden_4)

    for name in list:
        if name[:2] != "__":
            print(name)
