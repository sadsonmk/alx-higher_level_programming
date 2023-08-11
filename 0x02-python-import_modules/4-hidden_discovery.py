#!/usr/bin/python3

from importlib import import_module
if __name__ == "__main__":
    hidden = import_module("hidden_4")
    hidden = dir(hidden)
    for name in hidden:
        if name[0:2] == "__":
            continue
        print("{}".format(name))
