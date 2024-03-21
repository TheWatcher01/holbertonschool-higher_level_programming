#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import argparse
from database import connect_to_database, get_all_states, get_states_starting_with_n
from output import write_to_file, print_rows

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filter", help="Filter states starting with N", action="store_true")
    parser.add_argument(
        "--write", help="Write output to a file", action="store_true")
    args = parser.parse_args()

    db = connect_to_database()
    cur = db.cursor()

    expected_output = [(1, 'California'), (2, 'Arizona'),
                       (3, 'Texas'), (4, 'New York'), (5, 'Nevada')]
    expected_output_filter = [(4, 'New York'), (5, 'Nevada')]

    if args.filter:
        rows = get_states_starting_with_n(cur)
        if rows == expected_output_filter:
            print("Output is correct.")
            if args.write:
                write_to_file('1-filter_states.py', rows)
            else:
                print_rows(rows)
        else:
            print("Output is incorrect.")
    else:
        rows = get_all_states(cur)
        if rows == expected_output:
            print("Output is correct.")
            if args.write:
                write_to_file('0-select_states.py', rows)
            else:
                print_rows(rows)
        else:
            print("Output is incorrect.")
    cur.close()
    db.close()
