#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False
