#!/usr/bin/python

import sys

final_path = None
maxcount = 0
old_path = None
count = 0

for line in sys.stdin:
    path = line.strip()
    if old_path and path != old_path:
        if count > maxcount:
            maxcount = count
            final_path = old_path
        count = 0
    count += 1
    old_path = path

print final_path, "\t", maxcount
