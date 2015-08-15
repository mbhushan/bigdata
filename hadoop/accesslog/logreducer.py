#!/usr/bin/python

import sys

totalhits = 0

for line in sys.stdin:
    data = line.strip()
    if data == "yes":
        totalhits += 1

print totalhits
