#!/usr/bin/python3
"""
Module generates log of HTTP requests with random IP addresses, timestamps,
status codes, and file sizes.
It demonstrates use of Python's random and datetime libraries to generate
random data.
"""

import random
import sys
from time import sleep
import datetime

# Loop 10000 times to generate 10000 log entries
for i in range(10000):
    # Sleep for a random duration between 0 and 1 second
    sleep(random.random())

    # Generate log entry with random IP address, current timestamp,
    # random status code, and random file size
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255),  # Random IP address
        datetime.datetime.now(),  # Current timestamp
        # Random status code
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)  # Random file size
    ))

    # Flush the output to ensure it gets printed immediately
    sys.stdout.flush()
