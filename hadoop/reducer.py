#!/usr/bin/python

import sys

buff = None
for line in sys.stdin:
    data = line.strip()
    values = data.split("\t")
    if not values[0].strip('"').isdigit():
        continue
    marker = values[1].strip('"')
    # print "marker: ", marker
    if marker == "N":
        buff = values[2:]
        # print "N_buff: ", buff
    elif marker == "U":
        buff.extend(values[2:])
        # print "U_buff: ", buff
        buff = '\t'.join(buff)
        print buff
        buff = None
