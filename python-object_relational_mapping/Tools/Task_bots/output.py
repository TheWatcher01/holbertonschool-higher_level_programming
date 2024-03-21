#!/usr/bin/python3

def write_to_file(filename, rows):
    with open(filename, 'w') as f:
        for row in rows:
            f.write(str(row) + '\n')


def print_rows(rows):
    for row in rows:
        print(row)
