#!/usr/bin/python3
'''a script to read stdin line by line and computes metrics'''


import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    # Parse the line
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[8])
        file_size = int(parts[9])
    except:
        # If the line cannot be parsed, skip it
        continue

    # Update variables
    total_size += file_size
    status_codes[status_code] += 1
    line_count += 1

    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print("Total file size: File size: {}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print("{}: {}".format(code, count))

# Print final statistics
print("Total file size: File size: {}".format(total_size))
for code, count in sorted(status_codes.items()):
    if count > 0:
        print("{}: {}".format(code, count)))
