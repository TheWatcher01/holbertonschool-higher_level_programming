#!/usr/bin/python3
"""
Module reads HTTP request logs from stdin, keeps track of total file size and
number of occurrences of each status code, and prints these statistics every
10 lines and when keyboard interruption occurs.
"""

import sys

# Initialize dict to keep track of number of occurrences of each status code
status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

total_size = 0  # Initialize the total file size
line_count = 0  # Initialize the line count

try:
    # Read from stdin line by line
    for line in sys.stdin:
        # Split the line into parts
        data = line.split(" ")

        # If the line has more than 2 parts (i.e., it's a valid log entry)
        if len(data) > 2:
            # Extract the status code and file size from the line
            status = data[-2]
            file_size = int(data[-1])

            # If status code is one of ones we're tracking, increment its count
            if status in status_codes:
                status_codes[status] += 1

            # Add the file size to the total file size
            total_size += file_size

            # Increment the line count
            line_count += 1

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))

# If keyboard interruption occur, print statistics one last time before exiting
except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
