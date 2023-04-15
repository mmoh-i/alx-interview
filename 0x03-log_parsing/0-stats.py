#!/usr/bin/python3
'''a script to read stdin line by line and computes metrics'''


import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[8])
        file_size = int(parts[9])
    except:
        continue

    total_size += file_size
    status_codes[status_code] += 1
    line_count += 1

    if line_count % 10 == 0:
        print("Total file size: File size: {}".format(total_size))
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print("{}: {}".format(code, count))

print("Total file size: File size: {}".format(total_size))
for code, count in sorted(status_codes.items()):
    if count > 0:
        print("{}: {}".format(code, count)))
