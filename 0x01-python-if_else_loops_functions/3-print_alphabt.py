#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) != "e" and chr(ch) != "q":
        print("{}".format(chr(ch)), end="")
