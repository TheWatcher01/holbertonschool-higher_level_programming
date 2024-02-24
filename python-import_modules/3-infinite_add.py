#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    _sum = 0
    for i in args:
        _sum += int(i)
print("{}".format(_sum))
