#!/usr/bin/python3
for ascii_value in range(97, 123):
    if not (ascii_value == 101 or ascii_value == 113):
        print("{}".format(chr(ascii_value)), end="")
