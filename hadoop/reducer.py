#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip()
    values = data.split("\t")
    for i in range(2):
        print "VAL: ", values[i]
