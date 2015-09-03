#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip()
    values = data.split("\t")
    # for i in range(2):
    #    print "VAL: ", values[i]
    if values[0].isalpha():
        continue
    marker = values[1]
    buff = None
    if marker == "N":
        buff = values[2:]
    elif marker == "U":
        buff.extend(values[2:])
    else:
        '\t'.join(buff)
