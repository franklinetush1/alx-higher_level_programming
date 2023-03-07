#!/usr/bin/python3
for ch in range(97, 123):
    print(chr(ch), end="")

for ch in [x for x in range(97, 123) if x != 101 and x != 113]:
    print(chr(ch), end="")
