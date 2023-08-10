#!/usr/bin/python3

for alfbet in range(97, 123):
    if alfbet == 101 or alfbet == 113:
        continue
    print("{}".format(chr(alfbet)), end='')
